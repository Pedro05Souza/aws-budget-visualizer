from ..Entities import Budget
from typing import List
from ..utils import payload_to_budget

__all__ = ["GetAllBudgetsUseCase"]

class GetAllBudgetsUseCase():

    def __init__(self, fetch_all_budgets) -> None:
        self.fetch_all_budgets = fetch_all_budgets

    def get_all_budgets(self) -> List[Budget]:
        payload = self.fetch_all_budgets()

        budgets = []

        for budget_data in payload:

            budget = payload_to_budget(budget_data)
            budgets.append(budget)
        return budgets