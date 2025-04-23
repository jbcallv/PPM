def main():
    """This is the standard code for ia-wrapper."""
    config = load_config()
    app = create_app(config)
    app.run(port=8000)


