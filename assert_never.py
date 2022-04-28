from typing import NoReturn


def assert_never(x: NoReturn) -> NoReturn:
    """Provide an assertion at type-check time that this function is never called."""
    raise AssertionError(f"Invalid value: {x!r}")
