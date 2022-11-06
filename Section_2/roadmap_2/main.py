import fastapi
import uvicorn

print("Hello fastapi")
api = fastapi.FastAPI()

@api.get('/api/endpoint')
def endpoint():
    return {"msg": "Hello everyone"}

uvicorn.run(api)