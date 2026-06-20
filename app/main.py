from fastapi import FastAPI

from app.models import Greeting

# Egyszerű FastAPI alkalmazás. A Swagger UI a /docs címen érhető el,
# itt a nem technikai résztvevők is látják a működő terméket.

app = FastAPI(
    title="DEDIH 2.0 CI/CD demo",
    description="Demo alkalmazás a CI/CD és DevSecOps kurzushoz.",
    version="0.1.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    # Egészségcsekk végpont. A CI futásban és a böngészőben is használható.
    return {"status": "ok"}


@app.post("/greet")
def greet(payload: Greeting) -> dict[str, str]:
    # A Greeting modell a Pydantic-tól kapja a validációt.
    # Ha a bemenet nem jó, a FastAPI automatikusan 422-vel válaszol.
    return {"message": f"Szia, {payload.name}!"}
