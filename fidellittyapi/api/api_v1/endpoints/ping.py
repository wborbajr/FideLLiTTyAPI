from fastapi import APIRouter

router = APIRouter()


@router.get("/ping", tags=["ping"])
async def pong():
    return {"Response": "Pong"}
