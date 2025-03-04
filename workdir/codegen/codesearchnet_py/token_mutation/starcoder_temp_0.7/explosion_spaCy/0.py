def load_model_from_path(model_path, meta=False, **overrides):
    """Load a a from a data directory path. Creates path file with
    pipeline from meta.json and then calls from_disk() with path."""
    with make_path(model_path, **overrides).open('rb') as file_:
        return load_model(file_, meta=meta)

