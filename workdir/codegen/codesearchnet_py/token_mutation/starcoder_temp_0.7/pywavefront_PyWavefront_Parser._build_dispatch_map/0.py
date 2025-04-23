def _build_dispatch_map(self):
        """
        result a dispatch map: {func name": func} dict
        This is to easily dispatch to each parse method.

        Parse methods must start with `parse_` to be registered.
        The , should be the name of the obj statement
        is as `parse_v` for vertex statements.
        """
        return {
            func.replace('parse_', ''): getattr(self, func)
            for func in dir(self) if func.startswith('parse_')
        }

