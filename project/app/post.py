from fastapi import FastAPI, Request, APIRouter, Depends, HTTPException, status
from schema.post_schema import Posts
from database.fastapi_shop_orm import Post, get_db
from sqlalchemy.orm import Session

router = APIRouter()






@router.get('/posts')
async def show_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return {'post': posts}

@router.get("/posts/{post_id}")
async def show_posts(post_id:int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    return {'msg': post}

@router.post('/add-post')
async def add_post(new_post: Posts, db: Session = Depends(get_db)):
    post = Post(**new_post.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return {'msg': 'post added successful'}

@router.delete('/posts/{post_id}')
async def delete_post(post_id:int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id)
    if not post.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="post with id {post_id} does not exit"
        )
    post.delete(synchronize_session=False)
    db.commit()
    return {'msg':'post deleted'}

@router.put('/posts/{post_id}')
async def update_post(post_update: Posts, post_id:int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id)
    if not post.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="post with id {post_id} does not exit"
        )
    post.update(post_update.dict(), synchronize_session=False)
    db.commit()
    return {'msg':'post updated'}

