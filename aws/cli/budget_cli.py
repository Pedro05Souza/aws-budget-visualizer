import click
from aws.usecases import GetAllBudgetsUseCase, GetBudgetUsecase
from aws import BudgetRepository

__all__ = ["BudgetManagerCLI"]

class BudgetManagerCLI():
    def __init__(self):
        pass

    @click.group()
    def cli():
        pass

    @cli.command()
    def get_all():
        budget_repository = BudgetRepository()
        get_all_budgets_usecase = GetAllBudgetsUseCase(budget_repository.get_all_budgets)
        budgets = get_all_budgets_usecase.get_all_budgets()

        for budget in budgets:
            click.echo(budget)

        click.echo(f"Total Budgets: {len(budgets)}")

    @cli.command()
    @click.argument('budget_name')
    def get_one(budget_name):
        budget_repository = BudgetRepository()
        get_budget_usecase = GetBudgetUsecase(budget_repository.get_budget, budget_name)
        budget = get_budget_usecase.get_budget()

        click.echo(budget)