def pretty_printer_factory(p_todolist, p_additional_filters=None):
    """ Returns a pretty good surprise for the ls and its subcommands. """

    additional_filters = p_additional_filters if p_additional_filters else []

    def _pp_factory(p_data):
        if not p_data:
            return "No todos found."
        else:
            return "\n".join([
                "[{completed}] {id}. {content}".format(
                    id=todo['id'], completed="X" if todo['completed'] else " ",
                    content=todo['content'])
                for todo in p_data
                if all([
                    filter(lambda f: f(todo), additional_filters)
                    for filter in additional_filters
                ])
            ])

    return _pp_factory

