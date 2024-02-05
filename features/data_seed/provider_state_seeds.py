import os
import requests
import shared

from config import Config


def new_frontyard_session():
    session = requests.Session()
    fy_url = Config.FY_URL
    # TODO: we will need to make this block more global considering api URLs can have different hosts
    # eg. HTTPConnectionPool(host='frontyard.tails-nonprod.com', port=80)
    if shared.browser in ("chrome", "iphone", "android"):
        fy_url = Config.FY_HYPER_URL
        # Define the proxies and assign to the session
        proxy = {
            'http': os.getenv('LT_PROXY_HOST') + ':' + os.getenv('LT_PROXY_PORT'),
            'https': os.getenv('LT_PROXY_HOST') + ':' + os.getenv('LT_PROXY_PORT'),
        }
        session.proxies = proxy

    login_url = f"{fy_url}/login"
    credentials = {
        "username": Config.FY_USERNAME,
        "password": Config.FY_PASSWORD
    }
    # Making the POST request using session
    session.request('POST', login_url, data=credentials, verify=False)

    return session, fy_url


def get_subscription_id(customer_id):
    session, fy_url = new_frontyard_session()
    url = fy_url + "/api/v1/subscriptions"
    querystring = {"customer_id": customer_id}
    response = session.get(url, auth=(Config.FY_USERNAME, Config.FY_PASSWORD), params=querystring)
    print(response.json()["data"][0]["subscription_id"])
    return response.json()["data"][0]["subscription_id"]


def set_quote_for_subscription(customer_id):
    session, fy_url = new_frontyard_session()
    url = fy_url + "/_provider_state"
    payload = [
        {
            "predicate": "Set subscription prices",
            "parameters": {"subscription_id": get_subscription_id(customer_id)}
        }
    ]
    response = session.post(url, json=payload)
    return response


def generate_email_customer_seed(seed_profile_type, store_id):
    session, fy_url = new_frontyard_session()
    seed_url = f"{fy_url}/qa_seeds/new_customer/{seed_profile_type}/{store_id}"
    data = {'tier': 'superpremium'}
    post_response = session.post(seed_url, data=data, verify=False)
    print(post_response.text)
    email = post_response.content.decode("utf-8")
    return email
