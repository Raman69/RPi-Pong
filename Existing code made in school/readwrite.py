
def tw(n):
    r = open("led.txt")
    lines = r.readlines()
    w = open('led.txt','w')
    write = w.writelines(n)
    a = open('led.txt','a')
    a = a.writelines(n)
    r = open("led.txt")
    lines = r.readline()
