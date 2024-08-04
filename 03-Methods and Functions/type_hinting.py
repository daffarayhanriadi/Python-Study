name: str = "Daffa"
age: int = 22
value: float = 80.5
condition: bool = False
complex_value: complex = 20j
studying_list: list[str] = ["mathematic", "physic", "chemistry"]
tuple_example: tuple[str] = ("english", "Indonesia")
dict_example: dict[str, int] = {"size": 12, "length": 30.2}

def count(num1: int, num2: int) -> int:
    return num1 + num2

def call(name: str) -> None:
    print(f"Hello {name}")
    
print(call("daffa"))

my_name: str = "daffa rayhan"

print(count(5, 2))