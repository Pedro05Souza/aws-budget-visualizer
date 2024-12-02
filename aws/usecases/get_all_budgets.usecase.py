from Entities import Budget
from typing import List
from utils import payload_to_budget

class GetAllBudgetsUseCase():

    def __init__(self, budget_fetcher) -> None:
        self.budget_fetcher = budget_fetcher

    def get_all_budgets(self) -> List[Budget]:
        payload = self.budget_fetcher()

        budgets = []

        for budget_data in payload:

            budget = payload_to_budget(budget_data)
            budgets.append(budget)

        return budgets