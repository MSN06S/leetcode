def twoSum(nums,target):
    # create a hash table
    hashtable = {}
    for i in range(len(nums)):
        hashtable[nums[i]] = i

    for i in range(len(nums)):
        x = target - nums[i]
        if x in hashtable and hashtable[x]!=i:
            return [i,hashtable[x]]
        


nums = [2,11,7,17,15]
target = 9

print(twoSum(nums,target))