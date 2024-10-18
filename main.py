#path_query_header.py
from fastapi import FastAPI, Header ,Depends,Cookie, Response, HTTPException # type: ignore
from typing import Optional

app = FastAPI()

# Example 1: Path Parameter
@app.get("/numbers/{number1}")
async def read_item(number1: int):
    return {"number1": number1}

# Example 2: Query Parameter (optional)
@app.get("/items/")
async def read_items(number1: Optional[int]=0, number2: int = 10):
    return {"number1": number1, "number2": number2}

# Example 3: Header Parameter
@app.get("/req_headers/")
def req_header_param(number1: str = Header(...)): #... for required value 
    return {"number1": number1}


@app.get("/optional_headers/")
def optional_header_param(number1: str = Header(None)):# None for optional value 
    return {"number1": number1}


#dependency.py

def sum(a:int,b:int):
    return a+b


@app.get("/sum")
def get_sum(answer:int=Depends(sum)):
    return f"the answer of the two number is {answer}"


#cookies.py


# Endpoint to set a cookie
@app.get("/set-cookie/")
async def set_cookie(color_value:str,my_response: Response):
    my_response.set_cookie(key="color", value=color_value, httponly=True)
    return {"message": f"Cookie 'color' has been set to {color_value}"}

# Endpoint to read a cookie
@app.get("/get-cookie/")
async def get_cookie(color: str = Cookie(None)):
    if color:
        return {"message": f"Hello, {color}!"}
    else:
        raise HTTPException(status_code=404, detail="Cookie not found")

# Endpoint to delete a cookie
@app.get("/delete-cookie/")
async def delete_cookie(response: Response):
    response.delete_cookie(key="color")
    return {"message": "Cookie 'color' has been deleted"}