from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic.error_wrappers import ValidationError

app = FastAPI()

items = [
    {
        'name':'cola',
        'price':'2000'
    },
    {
        'name':'cola_s',
        'price':'1000'
    },
    {
        'name':'sos',
        'price':'2000'
    }
]

@app.get("/search-by-price/{price}")
async def search_by_price(price:Optional[str]):
    l_items = []
    for i in items:
        if i['price'] == price:
            l_items.append(i['name'])
    if l_items:
        return {'result': l_items}
    if not l_items:
        raise HTTPException(status_code=404, detail='we dont have any product with this price')
        

@app.get("/search-by-name/{name}")
async def search_by_name(name:Optional[str]):  
    result :dict = {}
    for i in items:
        if i['name'] == name:
            result = i
    if result:
        return result
    if not result:
        raise HTTPException(status_code=500, detail='we dont have any product with this price')   


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level='debug')