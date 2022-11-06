import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get("/api/pass_data1")
def pass_data1(x, y):
    print(type(x), type(y))
    return {"msg": x, "ans": x + y}


@api.get("/api/pass_data2/{x}/{y}")
def pass_data2(x, y):
    print(type(x), type(y))
    return {"msg": x, "ans": x + y}

@api.get("/api/pass_data3")
def pass_data3(x:int, y: int):
    ans = x + y
    return {"x": x, "y":y, "ans": ans}

@api.get("/api/pass_data4")
def pass_data4(x:int, y: int):
    try:
        ans = x / y
    except ZeroDivisionError :
        return {"Error": "Divide by zero"}
    return {"x": x, "y":y, "ans": ans}

@api.get("/api/pass_data5")
def pass_data5(x:int, y: int):
    try:
        ans = x / y
    except ZeroDivisionError :
        return fastapi.Response(content='{"Error": "Divide by zero"}',
                                status_code=400)
    return {"x": x, "y":y, "ans": ans}

@api.get("/api/pass_data6")
def pass_data6(x:int, y: int):
    try:
        ans = x / y
    except ZeroDivisionError :
        return fastapi.responses.JSONResponse(
            content={"Error": "Divide by zero"}, status_code=400)
    return {"x": x, "y":y, "ans": ans}


@api.get("/")
def index():
    body = '''
    <html> <body style='padding: 10px;'>
    <h1>Landing Page</h1>
    <div>
    API hook: <a href="api/pass_data1?x=3&y=5"> api/pass_data1?x=3&y=5 </a>
    </div>
    </body></html>
    '''

    return fastapi.responses.HTMLResponse(content=body)


