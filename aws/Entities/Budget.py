from pydantic import BaseModel

__all__ = ['Budget']

class Budget (BaseModel):
    name: str
    currency: str
    current_expense: float
    threshold: float