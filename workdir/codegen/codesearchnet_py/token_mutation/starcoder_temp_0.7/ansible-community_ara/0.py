def index():
    """
    This is not served anywhere in the content application.
    It is used explicitly in the context of generating host content since
    flask-frozen requires url_for's to crawl content.
    url_for's are not used with host.show_host directly and are instead
    dynamically generated through javascript for performance purposes.
    """
    return render_template('index.html')

