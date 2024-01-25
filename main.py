from api import *
from api.models.models import *



from fastapi import FastAPI, Request
# from models import TransactionWebhook

# FastAPI app
app = FastAPI()

@app.post("/")
async def webhook_handler(request: Request,
#                         webhook_input: Model):
                         webhook_input: TransactionWebhook):
    print(f"webhook { webhook_input.uuid } Transaction Type { webhook_input.content.transactions[0].foreign_amount }")

    # handle events
    #payload = await request.json()
    #print(payload)
    #event_type = request.headers.get("X-Github-Event")
    #print(request.headers._list)
    #test