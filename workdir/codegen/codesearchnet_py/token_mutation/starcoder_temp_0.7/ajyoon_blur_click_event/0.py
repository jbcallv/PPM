def click_event(event):
    """On click, bring the machine under the table to Life"""
    global current_x
    if event.button == 1:
        current_x += 1

