def roundRobin(process, n, quantum):

    # Write your code here.
    current_time = 0
    arrival_time = [0] * n
    burst_time = process.copy() # the time the process takes for its execution
    completion_time = [0] * n # time at which the process complete its execution
    turn_a_time = [0] * n #time difference between the completion time and the arrival time
    waiting_time = [0] * n # time difference between the tat and burst time
    
    


    # rem_bt = [0] * n
    # wt = [0] * n
    # for i in range(n):
    #     rem_bt[i] = process[i]
    # t = 0

    # while(1):
    #     done = True

    #     for i in range(n):
    #         if (rem_bt[i]> 0):
    #             done = False
    #             if (rem_bt[i] > quantum):
    #                 t += quantum
    #                 rem_bt[i] -= quantum
    #             else:
    #                 t = t + rem_bt[i]
    #                 wt[i] = t - process[i]
    #                 rem_bt[i] = 0
    #     if (done == True):
    #         break
    # print(wt)

    arr = process.copy()

    while(not all(item==0 for item in arr)):
        for i in range(n):
            if(arr[i]>0):
                if arr[i]>quantum:
                    current_time += quantum
                    arr[i] -= quantum
                    print(arr)
                else:
                    current_time += arr[i]
                    completion_time[i] = current_time
                    print("process completion: ", i, "completion time: ", completion_time[i])
                    arr[i] = 0
                    print(arr)
    print(completion_time)

    for i in range(n):
        turn_a_time[i] = completion_time[i] - burst_time[i]
        waiting_time[i] = turn_a_time[i] - burst_time[i]

    print(turn_a_time,waiting_time)











    # i = 0 # process 0 
    # while (not all(item ==0 for item in arr)):
    #     # if the burst time of the process i is grater than or equal to quantum unit
    #     if arr[i] >= quantum:
    #         # increasing the current time by the quantum unit
    #         current_time += quantum
    #         # decreassing the burst time of the process i by quantum unit
    #         arr[i] -= quantum 
    #         #  if the remaining burst time of process i is 0
    #         if arr[i] == 0:
    #             completion_time[i] = current_time
    #             print("process completion: ", i, "completion time: ", completion_time[i])
    #     # if the burst time of the process i is less than quantum unit
    #     elif arr[i] < quantum:
    #         # setting burst time for process i to 0
    #         arr[i] = 0
    #         # increasing the current time by burst time of the process i
    #         current_time += arr[i]
    #         # setting the completion time for process i
    #         completion_time[i] = current_time 
    #         print("process completion: ", i, "completion time: ", completion_time[i])
    #         # time remaining in the quantum time
    #         remaining_time = quantum - arr[i]
    #         i += 1
    #         i = i%n
    #         while remaining_time != 0:
    #             if arr[i] >= remaining_time:
    #                 # decreasing the burst time of the process by remaining burst time
    #                 arr[i] -= remaining_time
    #                 # increasing the current time with remaining time
    #                 current_time += remaining_time
    #                 if arr[i] == 0:
    #                     completion_time[i] = current_time
    #                     print("process completion: ", i, "completion time: ", completion_time[i])
    #                 remaining_time = 0
    #             elif arr[i] < remaining_time:
    #                 arr[i] = 0
    #                 current_time += arr[i]
    #                 completion_time[i] = current_time
    #                 remaining_time -= arr[i]
    #                 i += 1
    #             i = i%n
    #     i += 1
    #     i = i%n

    # print("completion time array: ", completion_time)












    # while(not all(item == 0 for item in arr)):
    #     for i in range(n):
    #         if arr[i]>2:
    #             total_time += quantum
    #             arr[i] -= quantum
    #         elif arr[i] == 2:
    #             total_time += quantum
    #             arr[i] = 0
    #             process_finish[i] = total_time
    #         elif arr[i] == 1:
    #             total_time += 1
    #             arr[i] = 0
    #             process_finish[i] = total_time

       
        
    # while(not all(item == 0 for item in arr )):
    #     i = 0
    #     if arr[i]>= quantum:
    #         total_time += quantum
    #         arr[i] = arr[i] - quantum
    #         if arr[i] == 0:
    #             process_finish[i] = total_time
    #             print("process finished: ", i)
    #             print("time at process completed: ", total_time)
    #         if arr[i]< quantum and arr[i]>0:
    #             total_time += arr[i]
    #             arr[i] -= arr[i]
    #             process_finish[i] = total_time
    #             print("process finished: ", i)
    #             print("time at process completed: ", total_time)
    #             remaining_time = quantum - arr[i]
    #             i = i+1
    #             while remaining_time != 0:
    #                 if arr[i] >= remaining_time:
    #                     total_time += remaining_time
    #                     arr[i] -= remaining_time
    #                     if arr[i] == 0:
    #                         process_finish[i] = total_time
    #                         print("process finished: ", i)
    #                         print("time at process completed: ", total_time)
    #                         remaining_time = 0
    #                         break
    #                 elif arr[i] < remaining_time and arr[i]>0:
    #                     total_time += (remaining_time - arr[i])
    #                     remaining_time -= arr[i]
    #                     arr[i] = 0
    #                     process_finish[i] = total_time
    #                     print("process finished: ", i)
    #                     print("time at process completed: ", total_time)
    #                     i += 1
    #     i += 1
    #     i = i%n

    # print(process_finish)


            
                # while remaining_time != 0 and i<n-1:
                #     if arr[i+1]>=remaining_time:
                #         total_time += (arr[i+1] - remaining_time)
                #         arr[i+1] -= remaining_time
                #         remaining_time = 0
                #         if arr[i+1] == 0:
                #             process_finish[i+1] = total_time
                #             print("process finished: ", i)
                #             print("time at process completed: ",  total_time)
                #             break
                #     elif arr[i+1]< remaining_time:
                #         total_time += (remaining_time-arr[i+1])
                #         process_finish[i] = total_time
                #         remaining_time -= arr[i+1]
                #     i += 1
    # print("finish time of the processes: ",process_finish) 
    # for i in range(n):
    #     process_finish[i] = process_finish[i] - process[i]
    # print("time taken to complete process: ", process_finish)

    


if __name__ == "__main__":
    process = [1,2,2,2,2,2]
    n = len(process)
    quantum = 2
    roundRobin(process, n, quantum)




# 3
# 6 2
# 1 2 2 2 2 2 
# 6 1
# 2 2 2 2 2 1
# 7 4
# 6 6 6 6 6 6 6


# 3
# 10 20
# 7 13 18 3 8 4 10 15 12 15 
# 10 5
# 12 14 19 19 18 1 6 15 10 3 
# 10 3
# 19 5 1 17 4 15 8 13 1 13 


# 2
# 7 1
# 3 3 5 1 3 1 4
# 4 4
# 8 9 12 15

# 1
# 7 2
# 3 3 5 3 3 1 4
