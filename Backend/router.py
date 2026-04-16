from fastapi import APIRouter
import endpoint
import login
import db

router = APIRouter()

router.include_router(endpoint.router, prefix="/events", tags=["events"])

router.include_router(login.router, tags=["auth"])

router.include_router(db.router, tags=["db"])