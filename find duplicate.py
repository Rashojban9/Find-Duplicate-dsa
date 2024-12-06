class duplicate:
    def findDuplicatde(self,nums):
        a=len(nums)
        dub=[]
        for i in range(a):
            for j in range(i+1,a):
                if nums[i]==nums[j]:
                    dub.append(nums[i])
        return dub
array=[1,2,3,3,44,55,100]
dubl=duplicate()
arr=dubl.findDuplicatde(array)

d=len(arr)
if d<=1:
    print("duplicate number is ",end="")
    print (arr[0])
else:
    print("duplicate number are ",end="")
    for num in arr:
        print(num,end=",")
                    
