from fastapi import FastAPI, HTTPException, Form, Request
from pydantic import BaseModel
import user_orm as orm
from datetime import date
from fastapi.templating import Jinja2Templates

app = FastAPI()
TEMPLATE = Jinja2Templates("templates")

class User(BaseModel):
    username:str
    password:str
    email:str
    
    class Config:
        orm_mode = True
@app.post("/signup")
async def signup(request: Request, username = Form(),
                 password = Form(), email=Form()):
    new_user = User(username=username, password=password, email=email)
    try:
        db_user = orm.Users.create(username= new_user.username,
                                   password=new_user.password,
                                   email=new_user.email,
                                    creation_date=date.today())
    except AssertionError as e:
        raise HTTPException(status_code=500, detail=e)
    except TypeError as t:
        return {'msg' : e}
    
    return TEMPLATE.TemplateResponse(
        'signup.html',
        {
            'request':request
        }
    )
@app.get("/signup")
async def get(request:Request):
    return TEMPLATE.TemplateResponse('signup.html',{'request':request})

@app.get("/success")
async def success(request:Request):
    return TEMPLATE.TemplateResponse('success.html',
                                     {
                                        'request':request,
                                     })
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level='debug')
