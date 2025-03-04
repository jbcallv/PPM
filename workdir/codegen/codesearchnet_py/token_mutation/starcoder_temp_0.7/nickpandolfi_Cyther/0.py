def call(commands, *, print_result=False, raise_exception=False,
         print_commands=False):
    """
    " call a number of commands and wrangle the output how you choose
    """
    print_commands = bool(print_commands)
    print_result = bool(print_result)
    raise_exception = bool(raise_exception)
    if print_commands:
        print(commands)
    try:
        output = subprocess.check_output(commands, shell=True)
    except subprocess.CalledProcessError as err:
        output = err.output
        if raise_exception:
            raise
    if print_result:
        print(output)
    return output

