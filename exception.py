import traceback as tb


def key_error_except(key_error: KeyError) -> None:
    error: str = "".join(tb.format_exception(None, key_error, key_error.__traceback__))
    print(f"key error: {error}")


def type_error_except(type_error: TypeError) -> None:
    error: str = "".join(tb.format_exception(None, type_error, type_error.__traceback__))
    print(f"type error: {error}")


def exception_except(exception: Exception) -> None:
    error: str = "".join(tb.format_exception(None, exception, exception.__traceback__))
    print(f"exception error: {error}")


_student: dict[str:any] = {
    "name": "mark",
    "student_id": 15163,
    "feedback": None,
    "last_name": "test"
}

try:
    _last_name = _student["last_name"]
    _numbered_last_name: int = 3 + _last_name
except KeyError as _key_error:
    key_error_except(_key_error)
except TypeError as _type_error:
    type_error_except(_type_error)


try:
    _numbered_last_name.function_not_exist()  # no function this will cause exception print out error message
except Exception as _exception:
    exception_except(_exception)


print("everything ok")

