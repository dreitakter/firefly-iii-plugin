from typing import Any, List, Optional

from enum import Enum

from pydantic import BaseModel

class TransactionTypeEnum(str, Enum):
    withdrawal = 'withdrawal'
    deposit = 'deposit' 
    transfer = 'transfer' 
    reconciliation = 'reconciliation' 
    opening_balance = 'opening balance' 

class TransactionSplit(BaseModel):
    user : int
    transaction_journal_id : int
    type : TransactionTypeEnum
    date: str
    order: int
    currency_id: int
    currency_code: str
    currency_symbol: str
#    currency_name: Optional[str]
    currency_decimal_places: int
    foreign_currency_id: Optional[int]
    foreign_currency_code: Optional[str]
    foreign_currency_symbol: Optional[str]
    foreign_currency_decimal_places: Optional[int]
    amount: str
    foreign_amount: Optional[str]
    description: str
    source_id: int
    source_name: str
    source_iban: Optional[str]
    source_type: str
    destination_id: int
    destination_name: str
    destination_iban: Optional[str]
    destination_type: str
    budget_id: Optional[int]
    budget_name: Optional[str]
    category_id: Optional[str]
    category_name: Optional[str]
    bill_id: Optional[str]
    bill_name: Optional[str]
    reconciled: Optional[bool]
    notes: Optional[str]
    tags: Optional[List[str]]
    internal_reference: Optional[str]
    external_id: Optional[str]
 #   external_url: Optional[str]
    original_source: Optional[str]
    recurrence_id: Optional[str]
 #   recurrence_total: Optional[int]
 #   recurrence_count: Optional[int]
    bunq_payment_id: Optional[str]
    import_hash_v2: Optional[str]
    sepa_cc: Optional[str]
    sepa_ct_op: Optional[str]
    sepa_ct_id: Optional[str]
    sepa_db: Optional[str]
    sepa_country: Optional[str]
    sepa_ep: Optional[str]
    sepa_ci: Optional[str]
    sepa_batch_id: Optional[str]
    interest_date: Optional[str]
    book_date: Optional[str]
    process_date: Optional[str]
    due_date: Optional[str]
    payment_date: Optional[str]
    invoice_date: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    zoom_level: Optional[int]
 #   has_attachments: Optional[bool]

class Transaction(BaseModel):
    id: int
    created_at : str
    updated_at : str
    user : int
    group_title : Optional[str]
    transactions : List[TransactionSplit]

class ObjectLink0(BaseModel):
    rel : str
    uri : str

class ObjectLink(BaseModel):
    #0 : ObjectLink0
    self : str


class TransactionRead(BaseModel):
    type : str
    id : str
    attributes : Transaction
    links : ObjectLink

class TransactionSingle(BaseModel):
    data : TransactionRead

class TransactionWebhook(BaseModel):
    uuid: str
    user_id: int
    trigger: str
    response: str
    url: str
    version: str
    content: Transaction