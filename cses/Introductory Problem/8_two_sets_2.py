"""
PS: To divide the numbers 1,2,...,n into two sets of equal sum
"""
def is_two_sets(n):
   a = []
   b = []
   sum_n = (n * (n+1))//2
   """
   The below approach as works : 
   each set of values have same sum so that will be 1/2 of sum_of_n_numbers

   assign subset_sum = 1/2 (sum_of_n_numbers)

   for each number from n to 1:
       if number is less than or equal to the subset_sum:
           append the number to the subset A
           decrease the subset_sum by number
        else:
            append the number to the subset B

    main idea -> fill the one of the subsets with the numbers whose summation equals to
                subset_sum

   """
   if sum_n%2 ==0:
       subset_sum = sum_n //2
       for i in range(n,0,-1):
           print(i, subset_sum)
           if i <= subset_sum:
               subset_sum -= i
               a.append(i)
           else:
               b.append(i)
       print("YES")
       print(len(a))
    #    print(*a, sep=' ')
       print(len(b))
    #    print(*b, sep=' ')
   else:
       print("NO")


if __name__ == "__main__":
    number = int(input())
    is_two_sets(number)
