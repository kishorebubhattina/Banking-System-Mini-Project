from datetime import datetime


class Account:
    """Represents one bank account."""

    def __init__(
        self,
        account_number,
        name,
        phone,
        pin,
        balance=0.0,
        transactions=None,
    ):
        self.account_number = account_number
        self.name = name
        self.phone = phone
        self.pin = pin
        self.balance = float(balance)
        self.transactions = transactions or []

    def add_transaction(self, transaction_type, amount, description, timestamp=None):
        transaction = {
            "timestamp": timestamp or datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": transaction_type,
            "amount": float(amount),
            "description": description,
        }
        self.transactions.append(transaction)

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "phone": self.phone,
            "pin": self.pin,
            "balance": self.balance,
            "transactions": self.transactions,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            account_number=data["account_number"],
            name=data["name"],
            phone=data["phone"],
            pin=data["pin"],
            balance=data.get("balance", 0.0),
            transactions=data.get("transactions", []),
        )
