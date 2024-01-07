def EscapeApostrophes(unsanitisedString):
    return str(unsanitisedString).replace("'", "''")