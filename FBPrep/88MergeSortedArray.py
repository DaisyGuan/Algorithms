def merge(nums1,m,nums2,n):
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1

    if n > 0:
        nums1[:n] = nums2[:n]
    return nums1

#print merge([1,2,3,0,0],3,[2,4],2)
#[1,2,3]

def merge2(nums1,m,nums2,n):
    newList =[]
    i=j=0
    while i<m and j<n:
        if nums1[i] <= nums2[j]:
            newList.append(nums1[i])
            i += 1
        else:
            newList.append(nums2[j])
            j += 1

    if i < m:
        newList += nums1[i:m]
    if j < n:
        newList += nums2[j:n]
    return newList


print merge2([1,2,3,0,0],3,[2,4],2)
