def get_tour(index):
    """
    This function generates a list of tours.
    
    The index argument is used to retrieve a particular tour. If None is
    passed, it will return the full list of tours. If instead -1 is given,
    this function will return a test tour

    To add more tours a new variable needs to be created to hold the list of
    dicts and the list table at the bottom of this function needs to be
    updated accordingly
    """
    tours = [
        {
            "title": "Tour 1",
            "desc": "It's a simple tour with no extras",
            "steps": [
                ("Including a step with a <b>title</b>", "This is the description of the step"),
                ("Including a step with a <b>title</b>", "This is the description of the step"),
                ("Including a step with a <b>title</b>", "This is the description of the step"),
            ]
        },
        {
            "title": "Tour 2",
            "desc": "It's a simple tour with a link",
            "steps": [
                ("Including a step with a <b>title</b>", "This is the description of the step"),
                ("Including a step with a <b>title</b>", "This is the description of the step"),
                ("Including a step with a <b>title</b>", "This is the description of the step"),
                ("Including a step with a <b>title</b>", "This is the description of the step"),
                ("Including a step with a <b>title</b>", "This is the description of the step"),
                ("Including a step with a <b>title</b>", "This is the description of the step"),
                ("Including a step with a <b>title</b>", "This is the description of the step"),
                ("Including a step with a <b>title</b>", "This is the description of the step"),
                ("Including a step with a <b>title</b>", "This is the description of the step"),
                ("Including a step with a <b>title</b>", "This is the description of the step"),
                ("Including a step with a <b>title</b>", "This is the description of the step"),
                ("Including a step with a <b>title</b>", "This is the description of the step"),
                ("Including a step with a <b>title</b>", "This is the description of the step"),
                ("Including a step with a <b>title</b>", "This is the description of the step"),
                ("Including a step with a <b>title</b>", "This is the description of the step"),
                ("Including a step with a <b>
