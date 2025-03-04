def dl_file(url, dest, chunk_size=6553):
    """Download `url` to `dest`"""
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(dest, 'wb') as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)

