from fastapi import FastAPI, Request
from models import Transaction

# FastAPI app
app = FastAPI()

@app.post("/")
async def webhook_handler(request: Request,
                          webhook_input: Transaction):
    print(f"webhook {Transaction.transactions[0].transaction_journal_id}")

    # handle events
    payload = await request.json()
    print(payload)
    event_type = request.headers.get("X-Github-Event")
    print(request.headers._list)
    #test