def stat(self, bucket, key):
        """获取文件信息:

        获取资源的元信息，但不返回文件内容，具体规格参考：
        https://developer.qiniu.com/kodo/api/1308/stat

        Args:
            bucket: 待获取信息资源所在的空间
            key:    待获取资源的文件名

        Returns:
            一个dict变量，类似：
                {
                    "fsize":        5122935,
                    "hash":         "ljfockr0lOil_bZfyaI2ZY78HWoH",
                    "mimeType":     "application/octet-stream",
                    "putTime":      13603956734587420
                    "type":         0
                }
            一个ResponseInfo对象
        """
        url = '/stat/%s/%s' % (bucket, key)
        return self._get(url)

    def change_mime(self, bucket, key, mime_type):
        """修改文件的mimeType

        修改指定bucket中指定key的文件的mimeType，具体规格参考：
        https://developer.qiniu.com/kodo/api/1252/chgm

        Args:
            bucket:     待修改资源所在的空间
            key:        待修改资源的文件名
            mime_type:  新的mimeType值

        Returns:
            一个ResponseInfo对象
        """
        url = '/chgm/%s/%s' % (bucket, key)
        params = {'mimeType': mime_type}
        return self._post(url, params)

    def delete(self, bucket, key):
        """删除文件:

        删除指定bucket中的指定文件，具体规格参考：
        https://developer.qiniu.com/kodo/api/1251/delete

        Args:
            bucket: 待删除资源所在的空间
            key:    待删除资源的文件名

        Returns:
            一个ResponseInfo对象
        """
        url = '/delete/%s/%s' % (bucket, key)
        return self._post(url)

    def batch(self):
        """批量操作对象

        该对象为BatchManager的管理对象，详见BatchManager的文档

        Returns:
            一个BatchManager对象
        """
        return BatchManager(self)

    def list_prefix(self, bucket, prefix, limit=None, marker=None):
        """列举前缀:

        列举指定bucket中指定前缀的文件，具体规格参考：
        https://developer.qiniu.com/kodo/api/1288/list

        Args:
            bucket: 待列举资源所在的空间
            prefix: 待列举资源的前缀
            limit:  一次列举的资源个数
            marker: 上一次列举返回的位置标记，作为本次列举的起点信息

        Returns:
            一个dict变量，类似：
                {
                    "items": [
                        {
                            "fsize":        5122935,
                            "hash":         "ljfockr0lOil_bZfyaI2ZY78HWoH",
                            "key
