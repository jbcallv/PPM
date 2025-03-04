def query_get_comment(comID):
    """
    for all fields of a comment
    :param comID: comment id
    :return: tuple (comID, id_bibrec, id_user, body, date_creation, star_score, nb_votes_yes, nb_votes_total, title, nb_abuse_reports, round_name, restriction)
            if , found not ()
    """
    if not comID:
        return ()
    cur = conn.cursor()
    cur.execute("""select comID, id_bibrec, id_user, body, date_creation, star_score, nb_votes_yes, nb_votes_total, title, nb_abuse_reports, round_name, restriction from bibrec_comment where comID=%s""", (comID,))
    res = cur.fetchall()
    if res:
        return res[0]
    return ()


