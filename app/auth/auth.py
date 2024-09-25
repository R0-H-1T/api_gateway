from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
    OAuth2PasswordRequestForm,
)
from app.helper import Tags
from typing import Annotated
from app.auth.dependency import get_async_client
from app.auth.models import User
import httpx

router = APIRouter(tags=[Tags.auth])

prefix_url = "http://localhost:8082"


@router.post("/signup")
async def signup(
    user: User, client: Annotated[httpx.AsyncClient, Depends(get_async_client)]
):
    r = await client.post(url=f"{prefix_url}/signup", json=user.model_dump())

    print(r.status_code)
    if r.status_code != status.HTTP_201_CREATED:
        return HTTPException(status_code=r.status_code)

    return r.json()


@router.post("/signin")
async def signin(
    user: Annotated[OAuth2PasswordRequestForm, Depends()],
    client: Annotated[httpx.AsyncClient, Depends(get_async_client)],
):

    r = await client.post(
        url=f"{prefix_url}/signin",
        data={
            "username": user.username,
            "scopes": user.scopes,
            "grant_type": user.grant_type,
            "password": user.password,
            "client_id": user.client_id,
            "client_secret": user.client_secret,
        },
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "accept": "application/json",
        },
    )
    print(r.status_code)
    if r.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=r.status_code)

    return r.json()


@router.get("/signout")
async def signout(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    client: Annotated[httpx.AsyncClient, Depends(get_async_client)],
):
    r = await client.get(
        url=f"{prefix_url}/signout",
        headers={"Authorization": f"{credentials.scheme} {credentials.credentials}"},
    )

    if r.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=r.status_code)


@router.get("/token")
async def token(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    client: Annotated[httpx.AsyncClient, Depends(get_async_client)],
):
    r = await client.get(
        url=f"{prefix_url}/token",
        headers={"Authorization": f"{credentials.scheme} {credentials.credentials}"},
    )

    if r.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=r.status_code)

    return r.json()
