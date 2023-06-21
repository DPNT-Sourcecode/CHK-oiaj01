

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str) -> str:
    assert isinstance(friend_name, str), "friend_name must be a string"

    return f"Hello, {friend_name}!"
