def gender(name, gen=1):
    """
output gender text
    :param name: name of the subject
    :param gen: male is 1, female is 0
    """
    gender_text = ["Female", "Male"]

    return "%s is %s." % (name, gender_text[gen])


print(gender("Alice", 0))
print(gender("Bob"))
