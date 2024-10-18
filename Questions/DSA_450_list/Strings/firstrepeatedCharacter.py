def firstRepChar(s):
        # code here
        min_index = len(s)+1
        ans = ''
        
        for i in range(len(s)-1):
            if s[i] in s[i+1:]:
                print("min index is: ", s.find(s[i], i+1 ))
                if s.find(s[i], i+1)  < min_index:
                    ans = s[i]
                    min_index  = s.find(s[i], i+1) 
            print(min_index, ans)
        if ans != '':
            return ans
        else:
            return -1
        

print(firstRepChar('ldutwihymacesxgikyyjnpbjpbl'))