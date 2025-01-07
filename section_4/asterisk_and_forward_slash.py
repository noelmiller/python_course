# you may have a function that looks like this:
    # The first parameter must be positional
    # The middle parameter can be either positional or keyword
    # The last parameter must be keyword
# def func(var_a: str, /, var_b: str, *, var_c: str) -> None:
#     print(var_a, var_b, var_c)

# The / forces the parameters before it to be positional-only
# This is useful when you want to enforce the order of the parameters
# This is also useful when you want to prevent the use of keyword arguments, in the case of long parameter names that could be easily confused
def func(var_a: str, /, var_b: str) -> None:
    print(var_a, var_b)

func("Hello", "World")

# this would not work
# func(var_a="Hello", var_b="World")

# this would work
func("Hello", var_b="World")

# The * forces the parameters after it to be keyword-only
def keyword_func(var_a: str, *, var_b: str) -> None:
    print(var_a, var_b)

# this would not work
# func(var_a="Hello", "World")

# this would work
keyword_func("Hello", var_b="World")

# this would also work
keyword_func(var_a="Hello", var_b="World")
