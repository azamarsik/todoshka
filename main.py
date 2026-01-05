from fastapi import FastAPI
from routers import tasks

app = FastAPI()
app.include_router(tasks.router, prefix="/api/v1")



app = FastAPI(title="todoshka", version = "0.1.0")


@app.get("/ping")
def ping():
    return Response(content = json.dumps({"ping":"pong!"}), status_code = HTTPStatus.OK)


@app.get("/docs", response_class=HTMLResponse)
def docs():
    html_content = """
    <html>
    <body>
        <p>"Даров!"</p>
    </body>
    </html>
    """
    return Response(content = html_content, status_code = HTTPStatus.OK)
