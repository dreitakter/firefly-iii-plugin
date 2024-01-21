from typing import List

from enum import Enum

from pydantic import BaseModel

class TransactionTypeEnum(str, Enum):
    withdrawal = 'withdrawal'
    deposit = 'deposit' 
    transfer = 'transfer' 
    reconciliation = 'reconciliation' 
    opening_balance = 'opening balance' 

class TransactionSplit(BaseModel):
    user : str
    transaction_journal_id : str
    type : TransactionTypeEnum
    #... hier noch fehlende Felder aufnehmen
    date: str
    order: int
    currency_id: str
    currency_code: str
    currency_symbol: str
    currency_name: str
    currency_decimal_places: int
    foreign_currency_id: str
    foreign_currency_code: str
    foreign_currency_symbol: str
    foreign_currency_decimal_places: int
    amount: str
    foreign_amount: str
    description: str
    source_id: str
    source_name: str
    source_iban: str
    source_type: str
    destination_id: str
    destination_name: str
    destination_iban: str
    destination_type: str
    budget_id: str
    budget_name: str
    category_id: str
    category_name: str
    bill_id: str
    bill_name: str
    reconciled: bool
    notes: str
    tags: List[str]
    internal_reference: str
    external_id: str
    external_url: str
    original_source: str
    recurrence_id: str
    recurrence_total: int
    recurrence_count: int
    bunq_payment_id: str
    import_hash_v2: str
    sepa_cc: str
    sepa_ct_op: str
    sepa_ct_id: str
    sepa_db: str
    sepa_country: str
    sepa_ep: str
    sepa_ci: str
    sepa_batch_id: str
    interest_date: str
    book_date: str
    process_date: str
    due_date: str
    payment_date: str
    invoice_date: str
    latitude: float
    longitude: float
    zoom_level: int
    has_attachments: bool

class Transaction(BaseModel):
    created_at : str
    updated_at : str
    user : str
    group_title : str
    transactions : List[TransactionSplit]

class ObjectLink0(BaseModel):
    rel : str
    uri : str

class ObjectLink(BaseModel):
    0 : ObjectLink0
    self : str


class TransactionRead(BaseModel):
    type : str
    id : str
    attributes : Transaction
    links : ObjectLink

class TransactionSingle(BaseModel):
    data : TransactionRead