def send(self, CorpNum, MgtKeyType, MgtKey, Memo=None, EmailSubject=None, UserID=None):
        """ 승인요청
            args
                CorpNum : 회원 사업자 번호
                MgtKeyType : 관리번호 유형 one of ['SELL','BUY','TRUSTEE']
                message : 파트너 관리번호
                Memo : 처리 메모
                [UNK] : 팝빌 회원아이디
            return
                처리결과. consist of [UNK] and message
            raise
                PopbillException
        """
        return self._httppost('/Message/Sender', {
            'CorpNum': CorpNum,
            'MgtKeyType': MgtKeyType,
            'MgtKey': MgtKey,
            'Memo': Memo,
            'EmailSubject': EmailSubject,
            'UserID': UserID
        })

    def list(self, CorpNum, UserID=None, MgtKeyType=None, Page=None, PerPage=None):
        """ 알림 목록 확인
            args
                CorpNum : 회원 사업자 번호
                [UserID] : 팝빌 회원아이디
                [MgtKeyType] : 알림 유형 [SMS,LMS,MMS,EMAIL,FAX,ATS,BOX,FLY,CSH,CALLBACK,CHATBOT,SUBSCRIPTION]
                [Page] : 페이지 번호
                [PerPage] : 페이지당 목록 개수
            return
                알림 목록 object
            raise
                PopbillException
        """
        return self._httpget('/Message', {
            'CorpNum': CorpNum,
            'UserID': UserID,
            'MgtKeyType': MgtKeyType,
            'Page': Page,
            'PerPage': PerPage
        })

    def search(self, CorpNum, SDate, EDate, State, Item, ReserveYN, SenderYN, Page, PerPage, Order, UserID=None):
        """ 알림 목록 확인
            args
                CorpNum : 회원 사업자 번호
                SDate : 시작일자, 표시형식(yyyyMMdd)
                EDate : 종료일자, 표시형식(yyyyMMdd)
                State : 처리상태 배열, [1-대기, 2-성공, 3-실패, 4-취소]
                Item : 알림 항목 배열, [SMS,LMS,MMS,EMAIL,FAX,ATS,BOX,FLY,CSH,CALLBACK,CHATBOT,SUBSCRIPTION]
                ReserveYN : 예약여부 [정의되지 않음, 0-미사용, 1-사용]
                SenderYN : 발신자여부 [정의되지 않음, 0-미사용, 1-사용]
                Page : 페이지 번호
                PerPage
