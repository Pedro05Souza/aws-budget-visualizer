from ..utils import payload_to_budget
from errors import BudgetNotFoundError

__all__ = ["GetBudgetUsecase"]

class GetBudgetUsecase():

    def __init__(self, fetch_budget, budget_name):
        self.fetch_budget = fetch_budget
        self.budget_name = budget_name

    def get_budget(self):
        payload = self.fetch_budget(self.budget_name)

        if not payload:
            raise BudgetNotFoundError
        
        return payload_to_budget(payload)