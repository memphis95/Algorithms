def countDistinct(arr, N, K):
        # Code here
        d = {}
        ans = []
        for i in range(K):
            if arr[i] not in d:
                d[arr[i]] = 1
            else:
                d[arr[i]] += 1
        ans.append(len(d))
        print("map is: ",d)
        print(ans)
        i = 1
        while i+K-1 < N:
            # print("array is: ", arr[i:i+K])
            if d[arr[i-1]] > 1:
                d[arr[i-1]] -= 1
            else:
                d.pop(arr[i-1])
                
            # print("last element is: ", i+K-1 ,arr[i+K-1])
            if arr[i+K-1] not in d:
                d[arr[i+K-1]] = 1
            else:
                d[arr[i+K-1]] += 1
            
            # print("map is: ", d)
            ans.append(len(d))
            i += 1
            # print(d)
        return ans
        
print(countDistinct([1,2,1,3,4,2,3], 7, 4))
# print(countDistinct())
# print(countDistinct())