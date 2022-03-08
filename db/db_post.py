import datetime

from sqlalchemy.orm import Session

from routers.schemas import PostBase
from db.models import DbPost

def create(db:Session,requiest: PostBase):
    new_post = DbPost(
        image_url = requiest.image_url,
        image_url_type = requiest.imge_url_type,
        caption = requiest.caption,
        timestamp = datetime.datetime.now(),
        user_id = requiest.creator_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post