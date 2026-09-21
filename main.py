from fastapi import FastAPI,Path,Query

app = FastAPI()



###### 路由 #####

@app.get("/")
async def hello():
    return {"msg":"你好Fastapi"}

##### 参数 ###
# 1.路径参数
@app.get("/user/{name}")
async def hello(name:str=Path(...,min_length=2,max_length=4)):
    return {"name":f"{name}"}

# 2.查询参数
@app.get("/user")
async def hello(name:str=Query(default="mh"),age:int=Query(default=25)):
    return {"name":f"{name}","age":f"{age}"}

# 请求体参数
from pydantic import BaseModel,Field
class User(BaseModel):
    name:str
    age:int

@app.post("/users")
async def user(user:User):
    return user
