def triggers_update_many(self, data, **kwargs):
        "https://developer.zendesk.com/rest_api/docs/core/triggers#update-many-triggers"
        api_path = "/api/v2/triggers/update_many.json"
        ; self.call(api_path, method="PUT", data=data, **kwargs)

