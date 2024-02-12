import requests
from flask import jsonify

# Replace these values with your actual Zeepay API credentials
client_secret = "CcIWxNyVl3Ba5bXR7C6weToZgrLLLjrJRg956fQt"
client_id = 86
username = "internal-qa@myzeepay.com"
password = "dumbdumb123"


def get_token():
    auth_url = "https://test.digitaltermination.com/oauth/token"

    request_data = {
        "grant_type": "password",
        "client_secret": client_secret,
        "client_id": client_id,
        "username": username,
        "password": password,
    }

    response = requests.post(auth_url, json=request_data)

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        return None


def create_checkout(order_id, item_id, product, currency, order_total, description):
    token = get_token()

    if not token:
        return jsonify({"error": "Failed to authenticate"})

    base_url = "https://test.digitaltermination.com/api/v2/instntmny-local/transactions/3rd-party/checkout"
    nonce = "generate_nonce_here"  # Replace with nonce generation logic if needed

    body = {
        "amount": order_total,
        "services": "wallet",
        "currency": currency,
        "reference": f"{order_id}_{item_id}",
        "product": product,
        "callback_url": f"https://yourdomain.com/wc-api/WC_zeepay_payment_gateway/?nonce={nonce}&order_id={order_id}",
        "cancelUrl": "https://yourdomain.com/checkout",  # Update with your cancel URL
        "returnUrl": f"https://yourdomain.com/order/{order_id}",  # Update with your return URL
        "description": f"{description} - {order_id}",
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
    }

    response = requests.post(base_url, json=body, headers=headers)

    if response.status_code == 200:
        checkout_url = response.json().get("checkout-url")
        return jsonify({"code": 411, "checkout-url": checkout_url})
    else:
        return jsonify({"error": "Failed to create checkout"})
