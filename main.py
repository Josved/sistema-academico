from fastapi import FastAPI
from routers import estudiantes, calculadora



app = FastAPI(
    title="Sistema Académico API",
    description="API para gestión de estudiantes",
    version="1.0.0"
)

app.include_router(estudiantes.router)
app.include_router(calculadora.router)

@app.get("/")
def read_root():
    return {
        "mensaje": "Bienvenido al Sistema Académico",
        "version": "1.0.0",
        "docs": "/docs"
    }
