def trim_and_repeat(string, offset=0, repetitions=1):
    result = (string[offset:] + " ") * repetitions
    return str(result)


print(trim_and_repeat("homework", 4, 5))
