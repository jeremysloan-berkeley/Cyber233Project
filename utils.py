def get_age_groups():
    results = []
    for i in range(20, 80, 10):
        results.append(i)
    return results

def get_short_gender_name(g):
    if g == "Male":
        return "M"

    if g == "Female":
        return "F"

    return "NB"

def get_short_empl_status(e):
    if e == 'Unemployed':
        return "UN"

    if e == 'Part-Time':
        return "PT"

    if e == 'Full-Time':
        return "FT"

    return "SE"
