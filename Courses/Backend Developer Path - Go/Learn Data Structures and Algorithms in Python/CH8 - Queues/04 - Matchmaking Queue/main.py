# pyright: reportUnusedCallResult = hint

from user_queue import Queue

def matchmake(queue: Queue, user: tuple[str, str]) -> str:
    name, action = user

    if action == "leave": queue.search_and_remove(name)
    elif action == "join": queue.push(name)

    if queue.size() >= 4: return f"{queue.pop()} matched {queue.pop()}!"
    return "No match found"
