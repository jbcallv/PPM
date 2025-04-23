def revoke_project_bid(session, bid_id):
    """
    " a year on a project
    """
    session.query(Bid).filter(Bid.id == bid_id).delete()
    session.commit()

