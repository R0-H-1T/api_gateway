from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.helper import Tags
from app.dependency import get_async_client
from httpx import AsyncClient

router = APIRouter(tags=[Tags.analytics])

prefix_url = "http://localhost:8084"


@router.get("/qna/{qna_id}", status_code=status.HTTP_200_OK)
async def analytics(
    qna_id: int,
    client: Annotated[AsyncClient, Depends(get_async_client)],
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
):
    res = await client.get(
        url=f"{prefix_url}/analytics/{qna_id}",
        headers={"Authorization": f"{credentials.scheme} {credentials.credentials}"},
    )

    if res.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=res.status_code)

    return res.json()

''''
api gateway - api/v1/analytics/qna/{qna_id}

analytics/{qna_id}

qna/{id}

'''