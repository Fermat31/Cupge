def merge(l1,l2):
    l=[]
    i=j=0
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            l.append(l1[i])
            i+=1
        else:
            l.append(l2[j])
            j+=1
    l+=l1[i:len(l1)]
    l+=l2[j:len(l2)]
    return l

l1=[5,15,70,94]
l2=[32,39,52,81,94,95]
def merge_sort(l):
    if len(l)<=1:
        return l
    mid=len(l)//2
    left=l[:mid]
    right=l[mid:]
    l1=merge_sort(left)
    l2=merge_sort(right)
    return merge(l1,l2)
l=[8, 6, 19, 12, 44, 32, 2, 18, 20, 9, 10, 34, 1, 21, 4]
print(merge_sort(l))