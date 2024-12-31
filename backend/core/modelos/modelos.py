from sqlalchemy import Column, Integer, String

class Miner(Base):
    __tablename__ = 'miner'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    id_type = Column(String)
    id_number = Column(String)
    municipality = Column(String)


