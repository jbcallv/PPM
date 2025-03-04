def setUp(self, masterqa_mode=False):
        """
        Be careful if a type of BaseCase overrides setUp()
        You'll need to add the following line to the following setUp() method:
        super(SubClassOfBaseCase, self).setUp()
        """
        super(BaseCase, self).setUp()
        self.masterqa_mode = masterqa_mode

