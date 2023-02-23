from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import user_orm as orm
from datetime import date
from validation import username_validation, password_validation, email_validation

app = FastAPI()

class User(BaseModel):
    username:str
    password:str
    email:str
    
    class Config:
        orm_mode = True
@app.post("/signup")
async def signup(new_user: User):
    try:
        db_user = orm.Users.create(username=username_validation(new_user.username), 
                                    password=password_validation(new_user.password), 
                                    email=email_validation(new_user.email), 
                                    creation_date=date.today())
    except AssertionError as e:
        raise HTTPException(status_code=500, detail=e)
    except TypeError as t:
        return {'msg' : e}
    
    return db_user

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level='debug')
