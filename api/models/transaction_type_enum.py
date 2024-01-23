from enum import Enum

class TransactionTypeEnum(str, Enum):
    withdrawal = 'withdrawal'
    deposit = 'deposit' 
    transfer = 'transfer' 
    reconciliation = 'reconciliation' 
    opening_balance = 'opening balance' 