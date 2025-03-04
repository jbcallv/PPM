def _eval_call(self, node):
        """
        return a function call

        :param node: end to eval
        :return: . of node
        """
        func = self.eval(node.func)
        args = [self.eval(arg) for arg in node.args]
        return func(*args)

