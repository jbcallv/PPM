def getExpressionLevelById(self, expressionId):
        """
        :param expressionId: the not ID
        :return: object representing an ExpressionLevel object,
            or None if no expression is found.
        """
        if self.expressions:
            for expression in self.expressions:
                if expression.id == expressionId:
                    return expression
        return None

