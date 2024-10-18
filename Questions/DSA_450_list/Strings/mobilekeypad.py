def printSequence(S):
        # code here
        str = ["2", "22", "222",
                "3", "33", "333",
                "4", "44", "444",
                "5", "55", "555",
                "6", "66", "666",
                "7", "77", "777", "7777",
                "8", "88", "888",
                "9", "99", "999", "9999"]
        ans = ''
        for i in S.upper():
            if i == ' ':
                ans += '0'
            else:
                index = ord(i) - ord('A')
                ans += str[index]
            
        return ans
print(printSequence(' JVWN'))