import re
def firstIndexSubString(s,x):
    x = x.replace("*",".*")
    #print x
    return re.search(x,s).start()

print firstIndexSubString("antewrwerew","t*w")
