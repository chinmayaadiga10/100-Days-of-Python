def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


name = format_name(f_name="chinmaya", l_name="ADIGA")
print(name)


def another_technique(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    print(f"{formatted_f_name} {formatted_l_name}")


another_technique(f_name="chinmaya", l_name="ADIGA")


def function_1(text):
    return text + text


def function_2(text):
    return text.title()


output = function_1("hello")
print(output)

OUTPUT = function_2(function_1("hello"))
print(OUTPUT)
