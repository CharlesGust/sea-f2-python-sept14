def safe_input():
    try:
        raw_input('Press CTRL+C (KeyboardInterrupt) or CTRL+D (EOFError), or something else to pass: ')
    except KeyboardInterrupt:
        None
    except EOFError:
        None