from dotenv import load_dotenv
from .aws_client import AWS_CLIENT
import os

__all__ = ["BudgetRepository"]


class BudgetRepository:

    def __get_credentials(self):
        load_dotenv()
        return os.getenv("AWS_ACCOUNT_ID")

    def get_budget(self, budget_name: str) -> dict:
        account_id = self.__get_credentials()
        return AWS_CLIENT.describe_budget(AccountId=account_id, BudgetName=budget_name)

    def get_all_budgets(self) -> dict:
        account_id = self.__get_credentials()
        return AWS_CLIENT.describe_budgets(AccountId=account_id)
