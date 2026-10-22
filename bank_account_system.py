
"""Bank account management module."""

import hashlib
import hmac
import json
import secrets
from pathlib import Path

account_data = {}


def create_account(acc_id, name, initial_deposit=0, transactions=None):
    """Create a bank account with an initial deposit."""
    if acc_id in account_data or initial_deposit < 0:
        return False

    if transactions is None:
        transactions = []

    account_data[acc_id] = {
        "name": name,
        "balance": initial_deposit,
        "transactions": transactions.copy(),
    }
    account_data[acc_id]["transactions"].append(
        f"Created {acc_id} with initial balance {initial_deposit}"
    )
    return True


def deposit(acc_id, amount):
    """Deposit a positive amount into an existing account."""
    account = account_data.get(acc_id)
    if account is None or amount <= 0:
        return False

    account["balance"] += amount
    account["transactions"].append(f"Deposit: {amount}")
    return True


def withdraw(acc_id, amount):
    """Withdraw a positive amount if sufficient funds are available."""
    account = account_data.get(acc_id)
    if account is None or amount <= 0:
        return False

    if account["balance"] < amount:
        return False

    account["balance"] -= amount
    account["transactions"].append(f"Withdrawal: {amount}")
    return True


def compute_bonus(acc_id, rate=0.05):
    """Calculate a bonus using a validated numeric rate."""
    account = account_data.get(acc_id)
    if account is None:
        raise ValueError("Account does not exist.")

    if not isinstance(rate, (int, float)) or isinstance(rate, bool):
        raise ValueError("Rate must be numeric.")

    if not 0 <= rate <= 1:
        raise ValueError("Rate must be between 0 and 1.")

    return account["balance"] * rate


def get_hash(pin, salt=None):
    """Return a salted PBKDF2 hash for a PIN."""
    if not isinstance(pin, str) or not pin:
        raise ValueError("PIN must be a non-empty string.")

    if salt is None:
        salt_bytes = secrets.token_bytes(16)
    else:
        salt_bytes = bytes.fromhex(salt)
    digest = hashlib.pbkdf2_hmac(
        "sha256", pin.encode("utf-8"), salt_bytes, 200_000
    )
    return f"{salt_bytes.hex()}${digest.hex()}"


def verify_pin(pin, stored_hash):
    """Verify a PIN against its salted hash."""
    try:
        salt, expected = stored_hash.split("$", maxsplit=1)
        actual = get_hash(pin, salt).split("$", maxsplit=1)[1]
        return hmac.compare_digest(actual, expected)
    except (ValueError, TypeError):
        return False


def generate_temp_pin():
    """Generate a cryptographically secure four-digit PIN."""
    return str(secrets.randbelow(9000) + 1000)


def backup_data(filename="backup.json"):
    """Save account data as JSON."""
    with Path(filename).open("w", encoding="utf-8") as backup_file:
        json.dump(account_data, backup_file, indent=4)
    print(f"Backup complete: {filename}")


def main():
    """Run a demonstration of account operations."""
    create_account("A01", "Alice", 1000)
    deposit("A01", 500)
    withdraw("A01", 200)

    print("Bonus:", compute_bonus("A01"))
    print("PIN Hash:", get_hash("1234"))
    print("PIN verified:", verify_pin("1234", get_hash("1234")))
    print("Temp PIN:", generate_temp_pin())
    backup_data()


if __name__ == "__main__":
    main()
