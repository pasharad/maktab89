from fastapi import FastAPI
from typing import List


app = FastAPI()


@app.get("/sum-numbers")
async def sum(number:str) -> dict:
    l_number = number.split(',')
    sum = 0
    for i in l_number:
        sum += int(i)
    return {'sum':sum}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level='debug')
