def hashListLenghts(lst,lns,ip=0,skip=0,verbose=False):

    il = 0
    while il<len(lns):

        # unroll the list so that current position is at first place
        lst = lst[ip:]+lst[:ip]

        # makes inversion according to lenght
        lst = lst[:lns[il]][::-1]+lst[lns[il]:]

        # re-roll list back in proper order
        lst = lst[-ip:]+lst[:-ip]

        ip = (ip+lns[il]+skip)%len(lst)
        il = il+1
        skip+=1

    return lst,ip,skip

def processList(lst,lns_asc):
    ip=0
    skip=0
    for _ in range(64):
        lst,ip,skip = hashListLenghts(lst,lns_asc,ip,skip)
    return lst

def densehash(lst):
    dh = []
    for i in range(16):
        h = 0
        for i in lst[i*16:i*16+16]:
            h = h ^ i
        dh.append(h)
    return dh

def knotHash(l):
    add = [17, 31, 73, 47, 23]
    l += add
    lst = [ i for i in range(256) ]
    lst = processList(lst,l)
    o = ""
    for d in densehash(lst):
        h = hex(d)[2:]
        if len(h)==1:
            o += "0"+h
        else:
            o += h
    return o
