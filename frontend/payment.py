# import dbm
import requests
from flask import jsonify, redirect
from frontend import db

# from frontend import DB_NAME
from frontend.models import Ticket

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
        "amount": 1,
        "services": "wallet",
        "currency": "GHS",
        "reference": "{{$guid}}",
        "callback_url": "https://webhook.site/4ea2e251-e3ad-4139-b662-ba9f75eefebd",
        "cancelUrl": "https://webhook.site/#!/4ea2e251-e3ad-4139-b662-ba9f75eefebd",
        "returnUrl": "https://webhook.site/#!/4ea2e251-e3ad-4139-b662-ba9f75eefebd",
        "description": "Payment for fun items bought at my enterprise whiles surfing the wonder net"
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
    }

    response = requests.post(base_url, json=body, headers=headers, allow_redirects=False)

    if response.status_code == 302:  # Redirect status code
        redirect_url = response.headers.get('Location')

        # Save ticket details to the database
        ticket = Ticket(
            order_id=order_id,
            item_id=item_id,
            product=product,
            currency=currency,
            order_total=order_total,
            description=description,
            checkout_url=redirect_url  # Save the checkout URL for reference
        )
        db.session.add(ticket)
        db.session.commit()

        # Instead of returning just JSON, return a redirect response
        return redirect(redirect_url)  # Redirect to the payment gateway UI
    else:
        return jsonify({"error": "Failed to create checkout"})


