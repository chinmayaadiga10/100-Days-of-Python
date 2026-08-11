# Understanding the usage of type hints in python ->
# type hints -> relatively new feature, prevents problems caused by dynamic typing

age: int
name: str
height: float
is_human: bool


def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


print(police_check(18))

if police_check(19):
    print("you can go")
else:
    print("pay fine")

# now, at some point after writing 1000's of lines of code, we can mistake the input type and pass police_check("twelve") -> to prevent type checking is used
# the -> arrow mark specifies the return data type that is expected by the function
# at some point if i forget the return type and return("some string") -> gives warning
