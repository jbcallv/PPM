def email_report(job, univ_options):
    """
    send an email to the user when the run finishes.

    :param _ univ_options: Dict of the options used by almost all tools
    """
    # do not send email when the run is not successful
    if job.status!= "success":
        return

    # only send email to the user
    if univ_options["email"] is None:
        return

    # do not send email when the user does not want it
    if not univ_options["email"]:
        return

    # do not send email when the email is not set
    if univ_options["email_to"] is None:
        return

    # send email
    send_email(job)

