import os
from hashlib import sha1


def verify():
    assert os.path.exists("solution.txt"), "FAIL: solution.txt does not exist"

    with open("solution.txt") as file:
        solution = sha1(
            file.read().replace(" ", "").strip().lower().encode("utf-8")
        ).hexdigest()

    assert (
        solution == "6097a6f5eb9f89b72c2d98ad9a738a0636b3e68c"
    ), "FAIL: incorrect solution"

    print("SUCCESS: challenge completed.")
    return True


verify()
