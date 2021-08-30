# Problem Statement
# Write a python function which searches for a particular substring in a given string. The substring may occur more than once in the string. If found, return the number of occurrences of the substring in the string. Otherwise, return 0.
# Perform case sensitive string comparison wherever necessary.

def pattern_search(text, pattern):
    #Remove pass and write your logic here
    occurance = 0 #number of occurance of the pattern
    i = 0 # intial position in text string
    j = 0 # intial position in pattern string
    while(i < len(text)):
        flag = False # flag to keep check whether the substring matched with pattern or not
        if(text[i] == pattern[j]):
            for k in range(1,len(pattern)):
                if(text[i+k] == pattern[j+k]):
                    flag = True
                else:
                    flag = False
                    break
            if flag == True:
                occurance += 1
                i = i+len(pattern)
            else:
                i += 1
        else:
           i += 1
        
    return occurance    

#Use different values for text and pattern and test your program
text = "MESMERIZING MESSAGE"
pattern = "MES"
result=pattern_search(text, pattern)
print("The given text:",text)
print("Pattern:",pattern)
print("No. of occurrences of the pattern :",result)