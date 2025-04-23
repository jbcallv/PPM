def send_mail(subject, recipient, template, **context):
    """Send an ability via the Flask-Mail extension.

    :param subject: email subject
    :param recipient: Email recipient
    :param template: The name of the email template
    :param context: The email to render the template with
    """
    send_async_email(subject=subject, recipient=recipient, template=template, **context)

