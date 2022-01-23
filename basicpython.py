import math

def get_data(path):
    with open(path) as file:
        lines = file.readlines()
    a = ''
    for line in lines:
        a += line.replace("\n"," ")
    b = list(int(num) for num in a.split(' '))
    return b

data = get_data(r'D:\Duke\821\basic python\example.txt')
print(data)

def analyze_data(nums, command):

    if command == "average":
        avg = sum(nums)/len(nums)
        return avg
    
    elif command == "standard deviation":
        s = 0.0
        avg = sum(nums)/len(nums)
        for i in nums:
            s += math.pow((i - avg), 2)
        std = math.sqrt(s/len(nums))
        return std

    elif command == "covariance":
        nums1 = nums[ :(len(nums)//2)]
        nums2 = nums[(len(nums)//2): ]
    
        avg1 = sum(nums1)/len(nums1)
        avg2 = sum(nums2)/len(nums2)
        
        cov = 0.0
        for j in range(0, len(nums1)):
            cov += (nums1[j]-avg1)*(nums2[j]-avg2)/len(nums1)
        return cov
    
    elif command == "correlation":
        nums1 = nums[ :(len(nums)//2)]
        nums2 = nums[(len(nums)//2): ]
    
        avg1 = sum(nums1)/len(nums1)
        avg2 = sum(nums2)/len(nums2)
        cov = 0.0
        for j in range(0,len(nums1)):
            cov += (nums1[j]-avg1)*(nums2[j]-avg2)/len(nums1)
    
        var1 = 0.0
        for i in nums1:
            var1 += math.pow((i-avg1),2)
        sd1 = math.sqrt(var1/len(nums1))
    
        var2 = 0.0
        for i in nums2:
            var2 += math.pow((i-avg2),2)
        sd2 = math.sqrt(var2/len(nums2))

        corr = cov/(sd1*sd2)
    
        return corr

print(analyze_data(data, "average"))
print(analyze_data(data, "standard deviation"))
print(analyze_data(data, "covariance"))
print(analyze_data(data, "correlation"))


