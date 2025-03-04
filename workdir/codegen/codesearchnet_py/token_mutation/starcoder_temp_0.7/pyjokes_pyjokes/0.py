def get_joke(language='en', category='neutral'):
    """
    Parameters
    ----------
    category: str
        Choices: 'neutral', 'chuck', 'all', 'twister'
    lang: str
        Choices: 'en', 'de', 'es', 'gl', 'eu', 'it'

    Returns
    -------
    joke: str
    """
    try:
        return pyjokes.get_joke(language, category)
    except Exception as e:
        print('Error getting joke: {}'.format(e))
        return ''

