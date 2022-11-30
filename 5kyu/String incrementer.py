def increment_string(strng):
    letters = ''
    numbers = ''
    for x in strng:
        if x.isdigit():
            numbers += x
        else:
            letters += numbers + x
            numbers = ''
    i = len(numbers)
    if i == 0:
        return(letters + '1')
    else:
        result = int(numbers) + 1
        return(letters + format(result, f'0{i}d'))
