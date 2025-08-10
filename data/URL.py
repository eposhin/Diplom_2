
BASE_URL = "https://stellarburgers.nomoreparties.site/api"

ENDPOINTS = {
    "register_user": f"{BASE_URL}/auth/register",
    "login": f"{BASE_URL}/auth/login",
    "logout": f"{BASE_URL}/auth/logout",
    "token": f"{BASE_URL}/auth/token",
    "user": f"{BASE_URL}/auth/user",
    "orders": f"{BASE_URL}/orders"
}