from fastapi import FastAPI

app = FastAPI()



###### 路由 #####

@app.get("/")
async def hello():
    return {"msg":"你好Fastapi"}