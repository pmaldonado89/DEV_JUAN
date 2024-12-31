from backend.core.modelos.schemas import MinerSchema
from backend.core.modelos.modelos import MinerModel
from fastapi import APIRouter, HTTPException, Depends
from backend.core.config.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/miners/")
def create_miner(miner: MinerSchema, db = Depends(get_db)):
    db_miner = MinerModel.create(miner)
    db.add(db_miner)
    db.commit()
    db.refresh(db_miner)
    return db_miner


@router.get("/miners/")
def read_miners(db = Depends(get_db)):
    miners = db.query(MinerModel).all()
    return miners

@router.put("/miners/{miner_id}")
def update_miner(miner_id: int, miner: MinerSchema, db = Depends(get_db)):
    db_miner = db.query(MinerModel).filter(MinerModel.id == miner_id).first()
    if db_miner is None:
        raise HTTPException(status_code=404, detail="Miner not found")
    db_miner.full_name = miner.full_name
    db_miner.id_type = miner.id_type
    db_miner.id_number = miner.id_number
    db_miner.municipality = miner.municipality
    db.commit()
    db.refresh(db_miner)
    return db_miner

@router.delete("/miners/{miner_id}")
def delete_miner(miner_id: int, db = Depends(get_db)):
    db_miner = db.query(MinerModel).filter(MinerModel.id == miner_id).first()
    if db_miner is None:
        raise HTTPException(status_code=404, detail="Miner not found")
    db.delete(db_miner)
    db.commit()
    return db_miner
