def getUnitCost(self, CorpNum):
        """ 팩스 전송 단가 확인
            args
                CorpNum : to 사업자번호
            return
                " [UNK] by float
            raise
                PopbillException
        """
        return self._httpget('/FAX/UnitCost', CorpNum)

