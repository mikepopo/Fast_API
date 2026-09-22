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


##### 请求与响应 ######
#1.装饰器中指定响应类
from fastapi.responses import HTMLResponse
@app.get("/html",response_class=HTMLResponse)
async def book():
    return "<H1>这是一级标题</H1>"

#2.return 中返回响应对象
from fastapi.responses import FileResponse
@app.get("/sponse")
async def book1():
    return FileResponse("./File/Snipaste_2026-09-22_10-44-00.png")

#3.自定义类响应数据格式
from pydantic import BaseModel
class News(BaseModel):
    id:str
    title:str
    content:str

@app.get("/news{id}",response_model=News)
async def books(id:str):
    return {
        "id":f"该书的编号为{id}",
        "title":"余华",
        "content":"这是一本好书"

    }

#### 异常 ####
from fastapi import FastAPI,HTTPException
@app.get("/new/{id}")
async  def get_news(id:int):
    id_list=[1,2,3,4,5]
    if id not in id_list:
        raise HTTPException(status_code=404,detail="当前ID不存在")
    return {"id":id}


##### 中间件 ####

@app.middleware("http")
async def book(request,call_next):
    print("中间件2 start")
    response =await call_next(request)
    print("中间件2 end")
    return response

@app.middleware("http")
async def book1(request,call_next):
    print("中间件1 start")
    response =await call_next(request)
    print("中间件1 end")
    return response