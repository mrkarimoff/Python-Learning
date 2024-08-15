# Closure is a function having access to the scope of its parent
# function after the parent function has returned
from typing import Callable


def parent_function(person: str) -> Callable[[], None]:
    coins: int = 3

    def play_game() -> None:
        nonlocal coins
        coins -= 1

        if coins > 1:
            print(f"\n{person} has {coins} coins.")
        elif coins == 1:
            print(f"\n{person} has {coins} coin.")
        else:
            print(f"\n{person} is out of coins!")

    return play_game


james: Callable[[], None] = parent_function("James")
jenny: Callable[[], None] = parent_function("Jenny")

james()
james()

jenny()
