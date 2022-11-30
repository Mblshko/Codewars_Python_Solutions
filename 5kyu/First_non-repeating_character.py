def first_non_repeating_letter(string):
    string_lower = string.lower()
    res = ''
    for x in string:
        if string_lower.find(x.lower()) == string_lower.rfind(x.lower()):
            res += x
    if len(res) == 0:
        return ''
    else:
        return res[0]
