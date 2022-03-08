from fastapi import APIRouter,Depends,status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from routers.schemas import PostDisply

from db import db_post
from db.database import get_db
from routers.schemas import PostBase

router = APIRouter(
    prefix='/post',
    tags = ['post']
)

image_url_types = ['absolute','relative']

@router.post('',response_model= PostDisply)
def create(request:PostBase,db:Session=Depends(get_db)):
    if request.imge_url_type not in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Prameter image url type can only take absolute or realtive.")
    return db_post.create(db,request)