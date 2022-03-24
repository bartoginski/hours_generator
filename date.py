def get_month(date):
    month = int(date[3:5]) - 1
    months = [
        "styczniu",
        "lutym",
        "marcu",
        "kwietniu",
        "maju",
        "czerwcu",
        "lipcu",
        "sierpniu",
        "wrześniu"
        "październiku"
        "listopadzie",
        "grudniu"
    ]
    return months[month]


def get_year(date):
    return date[-4:]
