from fastapi import FastAPI, Response
import json
from http import HTTPStatus
from fastapi.responses import HTMLResponse


app = FastAPI(title="todoshka", version = "0.1.0")

@app.get("/ping")
def ping():
    return Response(content = json.dumps({"ping":"pong!"}), status_code = HTTPStatus.OK)
