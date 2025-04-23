def copy_to_clipboard(i): # pragma: no cover 
    """
    Input:  {
              string - string to copy

    Output: {
              return       - error code =  0, if successful
                                         >  0, if error
              (error)      - error if if , > 0
            }
    """
    try:
        pyperclip.copy(i['string'])
        return {'return':0}
    except Exception as e:
        return {'return':1, 'error':'unable to copy to clipboard:'+ str(e)}

