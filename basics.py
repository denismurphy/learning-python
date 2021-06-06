# type hints use them, default to 0
def add_number(a_pram: int = 0, b_pram: int = 0) -> int:
    return a_pram + b_pram


_new_number: int = add_number(4, 6)
print(f"new number is {_new_number}")

_im_a_int: int = 42
print(f"int value is {_im_a_int}")

_im_a_float: float = 4.333
print(f"float value is {_im_a_float}")

_is_it_int: bool = int(_im_a_float) == 4
print(f"is it a int? {_is_it_int}")

_is_it_float: bool = float(_im_a_int) == 42.0
print(f"is it a float? {_is_it_float}")

print("Nice to meet you {0}. I am {1}".format("Denis", "Computer"))

_really: bool = True

if _really:
    print("really is True!")
else:
    print("really is False")

if _really and False:
    print("they both have to be True")
else:
    print("the second clause was False")

_a: int = 1
_b: int = 2
_is_it: str = "bigger" if _a > _b else "smaller"

print(f"is it {_is_it}")

_student_names: list[str] = ["mark", "test", "computer"]

print(_student_names[0])

print(_student_names[2])

_student_names.append("homer")

if "mark" in _student_names:
    print("mark in list")
else:
    print("mark isn't in list")

print(len(_student_names))

_everyone_but_mark: list[str] = _student_names[1:]  # slice remove mark from list

_list_of_computer: list[str] = _everyone_but_mark[1:-1]

del _student_names[1]

print(len(_student_names))

print(_everyone_but_mark)

print(_list_of_computer)

print("Normal for loop")
for name in _student_names:
    print(name)

print("index for loop")
for index in range(len(_student_names)):
    print(_student_names[index])

for name in _student_names:
    if name == "computer":
        print("Found Computer!")
        break
    print(f"Not computer, it's {name}")

_x: int = 10

while _x < 20:
    print(f"count at {_x}")
    _x += 1

_students: dict[str:str] = {
    "first number": 20,
    "second number": 40,
    "number": "test"
}

_all_students: list[dict] = [{
    "name": "test",
    "james": "two"
}, {
    "lastname": "james"
}]

# guarded check if "number" exist
if _students.get("number", None) is not None:
    print(f"Number is not null it value is: {_students['number']}")

print(_all_students[0]["name"])

print(_all_students[0].get("james"))

