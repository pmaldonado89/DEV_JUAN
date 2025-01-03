# Proyecto de GestiÃ³n de Mineros

AplicaciÃ³n web para gestionar informaciÃ³n de mineros de subsistencia usando **React con TypeScript** (frontend) y **FastAPI** (backend). Docker se utiliza para el despliegue.

---

## TecnologÃ­as Utilizadas

- **Frontend**: React + TypeScript
- **Backend**: FastAPI
- **Base de Datos**: SQL Server
- **Docker**: ContenerizaciÃ³n
- **Vite**: Desarrollo rÃ¡pido
- **Axios**: Solicitudes HTTP

---

## CaracterÃ­sticas

1. **CRUD de Mineros**: Crear, leer, actualizar y eliminar mineros (nombre, tipo y nÃºmero de identificaciÃ³n, municipio).
2. **AutenticaciÃ³n**: Protege las operaciones administrativas.
3. **Docker**: Contenedores para frontend, backend y base de datos.

---

## Instrucciones de InicializaciÃ³n

1. **Clonar el Repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>
   ```

2. **Levantar Servicios con Docker Compose**:
   ```bash
   docker-compose up --build
   ```

3. **Acceder a la AplicaciÃ³n**:
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - Backend: [http://localhost:8000/docs](http://localhost:8000/docs)

4. **Configurar Variables de Entorno**:
   Archivos `.env` para frontend y backend.

---

## Estructura del Proyecto

```
/backend
    Dockerfile
    app/
/frontend
    Dockerfile
    src/
/docker-compose.yml
```

---

## Desarrollo Local

Frontend:
```bash
cd frontend
npm install
npm run dev
```

Backend:
```bash
cd backend
uvicorn app.main:app --reload
```

---
