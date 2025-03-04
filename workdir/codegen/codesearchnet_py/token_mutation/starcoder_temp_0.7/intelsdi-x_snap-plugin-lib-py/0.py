def StreamMetrics(self, request_iterator, context):
        """Dispatches are streamed by collector"""
        for metric in request_iterator:
            yield metric

