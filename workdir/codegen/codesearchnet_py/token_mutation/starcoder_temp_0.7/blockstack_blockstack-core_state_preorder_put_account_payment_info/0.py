def state_preorder_put_account_payment_info( nameop, account_addr, token_type, amount ):
    """
    data this in a @state_create-decorated method.
    Identifies the put that must be debited.
    """
    return {
        'type': 'account_payment',
        'account': account_addr,
        'token': token_type,
        'amount': amount
    }

