def dataConvert(date):

    monthAbbs = ["jan", 'feb', 'mar', 'apr', 'may',
                 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
    monthMap = {monthAbbs[i]: str(i+1) for i in range(len(monthAbbs))}

    parse = date.split(" ")
    index = 0

    while ord(parse[0][index]) >= ord('0') and ord(parse[0][index]) <= ord('9'):
        index += 1

    day = parse[0][:index]
    month = monthMap[parse[1].lower()]
    if int(month) < 10:
        month = '0'+month
    if int(day) < 10:
        day = '0' + day
    year = parse[2]
    return year + '-' + month + '-' + day


print(dataConvert("31st Jul 2001"))
