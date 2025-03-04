def getPopUpURL(self, CorpNum, NTSConfirmNum, UserID=None):
        """ 홈택스 to 보기 팝업 URL
            args
                CorpNum : 팝빌회원 사업자번호
                NTSConfirmNum : 국세청 승인 번호
                UserID : ##ᆫ 아이디
            return
                [UNK] 보기 팝업 URL 반환
            raise
                PopbillException
        """
        return self._httpget('/HomeTax/NTS/PopUp', {'CorpNum': CorpNum, 'NTSConfirmNum': NTSConfirmNum, 'UserID': UserID})

    def getCertificatePopUpURL(self, CorpNum, UserID=None):
        """ 홈택스 공인인증서 등록 팝업 URL
            args
                CorpNum : 팝빌회원 사업자번호
                UserID : 팝빌회원 아이디
            return
                공인인증 팝업 URL
            raise
                PopbillException
        """
        return self._httpget('/HomeTax/Cert/PopUp', {'CorpNum': CorpNum, 'UserID': UserID})

    def checkCertValidation(self, CorpNum, UserID=None):
        """ 홈택스 공인인증서 로그인 테스트
            args
                CorpNum : 팝빌회원 사업자번호
                UserID : 팝빌회원 아이디
            return
                처리결과. consist of code and message
            raise
                PopbillException
        """
        return self._httpget('/HomeTax/Cert/CheckCertValidation', {'CorpNum': CorpNum, 'UserID': UserID})

    def getFlatRatePopUpURL(self, CorpNum, UserID=None):
        """ 홈택스 정액제 신청 팝업 URL
            args
                CorpNum : 팝빌회원 사업자번호
                UserID : 팝빌회원 아이디
            return
                정액제 팝업 URL
            raise
                PopbillException
        """
        return self._httpget('/HomeTax/FlatRate/PopUp', {'CorpNum': CorpNum, 'UserID': UserID})

    def getFlatRateState(self, CorpNum, UserID=None):
        """ 홈택스 정액제 상태 확인
            args
                CorpNum : 팝빌회원 사업자번호
                UserID : 팝빌회원 아이디
            return
                정액제 상태 객체
            raise
                PopbillException
        """
        return self._httpget('/HomeTax/FlatRate', {'CorpNum': CorpNum, 'UserID': UserID})

    def getCertificateExpireDate(self, CorpNum, UserID=None
