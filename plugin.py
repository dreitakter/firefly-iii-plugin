from fastapi import FastAPI, Request

# FastAPI app
app = FastAPI()

@app.post("/")
async def webhook_handler(request: Request):
    print(f"webhook")
    # handle events
    payload = await request.json()
    print(payload)
    event_type = request.headers.get("X-Github-Event")
    print(request.headers._list)