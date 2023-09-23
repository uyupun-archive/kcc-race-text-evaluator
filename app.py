import uvicorn
from fastapi import FastAPI

from routes import text_evaluate
from settings import get_settings

settings = get_settings()


def init_app() -> FastAPI:
    app = FastAPI()
    return app


def register_routes(app: FastAPI) -> None:
    app.include_router(router=text_evaluate.router)


def run_app(app: FastAPI) -> None:
    uvicorn.run(app="app:app", host=settings.ADDRESS, port=settings.PORT, reload=True)


app = init_app()
register_routes(app=app)

if __name__ == "__main__":
    run_app(app=app)
