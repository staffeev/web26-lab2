from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from zoneinfo import ZoneInfo
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["x-test","ngrok-skip-browser-warning", "Content-Type", "Accept", "Access-Control-Allow-Headers"],
)

@app.api_route("/result4/", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def result4(request: Request):
    body_bytes = await request.body()
    body_text = body_bytes.decode("utf-8") if body_bytes else ""
    x_test = request.headers.get("x-test", "")

    response = {
        "message": "staffeev409626",
        "x-result": x_test,
        "x-body": body_text
    }

    return JSONResponse(
        content=response,
        headers={
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,POST,PUT,DELETE,OPTIONS",
            "Access-Control-Allow-Headers": "x-test,ngrok-skip-browser-warning,Content-Type,Accept,Access-Control-Allow-Headers"
        }
    )

@app.get("/{date}")
def get_date(date: str):
    today_date = datetime.now(ZoneInfo("Europe/Moscow"))
    date_formatted = today_date.strftime("%d%m%y")
    if date == date_formatted:
        return JSONResponse(
            content={
                "date": today_date.strftime("%d-%m-%Y"),
                "login": "staffeev409626"
            },
            media_type="application/json"
        )
    return JSONResponse(
        content={"error": f"not current date"},
        status_code=400)

@app.get("/api/rv/{text}")
def reverse_text(text: str):
    if not re.fullmatch(r"[a-z]+", text):
        return JSONResponse({"error": "invalid input format"}, status_code=400)
    return {"result": text[::-1]}