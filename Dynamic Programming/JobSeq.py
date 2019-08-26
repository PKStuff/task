def index(JobID, Profit, Deadline):
    sorted_profit_index = []

    for i in sorted(Profit, reverse=True):
        sorted_profit_index.append(Profit.index(i))
    
    #print(sorted_profit_index)

    JobID1 = []
    Deadline1 = []
    for i in sorted_profit_index:
        JobID1.append(JobID[i])
        Deadline1.append(Deadline[i])
    
    Profit = sorted(Profit, reverse=True)

    dict1 = {}
    job = []

    for i,j,k in zip(JobID1, Profit, Deadline1):
        if k not in dict1.keys():
            dict1[k] = j
            job.append(i)
        else:
            a = k
            while(a>=1):
                if a not in dict1.keys():
                    dict1[a] = j
                    job.append(i)
                    break
                a-=1
    #print(dict1)
    print(job)


    # for char in zip(JobID1, Profit, Deadline1):
    #     print(char)
    



if __name__ == '__main__':
    Job_Id = list(map(str,input("Enter the JobIDs:").split()))
    Profit = list(map(int,input("Enter the Profits:").split()))
    Deadline = list(map(int,input("Enter the Deadlines:").split()))
    index(Job_Id, Profit, Deadline)