from click import style


def colour(colour, message, bold=False):
    """ Color a message """
    return style(fg=colour, text=message, bold=bold)


def yellow(message, bold=False):
    """ Color in yellow """
    return colour('yellow', message, bold)


def red(message, bold=False):
    """ Color in red """
    return colour('red', message, bold)


def green(message, bold=False):
    """ Color in red """
    return colour('green', message, bold)
