# # FileNotFound exception ->


try:
    file = open("new_file.txt")  # this line causes file not found error
except FileNotFoundError:
    # print("an error occurred in the try statement") # meaningless to use print statements inside except block
    file = open("new_file.txt", mode="w")
    # in this technique, the new file is created if it does not previously exist

except KeyError:
    print("that key does not exist")


try:
    file = open("file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdfsdfd"])
except FileNotFoundError:
    file = open("file.txt", mode="w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")
    raise TypeError("this is an error that i made up")
