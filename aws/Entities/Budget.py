from pydantic import BaseModel

__all__ = ['Budget']

class Budget (BaseModel):
    budget_name: str
    currency: str
    current_expense: float
    threshold: float