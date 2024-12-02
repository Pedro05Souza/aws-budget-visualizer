import boto3

__all__ = ["AWS_CLIENT"]

AWS_CLIENT = boto3.client(
    "budgets",
)
