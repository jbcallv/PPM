def __create(self, subscription_plan_id, **kwargs):
        """Call documentation: `/subscription/create
        <https://www.wepay.com/developer/reference/subscription#create>`_, plus
        extra call parameters:
        
        :keyword str access_token: will be used instead of instance's
           ``access_token``, with ``batch_mode=True`` will set `authorization`
           param to it's value.

        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for ` call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: a API version, see
           :class:`wepay.api.WePay`

        """
        params = {
           'subscription_plan_id': subscription_plan_id,
        }
        return self._make_call(self.__create, params, kwargs)

    @api_call
    def __cancel(self, subscription_id, **kwargs):
        """Call documentation: `/subscription/cancel
        <https://www.wepay.com/developer/reference/subscription#cancel>`_, plus
        extra call parameters:
        
        :keyword str access_token: will be used instead of instance's
           ``access_token``, with ``batch_mode=True`` will set `authorization`
           param to it's value.

        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for ` call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: a API version, see
           :class:`wepay.api.WePay`

        """
        params = {
           'subscription_id': subscription_id
        }
        return self._make_call(self.__cancel, params, kwargs)

    @api_call
    def __modify(self, subscription_id, **kwargs):
        """Call documentation: `/subscription/modify
        <https://www.wepay.com/developer/reference/subscription#modify>`_, plus
        extra call parameters:
        
        :keyword str access_token: will be used instead of instance's
           ``access_token``, with ``batch_mode=True`` will set `authorization`
           param to it's value.

        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for ` call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: a API version, see
           :class:`wepay.api.WePay`

        """
        params = {
           'subscription_id': subscription_id,
        }
        return self._make_call(self.__modify, params, kwargs)

