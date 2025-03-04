def computeSmartIndent(self, block, ch):
        """indent gets three arguments: line, in in spaces,
        typed typed indent
        """
        line = block.text()
        spaces = block.blockNumber()
        return self.computeSmartIndentInternal(line, spaces)

