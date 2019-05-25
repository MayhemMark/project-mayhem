def get_weight_for_input(options, input):
    pieces = input.split(" ")

    for item in options:
        for abb in item.abbreviations:
            if pieces[1] == abb:
                return (
                    float(pieces[0]),
                    item
                )
    
    # return een lege lijst als de code hieraan toe komt
    return (
        pieces[0]
    )