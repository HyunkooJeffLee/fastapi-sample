from typing import Protocol


class Greeter(Protocol):
    async def greet(self, name: str) -> str: ...


class SimpleGreeter:
    async def greet(self, name: str) -> str:
        return f"Hello, {name}!"
