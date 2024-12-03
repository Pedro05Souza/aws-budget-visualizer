from .Entities import Budget

__all__ = ["payload_to_budget"]


def payload_to_budget(payload: dict) -> Budget:

    name = payload["BudgetName"]
    threshold = payload["BudgetLimit"]["Amount"]
    currency = payload["BudgetLimit"]["Unit"]
    expense = payload["CalculatedSpend"]["ActualSpend"]["Amount"]
    forecasted_expense = payload["CalculatedSpend"]["ForecastedSpend"]["Amount"]

    return Budget(name=name, currency=currency, current_expense=expense, threshold=threshold, forecasted_expense=forecasted_expense)
