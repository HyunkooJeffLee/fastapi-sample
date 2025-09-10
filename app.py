# app.py
from contextlib import asynccontextmanager
from typing import Annotated
from fastapi import FastAPI, APIRouter, Depends
from services import Greeter, SimpleGreeter


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.greeter = SimpleGreeter()  # ← 실제 운영에선 여기서 DB/Settings 등 초기화
    yield
    # 종료 훅에서 정리 작업


app = FastAPI(lifespan=lifespan)
router = APIRouter(prefix="/api")


def get_greeter() -> Greeter:
    return app.state.greeter  # 앱 상태에 올려둔 인스턴스 반환


@router.get("/hello")
async def hello(
    greeter: Annotated[Greeter, Depends(get_greeter)],  # 기본값 없는 인자 → 앞에 배치
    name: str = "World",
):
    msg = await greeter.greet(name)
    return {"message": msg}


app.include_router(router)


@app.get("/")
async def root():
    return {"status": "ok"}
