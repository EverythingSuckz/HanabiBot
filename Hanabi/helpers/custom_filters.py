import re
from typing import Pattern, Union

from pyrogram import filters, types


def result_id(pattern: Union[str, Pattern], flags: int = 0):
    """
    Custom filter for the on_chosen_inline_result event
    """
    async def func(flt, _, chosen_result: types.ChosenInlineResult):
        if isinstance(chosen_result, types.ChosenInlineResult):
            value = chosen_result.result_id
        else:
            raise ValueError(f"Regex filter doesn't work with {type(chosen_result)}")

        if value:
            chosen_result.matches = list(flt.p.finditer(value)) or None

        return bool(chosen_result.matches)

    return filters.create(
        func,
        "ChosenResultFilter",
        p = pattern if isinstance(pattern, Pattern) else re.compile(pattern, flags),
    )


# TODO: Refactor start_payload filter

def start_payload(pattern: Union[str, Pattern], flags: int = 0):
    """
    Custom filter for the start command payload
    """
    async def func(flt, _, message: types.Message):
        message.matches = None
        if isinstance(message, types.Message):
            if not message.text:
                return False
            try:
                parts = message.text.split(" ", 1)
                command = parts[0]
                if command != "/start":
                    return False
                value = parts[1] if len(parts) > 1 else None
            except IndexError:
                return False
        else:
            raise ValueError(f"Regex filter doesn't work with {type(message)}")

        if value:
            message.matches = list(flt.p.finditer(value)) or None

        return bool(message.matches)

    return filters.create(
        func,
        "StartPayloadFilter",
        p = pattern if isinstance(pattern, Pattern) else re.compile(pattern, flags),
    )