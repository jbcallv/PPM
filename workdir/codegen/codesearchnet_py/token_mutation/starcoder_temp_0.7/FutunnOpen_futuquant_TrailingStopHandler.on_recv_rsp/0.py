def on_recv_rsp(self, rsp_str):
        """数据接收回调函数"""
        print(self.session_id, "on_recv_rsp:", rsp_str)

    def on_err_rsp(self, rsp_str):
        """错误信息回调函数"""
        print(self.session_id, "on_err_rsp:", rsp_str)

    def on_order_rsp(self, rsp_str):
        """委托响应函数"""
        print(self.session_id, "on_order_rsp:", rsp_str)


