def fixer(base, target):
    """Parse it from fixer.io."""
    fixer_url = "https://api.fixer.io/{}?base={}".format(target, base)
    with urllib.request.urlopen(fixer_url) as url:
        data = json.loads(url.read().decode())
        return float(data["rates"][base])


