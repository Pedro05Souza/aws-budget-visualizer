from Entities import Budget

__all__ = ['payload_to_budget']

def payload_to_budget(payload: dict) -> Budget:
    budget_info = payload['Budget']

    name = budget_info['BudgetName']
    threshold = budget_info['BudgetLimit']['Amount']
    currency = budget_info['BudgetLimit']['Unit']
    expense = budget_info['CalculatedSpend']['ActualSpend']['Amount']

    return Budget(name, currency, expense, threshold)