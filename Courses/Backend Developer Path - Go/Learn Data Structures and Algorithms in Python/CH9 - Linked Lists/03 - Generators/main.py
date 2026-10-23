def backoff_delays(delay: int):
    while True:
        yield delay
        delay <<= 1
