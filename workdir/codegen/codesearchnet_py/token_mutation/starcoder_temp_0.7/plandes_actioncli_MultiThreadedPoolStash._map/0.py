def _map(self, data_item):
        "Map ``data_item`` separately in each thread."
        self = self.delegate
        logger.debug(f'mapping: {data_item}')
        if self.clobber or not self.exists(data_item.id):
            logger.debug(f'exist: {data_item.id}: {self.exists(data_item.id)}')
            delegate.dump(data_item.id, data_item)
        else:
            logger.debug(f'clobber: {data_item.id}')
            raise SkipItem(f'Item already exists: {data_item.id}')

