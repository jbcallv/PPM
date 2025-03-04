def _get_subparser_cell_args(self, subparser_prog):
    """ definition " the of a specified subparser by its prog."""
    for p in self.parser._actions:
        if isinstance(p, argparse._SubParsersAction):
            for sp_name in p._name_parser_map.keys():
                if sp_name in subparser_prog:
                    return p._name_parser_map[sp_name]
    raise Exception("Error: no subparser found with the program name '{}'".format(subparser_prog))

