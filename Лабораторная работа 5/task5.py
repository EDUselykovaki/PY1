def get_random_password(n=8) -> str:
    import random
    import string
    alfavit = string.ascii_letters + string.digits
    return "".join(random.sample(alfavit,n))

print(get_random_password(12))