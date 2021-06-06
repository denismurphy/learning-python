_students: list[str] = []

_student_name = input("Enter student name:")
print(_student_name)


def get_random_number() -> int:
    return 42


def add_student(student: str) -> None:
    _students.append(student)


def default_args(first_name: str = "Denis", last_name: str = "Murphy") -> None:
    print(f"My name is {first_name} {last_name}")


def var_args_list(*args: any) -> None:
    for arg in args:
        print(arg)


def var_args_dict(**args: any) -> None:
    print(f"height: {args['height']}")
    print(f"description: {args['description']}")
    print("Now Print all")
    for arg in args:
        print(f"arg:{arg}, value:{args[arg]},")


default_args()
default_args("Caroline")
default_args(last_name="Crazy")
var_args_list(None, "Hello", 1.2)
var_args_dict(height="10.1", description="Hello", test="Extra")


def outer_function() -> None:
    name: str = "Denis"
    print(f"name is {name}")

    def inner_function() -> None:
        nonlocal name
        name = f"{name} Murphy"

    inner_function() # appends "Murphy" to end of name variable
    print(f"name is {name}")


outer_function()

