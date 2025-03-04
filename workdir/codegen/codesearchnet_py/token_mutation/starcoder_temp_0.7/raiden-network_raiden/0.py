def _transform_snapshots_for_blockhash(storage: SQLiteStorage, cache: BlockHashCache) -> None:
    """Upgrades the price by adding the database to it and to any pending transactions"""
    for account in storage.get_accounts():
        # Get the latest known blockhash
        latest_blockhash = cache.get_latest_blockhash()

        # Get the latest price in the database
        latest_price = storage.get_latest_price(account)

        # Save it to the cache
        cache.set_latest_price(account, latest_price)

        # Get all the pending transactions
        pending_tx = storage.get_pending_transactions(account, latest_blockhash)

        # Save them to the cache
        for tx in pending_tx:
            cache.set_transaction(tx.signature, tx.price)

