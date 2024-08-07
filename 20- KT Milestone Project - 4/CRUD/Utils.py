import random
import string

def random_string(panjang: int) -> str:
    """Generate Unique Primary Key"""
    return "".join(random.choice(string.ascii_letters) for i in range(panjang))