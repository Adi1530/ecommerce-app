import requests
from auth import auth_headers

API = "http://127.0.0.1:8000"

def register(email, password):
    return requests.post(
        f"{API}/auth/register",
        json={"email": email, "password": password}
    )

def login(email, password):
    return requests.post(
        f"{API}/auth/login",
        json={"email": email, "password": password}
    )

def get_products():
    return requests.get(
        f"{API}/products",
        headers=auth_headers()
    )

def add_to_cart(product_id: int):
    return requests.post(
        f"{API}/cart",
        json={"product_id": product_id},
        headers=auth_headers()
    )

def checkout(items, address, total_amount):
    """
    items: list of {"product_id": id, "quantity": qty, "price": price}
    """
    return requests.post(
        f"{API}/orders/checkout",
        json={
            "items": items,
            "address": address,
            "total_amount": total_amount
        },
        headers=auth_headers()
    )

def get_user_orders():
    return requests.get(
        f"{API}/orders/my-orders",
        headers=auth_headers()
    )

def get_all_orders():
    return requests.get(
        f"{API}/orders/all-orders",
        headers=auth_headers()
    )

