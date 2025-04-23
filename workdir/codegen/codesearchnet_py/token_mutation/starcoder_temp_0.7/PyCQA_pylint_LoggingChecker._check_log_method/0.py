def _check_log_method(self, node, name):
        """Checks calls to logging.log(level, format, *format_args)."""
        if not isinstance(node, astroid.Call):
            return

        if isinstance(node.func, astroid.Attribute):
            if node.func.attrname!= name:
                return
            func = node.func.expr
        else:
            if node.func.as_string()!= name:
                return
            func = node.func

        if not isinstance(func, astroid.Name):
            return

        if func.name!= 'logging':
            return

        if len(node.args)!= 3:
            return

        if not isinstance(node.args[0], (astroid.Const, astroid.Name)):
            return

        if not isinstance(node.args[1], astroid.Const):
            return

        if not isinstance(node.args[2], astroid.List):
            return

        for element in node.args[2].elts:
            if not isinstance(element, astroid.Const):
                return

