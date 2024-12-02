from aws import get_budgets, budget_formatted


def main():
    response = get_budgets()
    print(budget_formatted(response))


if __name__ == "__main__":
    main()
