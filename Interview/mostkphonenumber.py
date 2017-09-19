phone_list=[21210,21210,94025,21210,94025,12345]
#from collections import Counter
def mostK(alist,k):
    newlist=[]
    buff_dict={}
    for item in alist:
        if item not in newlist:
            newlist.append(item)

    for i in range(len(newlist)):
        buff_dict[newlist[i]]=alist.count(newlist[i])

    result = sorted(buff_dict,key = buff_dict.__getitem__)[::-1]

    return result[0:k]

print mostK(phone_list,1)
