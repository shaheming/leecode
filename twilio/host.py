def countHost(fileIn, fileOut):

    hostMap = {}
    with open(fileIn) as file:
        lines = file.readlines()
        for l in lines:
            host, count = l.split()
            hostMap[host] = int(count) + hostMap.get(host, 0)
    with open(fileOut, 'w') as file:
        for l in sorted(hostMap.items(), key=lambda host: -host[1]):
            file.write(l[0] + " " + str(l[1]) + '\n')

countHost('./host.txt','./hostout.txt')
