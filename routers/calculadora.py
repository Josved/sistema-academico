
from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/calculadora",
    tags=["Calculadora"]
)

@router.get("/suma")
def suma(a: float = Query(...), b: float = Query(...)):
    return {"operacion": "suma", "a": a, "b": b, "resultado": a + b}

@router.get("/resta")
def resta(a: float = Query(...), b: float = Query(...)):
    return {"operacion": "resta", "a": a, "b": b, "resultado": a - b}

@router.get("/multiplica")
def multiplica(a: float = Query(...), b: float = Query(...)):
    return {"operacion": "multiplica", "a": a, "b": b, "resultado": a * b}

@router.get("/divide")
def divide(a: float = Query(...), b: float = Query(...)):
    if b == 0:
        return {"error": "No se puede dividir entre cero"}
    return {"operacion": "divide", "a": a, "b": b, "resultado": a / b}
