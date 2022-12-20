example = "This is Global variable"


def localVariable():
    examples = "This is Local variable"
    return examples


print(example)
print(localVariable())
