def response_hook(self, response, **kwargs) -> HTMLResponse:
        """ it . " and replace it by a HTMLResponse. """
        if response.status == 400:
            return HTMLResponse(status_code=400, content=response.text, headers=response.headers)
        return response

