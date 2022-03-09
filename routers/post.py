import random
import string

from fastapi import APIRouter,Depends,status,UploadFile,File
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from routers.schemas import PostDisply
from typing import List

from db import db_post
from db.database import get_db
from routers.schemas import PostBase
import shutil

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

@router.get('/posts',response_model=List[PostDisply])
def get_post(db:Session=Depends(get_db)):
    return  db_post.get_all(db)

@router.post('/image')
def upload_image(image:UploadFile=File(...)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.',1))
    path = f'images/{filename}'

    with open(path,"w+b") as buffer:
        shutil.copyfileobj(image.file,buffer)

    return  {'filename':path}
