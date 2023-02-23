from fastapi import FastAPI
from typing import Optional

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

@app.get("/search-by-price/")
async def search_by_price(price:Optional[str]):
    l_items = []
    for i in items:
        if i['price'] == price:
            l_items.append(i['name'])
    return {'result': l_items}

@app.get("/search-by-name/")
async def search_by_name(name:Optional[str]):
    for i in items:
        if i['name'] == name:
            return {'result': i}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level='debug')
