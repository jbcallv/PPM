def summary(title, sentences=0, chars=0, auto_suggest=True, redirect=True):
  '''
  Plain text version of the page.

  .. note:: This is a convenience wrapper - auto_suggest and redirect are enabled by default

  Keyword arguments:

  * sentences - if set, return the first `sentences` sentences (can be no greater than 10).
  * chars - if set, return only the first `chars` characters (actual text returned may be slightly longer).
  * auto_suggest - let Wikipedia find a valid page title for the query
  * redirect - allow redirection without raising RedirectError
  '''

  # use auto_suggest and try to get the correct article
  # also, use page's error checking to raise DisambiguationError if necessary
  page_info = page(title, auto_suggest=auto_suggest, redirect=redirect)
  title = page_info.title
  pageid = page_info.pageid

  query_params = {
    'prop': 'extracts',
    'explaintext': '',
    'titles': title
  }

  if sentences:
    query_params['exsentences'] = sentences
  elif chars:
    query_params['exchars'] = chars
  else:
    query_params['exintro'] = ''

  request = _wiki_request(query_params)
  summary = request['query']['pages'][pageid]['extract']

  return summary

