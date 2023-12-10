import hashlib

GRAVATAR_BASE_URL = "https://www.gravatar.com/avatar/"


def gravatar_generator(email):
    size = 40

    gravatar_url = f"{GRAVATAR_BASE_URL}{hashlib.md5(email.lower()).hexdigest()}?s={size}"
    return gravatar_url
