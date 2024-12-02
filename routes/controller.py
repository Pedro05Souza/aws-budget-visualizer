from .router_app import app
from aws import get_budgets

@app.get("/")
def get_all_budgets() -> str:
    return get_budgets()