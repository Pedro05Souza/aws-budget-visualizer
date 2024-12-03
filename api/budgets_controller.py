from fastapi import APIRouter
from aws.usecases import GetAllBudgetsUseCase, GetBudgetUsecase
from aws import BudgetRepository

router = APIRouter(prefix='/budgets')

@router.get("/")
async def get_all_budgets() -> dict:
    budget_repository = BudgetRepository()
    get_all_budgets_usecase = GetAllBudgetsUseCase(budget_repository.get_all_budgets)
    budgets = get_all_budgets_usecase.get_all_budgets()

    return {"budgets": budgets}

@router.get("/{budget_name}")
async def get_budget(budget_name: str) -> dict:
    budget_repository = BudgetRepository()
    get_budget_usecase = GetBudgetUsecase(budget_repository.get_budget, budget_name)
    budget = get_budget_usecase.get_budget()

    return {"budget": budget}