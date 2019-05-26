def get_weight_for_input(options, input):
    pieces = input.split(" ")

    for item in options:
        if pieces[1] in item.abbreviations:
            return (float(pieces[0]), item)

    # return een lege lijst als de code hieraan toe komt
    return (
        float(pieces[0])
    )