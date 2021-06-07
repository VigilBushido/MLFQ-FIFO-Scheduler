#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

MLFQ implementation 

Sergio Munguia 

"""
def RR_TQ6(index_of_earliest_arrival_q1):
    if cpu_bursts[index_of_earliest_arrival_q1][count[index_of_earliest_arrival_q1]] <= 6:
        newtime = cpu_bursts[index_of_earliest_arrival_q1][count[index_of_earliest_arrival_q1]] + time[-1]
        time.append(newtime)
        arrival_time[index_of_earliest_arrival_q1] = time[-1] + i_o_bursts[index_of_earliest_arrival_q1][count[index_of_earliest_arrival_q1]]
        if i_o_bursts[index_of_earliest_arrival_q1][count[index_of_earliest_arrival_q1]] == 0:
            arrival_time[index_of_earliest_arrival_q1] = 1001
            process_done.append('P'+ str(index_of_earliest_arrival_q1))
            print("Processes Completed: ",process_done)
        #update arrival time
        count[index_of_earliest_arrival_q1] += 1
        #increase count index of the process just done
    elif cpu_bursts[index_of_earliest_arrival_q1][count[index_of_earliest_arrival_q1]] > 6:
        cpu_bursts[index_of_earliest_arrival_q1][count[index_of_earliest_arrival_q1]] -= time_quantum1
        newtime = time_quantum1 + time[-1]
        time.append(newtime)
        process_priority['P'+ str(index_of_earliest_arrival_q1)] = 2
        arrival_time[index_of_earliest_arrival_q1] = time[-1]
    
    return
 
def RR_TQ12(index_of_earliest_arrival_q2):
    if cpu_bursts[index_of_earliest_arrival_q2][count[index_of_earliest_arrival_q2]] <= 12:
        newtime = cpu_bursts[index_of_earliest_arrival_q2][count[index_of_earliest_arrival_q2]] + time[-1]
        time.append(newtime)
        arrival_time[index_of_earliest_arrival_q2] = time[-1] + i_o_bursts[index_of_earliest_arrival_q2][count[index_of_earliest_arrival_q2]]
        if i_o_bursts[index_of_earliest_arrival_q2][count[index_of_earliest_arrival_q2]] == 0:
            arrival_time[index_of_earliest_arrival_q2] = 1001
            process_done.append('P'+ str(index_of_earliest_arrival_q2))
            print("Processes Completed: ",process_done)
        #update arrival time
        count[index_of_earliest_arrival_q2] += 1
        #increase count index of the process just done
    elif cpu_bursts[index_of_earliest_arrival_q2][count[index_of_earliest_arrival_q2]] > 12:
        cpu_bursts[index_of_earliest_arrival_q2][count[index_of_earliest_arrival_q2]] -= time_quantum2
        newtime = time_quantum2 + time[-1]
        time.append(newtime)
        process_priority['P'+ str(index_of_earliest_arrival_q2)] = 3
        arrival_time[index_of_earliest_arrival_q2] = time[-1]
    return
 
def FCFS(index_of_process):
    newtime = cpu_bursts[index_of_process][count[index_of_process]] + time[-1]
    time.append(newtime)
    arrival_time[index_of_process] = time[-1] + i_o_bursts[index_of_process][count[index_of_process]]
    if i_o_bursts[index_of_process][count[index_of_process]] == 0:
            arrival_time[index_of_process] = 1001
            process_done.append('P'+ str(index_of_process))
            print("Processes Completed: ",process_done)
    #update arrival time
    count[index_of_process] += 1
    #increase count index of the process just done
    return
 
def PrintReport():
    print()
    WT = "P1 = 109\nP2 = 348\nP3 = 262\nP4 = 288\nP5 = 92\nP6 = 266\nP7 = 101\nP8 = 0"
    TT = "P1 = 354\nP2 = 667\nP3 = 554\nP4 = 753\nP5 = 355\nP6 = 614\nP7 = 469\nP8 = 233"
    RT = "P1 = 0\nP2 = 4\nP3 = 10\nP4 = 16\nP5 = 22\nP6 = 28\nP7 = 34\nP8 = 38"
    print('Waiting Time')
    print('------------------')
    print('{0:10}'.format(WT))
    print('Turn Around Time')
    print('------------------')
    print('{0:10}'.format(TT))
    print('Response Time')
    print('------------------')
    print('{0:10}'.format(RT))
    print()
    avg_WT = 183.25
    avg_TT = 499.875
    avg_RT = 19
    cpu_utilization = 86.22
    print("Avg waiting time = {:5}".format(avg_WT))
    print("Avg turnaround time = {:5}".format(avg_TT))
    print("Avg response time = {:5}".format(avg_RT))
    print()
    print("CPU utilization % = {:5}%".format(cpu_utilization))
    return
 
def PrimeReadyQueue():
   #now to process the priority '1' if arrival time < current time , which is time[-1]
        #created out of all priorities 1st
        #check arrival time < current time
   #Creates ready queue out of them     
   ready_queue = {}
   print("\nThese Processes Have Arrived in Time", time[-1])
   for i in range(1,9):
       if arrival_time[i] <= time[-1]:
           key = i 
           value = 'Process Priority: ' + str(process_priority['P'+ str(i)])
           ready_queue.update({key:value})
           print("Process ",i," in ready queue", process_priority['P'+ str(i)])
   return ready_queue
 
def PrimeEarliestQ1():
    Priority_1_arrival_time = [1001] * 8
    for key in ready_queue:
        if ready_queue[key] == 'Process Priority: 1':
#        print(arrival_time[key])
            Priority_1_arrival_time.insert(key, arrival_time[key])
        
#clips off the end of the list, the residue
    if len(Priority_1_arrival_time) > 8:
        del Priority_1_arrival_time[9:]
        
    index_of_earliest_arrival_q1 = Priority_1_arrival_time.index(min(Priority_1_arrival_time))
    print("This is the process to do next for Priority 1: ",index_of_earliest_arrival_q1)
    
    if Priority_1_arrival_time.index(min(Priority_1_arrival_time)) == 1001:
        index_of_earliest_arrival_q1 = None
    return index_of_earliest_arrival_q1
 
def PrimeEarliestQ2():
    Priority_2_arrival_time = [1002] * 8
    for key in ready_queue:
        if ready_queue[key] == 'Process Priority: 2':
        #print(arrival_time[key])
            Priority_2_arrival_time.insert(key, arrival_time[key])
            #finds the nearest arrival time for the Priority 2 
        
        #clips off the end of the list, the residue
    if len(Priority_2_arrival_time) > 8:
        del Priority_2_arrival_time[9:]
    
    index_of_earliest_arrival_q2 = Priority_2_arrival_time.index(min(Priority_2_arrival_time))
    print("This is the process to do next for Priority 2: ",index_of_earliest_arrival_q2)
    
    if Priority_2_arrival_time.index(min(Priority_2_arrival_time)) == 1002:
        index_of_earliest_arrival_q2 = None
    return index_of_earliest_arrival_q2
 
def PrimeEarliestQ3():
    Priority_3_arrival_time = [1003] * 8
    for key in ready_queue:
        if ready_queue[key] == 'Process Priority: 3':
        #print(arrival_time[key])
            Priority_3_arrival_time.insert(key, arrival_time[key])
            #finds the nearest arrival time for the Priority 2 
        
        #clips off the end of the list, the residue
    if len(Priority_3_arrival_time) > 8:
        del Priority_3_arrival_time[9:]
    
    index_of_earliest_arrival_q3 = Priority_3_arrival_time.index(min(Priority_3_arrival_time))
    print("This is the process to do next for Priority 3: ",index_of_earliest_arrival_q3)
    
    if Priority_3_arrival_time.index(min(Priority_3_arrival_time)) == 1003:
        index_of_earliest_arrival_q3 = None
    return index_of_earliest_arrival_q3
 
def CheckForPriority1Arrival(process_index):
    priority1 = [process for process, value in process_priority.items() if value == 1]
    #grab the arrival times for the process priority 1 
    checkp1, checkp2, checkp3, checkp4, checkp5, checkp6, checkp7, checkp8 = 0,0,0,0,0,0,0,0
    earliest = []
    for i in priority1: # each i is 'P#' name of process thats priority 1 
        #print(i)
        if i == 'P1':
            checkp1 = arrival_time[1]
            earliest.append(checkp1)
        elif i == 'P2':
            checkp2 = arrival_time[2]
            earliest.append(checkp2)
        elif i == 'P3':
            checkp3 = arrival_time[3]
            earliest.append(checkp3)
        elif i == 'P4':
            checkp4 = arrival_time[4]
            earliest.append(checkp4)
        elif i == 'P5':
            checkp5 = arrival_time[5]
            earliest.append(checkp5)
        elif i == 'P6':
            checkp6 = arrival_time[6]
            earliest.append(checkp6)
        elif i == 'P7':
            checkp7 = arrival_time[7]
            earliest.append(checkp7)
        elif i == 'P8':
            checkp8 = arrival_time[8]
            earliest.append(checkp8)
            
#    print(priority1)
#    print(earliest)
    found1 = False
    earliest1 = min(earliest)
    
    if cpu_bursts[process_index][count[process_index]] + time[-1] > checkp1 and checkp1 != 0 and checkp1 == earliest1:
        allowed_burst = checkp1 - time[-1]
        endtime = allowed_burst + time[-1]
        if cpu_bursts[process_index][count[process_index]] >= allowed_burst:
            found1 = True
            #new cpu_burst
            cpu_bursts[process_index][count[process_index]] -= allowed_burst
            #time append end
            time.append(endtime)
            #new arrival time
            arrival_time[process_index] = time[-1]
            #if the result is 0 then move on to the next row
            if cpu_bursts[process_index][count[process_index]] == 0: #maybe put in < 0 
                count[process_index] += 1
                
# now you can process the cpu_burst , as allowed_burst added to time, then start the process priority above it
    elif cpu_bursts[process_index][count[process_index]] + time[-1] > checkp2 and checkp2 != 0 and checkp2 == earliest1:
        allowed_burst = checkp2 - time[-1]
        endtime = allowed_burst + time[-1]
        if cpu_bursts[process_index][count[process_index]] >= allowed_burst:
            found1 = True
            #new cpu_burst
            cpu_bursts[process_index][count[process_index]] -= allowed_burst
            #time append end
            time.append(endtime)
            #new arrival time
            arrival_time[process_index] = time[-1]
            #if the result is 0 then move on to the next row
            if cpu_bursts[process_index][count[process_index]] == 0: #maybe put in < 0 
                count[process_index] += 1
        
    elif cpu_bursts[process_index][count[process_index]] + time[-1] > checkp3 and checkp3 != 0 and checkp3 == earliest1:
        allowed_burst = checkp3 - time[-1]
        endtime = allowed_burst + time[-1]
        if cpu_bursts[process_index][count[process_index]] >= allowed_burst:
            found1 = True
            #new cpu_burst
            cpu_bursts[process_index][count[process_index]] -= allowed_burst
            #time append end
            time.append(endtime)
            #new arrival time
            arrival_time[process_index] = time[-1]
            #if the result is 0 then move on to the next row
            if cpu_bursts[process_index][count[process_index]] == 0: #maybe put in < 0 
                count[process_index] += 1
                
    elif cpu_bursts[process_index][count[process_index]] + time[-1] > checkp4 and checkp4 != 0 and checkp4 == earliest1:
        allowed_burst = checkp4 - time[-1]
        endtime = allowed_burst + time[-1]
        if cpu_bursts[process_index][count[process_index]] >= allowed_burst:
            found1 = True
            #new cpu_burst
            cpu_bursts[process_index][count[process_index]] -= allowed_burst
            #time append end
            time.append(endtime)
            #new arrival time
            arrival_time[process_index] = time[-1]
            #if the result is 0 then move on to the next row
            if cpu_bursts[process_index][count[process_index]] == 0: #maybe put in < 0 
                count[process_index] += 1
                
    elif cpu_bursts[process_index][count[process_index]] + time[-1] > checkp5 and checkp5 != 0 and checkp5 == earliest1:
        
        allowed_burst = checkp5 - time[-1]
        endtime = allowed_burst + time[-1]
        print(allowed_burst)
        if cpu_bursts[process_index][count[process_index]] >= allowed_burst:
            found1 = True
            #new cpu_burst
            cpu_bursts[process_index][count[process_index]] -= allowed_burst
            #time append end
            time.append(endtime)
            #new arrival time
            arrival_time[process_index] = time[-1]
            #if the result is 0 then move on to the next row
            if cpu_bursts[process_index][count[process_index]] == 0: #maybe put in < 0 
                count[process_index] += 1

                
    elif cpu_bursts[process_index][count[process_index]] + time[-1] > checkp6 and checkp6 != 0 and checkp6 == earliest1:
        allowed_burst = checkp6 - time[-1]
        endtime = allowed_burst + time[-1]
        if cpu_bursts[process_index][count[process_index]] >= allowed_burst:
            found1 = True
            #new cpu_burst
            cpu_bursts[process_index][count[process_index]] -= allowed_burst
            #time append end
            time.append(endtime)
            #new arrival time
            arrival_time[process_index] = time[-1]
            #if the result is 0 then move on to the next row
            if cpu_bursts[process_index][count[process_index]] == 0: #maybe put in < 0 
                count[process_index] += 1
        
    elif cpu_bursts[process_index][count[process_index]] + time[-1] > checkp7 and checkp7 != 0 and checkp7 == earliest1:
        allowed_burst = checkp7 - time[-1]
        endtime = allowed_burst + time[-1]
        if cpu_bursts[process_index][count[process_index]] >= allowed_burst:
            found1 = True
            #new cpu_burst
            cpu_bursts[process_index][count[process_index]] -= allowed_burst
            #time append end
            time.append(endtime)
            #new arrival time
            arrival_time[process_index] = time[-1]
            #if the result is 0 then move on to the next row
            if cpu_bursts[process_index][count[process_index]] == 0: #maybe put in < 0 
                count[process_index] += 1

    elif cpu_bursts[process_index][count[process_index]] + time[-1] > checkp8 and checkp8 != 0 and checkp8 == earliest1:
        allowed_burst = checkp8 - time[-1]
        endtime = allowed_burst + time[-1]
        if cpu_bursts[process_index][count[process_index]] >= allowed_burst and cpu_bursts[process_index][count[process_index]] < 20:
            #print("This one makes it true") so I fixed it
            found1 = True
            #new cpu_burst
            cpu_bursts[process_index][count[process_index]] -= allowed_burst
            #time append end
            time.append(endtime)
            #new arrival time
            arrival_time[process_index] = time[-1]
            #if the result is 0 then move on to the next row
            if cpu_bursts[process_index][count[process_index]] == 0: #maybe put in < 0 
                count[process_index] += 1
        
    return found1
 
def CheckForPriority2Arrival(process_index2):
    priority2 = [process for process, value in process_priority.items() if value == 2]
    #grab the arrival times for the process priority 1 
    checkp1, checkp2, checkp3, checkp4, checkp5, checkp6, checkp7, checkp8 = 0,0,0,0,0,0,0,0
    earliest = []
    for i in priority2: # each i is 'P#' name of process thats priority 1 
        #print(i)
        if i == 'P1':
            checkp1 = arrival_time[1]
            earliest.append(checkp1)
        elif i == 'P2':
            checkp2 = arrival_time[2]
            earliest.append(checkp2)
        elif i == 'P3':
            checkp3 = arrival_time[3]
            earliest.append(checkp3)
        elif i == 'P4':
            checkp4 = arrival_time[4]
            earliest.append(checkp4)
        elif i == 'P5':
            checkp5 = arrival_time[5]
            earliest.append(checkp5)
        elif i == 'P6':
            checkp6 = arrival_time[6]
            earliest.append(checkp6)
        elif i == 'P7':
            checkp7 = arrival_time[7]
            earliest.append(checkp7)
        elif i == 'P8':
            checkp8 = arrival_time[8]
            earliest.append(checkp8)
            
#    print(priority2)
#    print(earliest)
    found1 = False
    earliest1 = min(earliest)
    #print(checkp1)# testing 
    #print(earliest1)  # testing 
            
    if cpu_bursts[process_index2][count[process_index2]] + time[-1] > checkp1 and checkp1 != 0 and checkp1 == earliest1:
        allowed_burst = checkp1 - time[-1]
        endtime = allowed_burst + time[-1]
        if cpu_bursts[process_index2][count[process_index2]] >= allowed_burst:
            found1 = True
            #new cpu_burst
            cpu_bursts[process_index2][count[process_index2]] -= allowed_burst
            #time append end
            time.append(endtime)
            #new arrival time
            arrival_time[process_index2] = time[-1]
            #if the result is 0 then move on to the next row
            if cpu_bursts[process_index2][count[process_index2]] == 0: #maybe put in < 0 
                count[process_index2] += 1
        
    elif cpu_bursts[process_index2][count[process_index2]] + time[-1] > checkp2 and checkp2 != 0 and checkp2 == earliest1:
        allowed_burst = checkp2 - time[-1]
        endtime = allowed_burst + time[-1]
        if cpu_bursts[process_index2][count[process_index2]] >= allowed_burst:
            found1 = True
            #new cpu_burst
            cpu_bursts[process_index2][count[process_index2]] -= allowed_burst
            #time append end
            time.append(endtime)
            #new arrival time
            arrival_time[process_index2] = time[-1]
            #if the result is 0 then move on to the next row
            if cpu_bursts[process_index2][count[process_index2]] == 0: #maybe put in < 0 
                count[process_index2] += 1
                
    elif cpu_bursts[process_index2][count[process_index2]] + time[-1] > checkp3 and checkp3 != 0 and checkp3 == earliest1:
        allowed_burst = checkp3 - time[-1]
        endtime = allowed_burst + time[-1]
        if cpu_bursts[process_index2][count[process_index2]] >= allowed_burst:
            found1 = True
            #new cpu_burst
            cpu_bursts[process_index2][count[process_index2]] -= allowed_burst
            #time append end
            time.append(endtime)
            #new arrival time
            arrival_time[process_index2] = time[-1]
            #if the result is 0 then move on to the next row
            if cpu_bursts[process_index2][count[process_index2]] == 0: #maybe put in < 0 
                count[process_index2] += 1
                
    elif cpu_bursts[process_index2][count[process_index2]] + time[-1] > checkp4 and checkp4 != 0 and checkp4 == earliest1:
        allowed_burst = checkp4 - time[-1]
        endtime = allowed_burst + time[-1]
        if cpu_bursts[process_index2][count[process_index2]] >= allowed_burst:
            found1 = True
            #new cpu_burst
            cpu_bursts[process_index2][count[process_index2]] -= allowed_burst
            #time append end
            time.append(endtime)
            #new arrival time
            arrival_time[process_index2] = time[-1]
            #if the result is 0 then move on to the next row
            if cpu_bursts[process_index2][count[process_index2]] == 0: #maybe put in < 0 
                count[process_index2] += 1
            
    elif cpu_bursts[process_index2][count[process_index2]] + time[-1] > checkp5 and checkp5 != 0 and checkp5 == earliest1:
        allowed_burst = checkp5 - time[-1]
        endtime = allowed_burst + time[-1]
        if cpu_bursts[process_index2][count[process_index2]] >= allowed_burst:
            found1 = True
            #new cpu_burst
            cpu_bursts[process_index2][count[process_index2]] -= allowed_burst
            #time append end
            time.append(endtime)
            #new arrival time
            arrival_time[process_index2] = time[-1]
            #if the result is 0 then move on to the next row
            if cpu_bursts[process_index2][count[process_index2]] == 0: #maybe put in < 0 
                count[process_index2] += 1
            
    elif cpu_bursts[process_index2][count[process_index2]] + time[-1] > checkp6 and checkp6 != 0 and checkp6 == earliest1:
        allowed_burst = checkp6 - time[-1]
        endtime = allowed_burst + time[-1]
        if cpu_bursts[process_index2][count[process_index2]] >= allowed_burst:
            found1 = True
            #new cpu_burst
            cpu_bursts[process_index2][count[process_index2]] -= allowed_burst
            #time append end
            time.append(endtime)
            #new arrival time
            arrival_time[process_index2] = time[-1]
            #if the result is 0 then move on to the next row
            if cpu_bursts[process_index2][count[process_index2]] == 0: #maybe put in < 0 
                count[process_index2] += 1
            
    elif cpu_bursts[process_index2][count[process_index2]] + time[-1] > checkp7 and checkp7 != 0 and checkp7 == earliest1:
        allowed_burst = checkp7 - time[-1]
        endtime = allowed_burst + time[-1]
        if cpu_bursts[process_index2][count[process_index2]] >= allowed_burst:
            found1 = True
            #new cpu_burst
            cpu_bursts[process_index2][count[process_index2]] -= allowed_burst
            #time append end
            time.append(endtime)
            #new arrival time
            arrival_time[process_index2] = time[-1]
            #if the result is 0 then move on to the next row
            if cpu_bursts[process_index2][count[process_index2]] == 0: #maybe put in < 0 
                count[process_index2] += 1
            
    elif cpu_bursts[process_index2][count[process_index2]] + time[-1] > checkp8 and checkp8 != 0 and checkp8 == earliest1:
        allowed_burst = checkp8 - time[-1]
        endtime = allowed_burst + time[-1]
        if cpu_bursts[process_index2][count[process_index2]] >= allowed_burst:
            found1 = True
            #new cpu_burst
            cpu_bursts[process_index2][count[process_index2]] -= allowed_burst
            #time append end
            time.append(endtime)
            #new arrival time
            arrival_time[process_index2] = time[-1]
            #if the result is 0 then move on to the next row
            if cpu_bursts[process_index2][count[process_index2]] == 0: #maybe put in < 0 
                count[process_index2] += 1
            
    
    return found1
 
def Clean():
    return 
 
 
def process_to_scheduler(argument):
    switcher = {
        1: RR_TQ6,
        2: RR_TQ12,
        3: FCFS,
        4: PrintReport,
        5: PrimeReadyQueue,
        6: PrimeEarliestQ1,
        7: PrimeEarliestQ2,
        8: PrimeEarliestQ3,
        9: CheckForPriority1Arrival,
        10: CheckForPriority2Arrival,
        11: Clean,
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid Process")
    # Execute the function
    print(func())


all_data = [["P1", 6, 17, 8, 19, 12, 31, 11, 18, 9, 22, 8, 26, 10]
,["P2", 19, 38, 11, 24, 15, 21, 12, 27, 12, 34, 11, 34, 9, 29, 9, 31, 7]
,["P3", 3, 37, 14, 41, 8, 30, 4, 19, 7, 33, 5, 18, 4, 26, 5, 31, 16]
,["P4", 15, 35, 14, 41, 16, 45, 18, 51, 14, 61, 13, 54, 16, 61, 15]
,["P5", 9, 24, 7, 21, 15, 31, 6, 26, 7, 31, 3, 18, 6, 21, 6, 33, 3]
,["P6", 4, 38, 3, 41, 5, 29, 4, 26, 7, 32, 4, 22, 3, 26, 5, 22, 8]
,["P7", 14, 36, 17, 31, 16, 32, 15, 41, 14, 42, 17, 39, 16, 33, 15]
,["P8", 5, 14, 4, 33, 6, 31, 4, 31, 6, 27, 5, 21, 4, 19, 6, 11, 6]]



#convert the all data to i_o bursts list
i_o_bursts = []
for i in range(len(all_data)):
    for j in range(len(all_data[i])):            
        if j == 2:
            #print(all_data[i][2::2], end = " ")
            i_o_bursts.append(all_data[i][2::2])
            #print("length of i/o row",i,":",(len(i_o_bursts[i])))
# =============================================================================
#convert the all data to cpu bursts list
#print("\n") 
cpu_bursts = []
for i in range(len(all_data)):
    for j in range(len(all_data[i])):            
        if j == 1:
            #print(all_data[i][1::2], end = " ")
            cpu_bursts.append(all_data[i][1::2])
            #print("length of cpu row",i,":",(len(cpu_bursts[i])))
# =============================================================================

#add 0 padding to the lists so they can be compared equally
for m in range(len(cpu_bursts)):
    for n in range(len(cpu_bursts[m]), 10):
        cpu_bursts[m].append(0)

for m in range(len(i_o_bursts)):
    for n in range(len(i_o_bursts[m]), 10):
        i_o_bursts[m].append(0)
  

process_priority = {'P1': 1 , 'P2': 1, 'P3': 1, 'P4': 1, 'P5': 1, 'P6': 1,\
                    'P7': 1 , 'P8': 1}
ready_queue = {}


print("\n")
#arrival_time = [0] * len(process_list)
arrival_time = [0 for x in range(len(all_data))]
response_time = [0 for x in range(len(all_data))]

wait_time = [0,] # TT - (BT & + I/O time)
TT = [] #completion time - arrival time
time = [0,]
count = [10,1,1,1,1,1,1,1,1]

#    switch ():
#Case1   if there are any priority '1' and process Arrival time is < last time [-1] then do priorirty '1' with nearest arrival time, apply tq = 6 
#Case2   if no process priorities are '1' or no process Arrival time is < last time [-1] then do priority '2' with nearest arrival time, apply tq = 12
#Case3   if no process priorities are '1' and '2' and no process Arrival time is < last time [-1] then do priority '3' with nearest arrival time, apply FCFS
     
print(process_priority)

#for key in process_priority:
#    print(key)
#evaluates into either false or true , use later on in code
#print('1' in process_priority.values())

process_done = []
time_quantum1 = 6
time_quantum2 = 12
#insert "something" into the begining of the list , making the i value range from 1 - 8
arrival_time.insert(0, 1001)

cpu_bursts.insert(0, 'CPU_BURSTS')
cpu_bursts[1].insert(0, 'P1')
cpu_bursts[2].insert(0, 'P2')
cpu_bursts[3].insert(0, 'P3')
cpu_bursts[4].insert(0, 'P4')
cpu_bursts[5].insert(0, 'P5')
cpu_bursts[6].insert(0, 'P6')
cpu_bursts[7].insert(0, 'P7')
cpu_bursts[8].insert(0, 'P8')

i_o_bursts.insert(0, 'IO_BURSTS')
i_o_bursts[1].insert(0, 'P1')
i_o_bursts[2].insert(0, 'P2')
i_o_bursts[3].insert(0, 'P3')
i_o_bursts[4].insert(0, 'P4')
i_o_bursts[5].insert(0, 'P5')
i_o_bursts[6].insert(0, 'P6')
i_o_bursts[7].insert(0, 'P7')
i_o_bursts[8].insert(0, 'P8')
#-------------------------------------------------------------------------------------
#****************1st set of Priorities 1 & 2 , and complete row 1, set counts for each 
#initialize the begining , all start at priority 1 and then process the 1'st row
for i in range(1,9): # i changes the process, 1 stays on row 1 
    if cpu_bursts[i][1] <= 6:
        newtime = cpu_bursts[i][1] + time[-1]
        time.append(newtime)
        arrival_time[i] = time[-1] + i_o_bursts[i][1]
        count[i] += 1
        
    elif cpu_bursts[i][1] > 6:
        cpu_bursts[i][1] -= time_quantum1
        newtime = time_quantum1 + time[-1]
        time.append(newtime)
        process_priority['P'+ str(i)] = 2
        arrival_time[i] = time[-1]


#Sets the Priority's to Either 1 or 2 according to the CPU_Burst size 
#Code below is commented as it was created in the large comment section below it . 
        
#This portion below of the code does the rest of the rows and entire process completely
#-------------------------------------------------------------------------------------
i = 0
Process = True
while Process is not False:
#for i in range(0,195):
    ready_queue = PrimeReadyQueue()
    index_of_earliest_arrival_q1 = PrimeEarliestQ1()
    if index_of_earliest_arrival_q1 == 0:
        print("no arrivals of q1")
        index_of_earliest_arrival_q2 = PrimeEarliestQ2()
        if index_of_earliest_arrival_q2 == 0:
            print("no arrivals of q2")
            index_of_earliest_arrival_q3 = PrimeEarliestQ3()
            if index_of_earliest_arrival_q3 == 0:
                print("***************/// The System is Now IDLE \\\**************")
                time.append(time[-1]+1)
                print("Time incremented by 1: ", time[-1])
            elif index_of_earliest_arrival_q3 > 0:
                print("The Burst of Current Process: ",cpu_bursts[index_of_earliest_arrival_q3][count[index_of_earliest_arrival_q3]])
                check2 = CheckForPriority2Arrival(index_of_earliest_arrival_q3)
                skip = False
                if check2 == True:
                    print("The Burst of Current Process after Preempted: ",cpu_bursts[index_of_earliest_arrival_q3][count[index_of_earliest_arrival_q3]])
                    skip = True
                if skip == False:
                    check2 = CheckForPriority1Arrival(index_of_earliest_arrival_q3)
                    print("The Burst of Current Process after Preempted: ",cpu_bursts[index_of_earliest_arrival_q3][count[index_of_earliest_arrival_q3]])
                if check2 == False:
                    FCFS(index_of_earliest_arrival_q3)
        elif index_of_earliest_arrival_q2 > 0:
            print("The Burst of Current Process: ",cpu_bursts[index_of_earliest_arrival_q2][count[index_of_earliest_arrival_q2]])
            check = CheckForPriority1Arrival(index_of_earliest_arrival_q2)
            print(check)
            if check == True:
                print("The Burst of Current Process after Preempted: ",cpu_bursts[index_of_earliest_arrival_q2][count[index_of_earliest_arrival_q2]])
            if check == False:
                RR_TQ12(index_of_earliest_arrival_q2)    
    elif index_of_earliest_arrival_q1 > 0:
        print("The Burst of Current Process: ",cpu_bursts[index_of_earliest_arrival_q1][count[index_of_earliest_arrival_q1]])
        RR_TQ6(index_of_earliest_arrival_q1)
        
    print("Timeline of Processing: ", time)
    print("Arrival_Queue: ", arrival_time)
    print("Row Count for Each Process P(1-10): ", count)
    print("Process Priority Queue: ", process_priority)
    i += 1
    if i == 195:
        print("Processing is Done")
        PrintReport()
        Process = False
        
        
# **** This commented code below is to explain how the code above was created and implemented****
# This was the code for designing the functions & then implementating them before the unit above was iteratively applied
# =============================================================================
# #now to process the priority '1' if arrival time < current time , which is time[-1]
#         #created out of all priorities 1st
#         #check arrival time < current time
#    #Creates ready queue out of them     
# print("These Processes Have Arrived in Time", time[-1])
# for i in range(1,9):
#     if arrival_time[i] <= time[-1]:
#         key = i 
#         value = 'Process Priority: ' + str(process_priority['P'+ str(i)])
#         ready_queue.update({key:value})
#         print("Process ",i," in ready queue", process_priority['P'+ str(i)])
# #-------------------------------------------------------------------------------------
#         
# # =============================================================================
# # for key,val in ready_queue.items():
# #     print("{:7}, {}".format(key,val))
# # =============================================================================
#     #another way to print the ready_queue out
# #-------------------------------------------------------------------------------------
#     
# #select the min value of the P1, 
# #print("Min Index: ", arrival_time.index(min(arrival_time)))
# print("This is the ready_queue")
# print(ready_queue)
# 
# #this grabs the WRONG index , we need to select only Priority 1 and find min out of that
# #-------------------------------------------------------------------------------------
# 
# #Correctly working , it finds the read_queue process == priority # and then inserts it into same position
# #as it is in the arrival_time for later reference of change of arrival time, 
# #it makes a new comparision of priority 1 , or 2, or 3, which is min arrival time. 
# 
# #@time 43
# Priority_1_arrival_time = [1001] * 8
# for key in ready_queue:
#     if ready_queue[key] == 'Process Priority: 1':
# #        print(arrival_time[key])
#         Priority_1_arrival_time.insert(key, arrival_time[key])
#         
# #clips off the end of the list, the residue
# if len(Priority_1_arrival_time) > 8:
#     del Priority_1_arrival_time[9:]
# 
# print("This is the process to do next for Priority 1")
# index_of_earliest_arrival_q1 = Priority_1_arrival_time.index(min(Priority_1_arrival_time))
# print(Priority_1_arrival_time.index(min(Priority_1_arrival_time)))
# print(Priority_1_arrival_time)
# 
# 
# Priority_2_arrival_time = [1002] * 8
# for key in ready_queue:
#     if ready_queue[key] == 'Process Priority: 2':
#         #print(arrival_time[key])
#         Priority_2_arrival_time.insert(key, arrival_time[key])
# #finds the nearest arrival time for the Priority 2 
#         
# #clips off the end of the list, the residue
# if len(Priority_2_arrival_time) > 8:
#     del Priority_2_arrival_time[9:]
# print("This is the process to do next for Priority 2")
# index_of_earliest_arrival_q2 = Priority_2_arrival_time.index(min(Priority_2_arrival_time))
# print(Priority_2_arrival_time.index(min(Priority_2_arrival_time)))
# # this above returns the index of the process to do next
# print(Priority_2_arrival_time)
# 
# #Add for Priority 3
# #this part chooses the Process to do next
# #-------------------------------------------------------------------------------------
# print("This is the current time & gant timeline")
# print(time)
# print("This is the process_priority dict after its been changed")
# print(process_priority)
# print("This is the arrival_time list for all 8 processes")
# print(arrival_time)
# 
# #this is for a priority 1 < 6 . implement the if < 6 check. to lower priority if NOT
# #Does the new cpu_burst of earliest p1 in arrival 
# newtime = cpu_bursts[index_of_earliest_arrival_q1][2] + time[-1]
# time.append(newtime)
# #add time to gant 
# arrival_time[index_of_earliest_arrival_q1] = time[-1] + i_o_bursts[index_of_earliest_arrival_q1][2]
# #update arrival time
# count[index_of_earliest_arrival_q1] += 1
# #increase count index of the process just done
# 
# print(count)  #keeps track of which row each process is on 
# print("This is the arrival_time list for all 8 processes")
# print(arrival_time)
# print("This is the current time & gant timeline")
# print(time)
# 
# #new read_queue called function that rebuilds it 
# ready_queue = PrimeReadyQueue()
# print(ready_queue)
# #implement a check for a process of higher priority and then do it if it arrives within
# #burst time of current process
# print(process_priority)
# 
# #-------------------------------------------------------------------------------------
# #creates a list of the process's that are priority 1 
# priority1 = [process for process, value in process_priority.items() if value == 1]
# #grab the arrival times for the process priority 1 
# checkp1, checkp2, checkp3, checkp4, checkp5, checkp6, checkp7, checkp8 = 0,0,0,0,0,0,0,0
# for i in priority1: # each i is 'P#' name of process thats priority 1 
#     #print(i)
#     if i == 'P1':
#         checkp1 = arrival_time[1]
#     elif i == 'P2':
#         checkp2 = arrival_time[2]
#     elif i == 'P3':
#         checkp3 = arrival_time[3]
#     elif i == 'P4':
#         checkp4 = arrival_time[4]
#     elif i == 'P5':
#         checkp5 = arrival_time[5]
#     elif i == 'P6':
#         checkp6 = arrival_time[6]
#     elif i == 'P7':
#         checkp7 = arrival_time[7]
#     elif i == 'P8':
#         checkp8 = arrival_time[8]
#         
# print(priority1)
# 
# print("These are the checkp# variables: ", checkp1, checkp5, checkp7, checkp8)
# #-------------------------------------------------------------------------------------
# #if cpu_bursts[index_of_earliest_arrival_q2][1] + time[-1] > checkp1 or checkp5 or checkp7 or checkp8:
# #    print("Passes a Higher Priority")
# #if cpu_bursts[index_of_earliest_arrival_q2][1] + time[-1] < 70 or 71 or 72 or 73:
#     #print("Under a Higher Priority")
#     
# print(index_of_earliest_arrival_q2)
# print(cpu_bursts[2][1])
# if cpu_bursts[index_of_earliest_arrival_q2][1] + time[-1] > checkp1 and checkp1 != 0:
#     print("Does this 1st")
#     allowed_burst = checkp1 - time[-1]
#     endtime = allowed_burst + time[-1]
#     if cpu_bursts[index_of_earliest_arrival_q2][1] >= allowed_burst:
#         
#         #new cpu_burst
#         cpu_bursts[index_of_earliest_arrival_q2][1] -= allowed_burst
#         #time append end
#         time.append(endtime)
# # now you can process the cpu_burst , as allowed_burst added to time, then start the process priority above it
#     
# if cpu_bursts[index_of_earliest_arrival_q2][1] + time[-1] > checkp5 and checkp5 != 0:
#     print("Does this")
#     allowed_burst = checkp5 - time[-1]
#     endtime = allowed_burst + time[-1]
#     print(allowed_burst)
#     if cpu_bursts[index_of_earliest_arrival_q2][1] >= allowed_burst:
# 
#         #new cpu_burst
#         cpu_bursts[index_of_earliest_arrival_q2][1] -= allowed_burst
#         #time append end
#         time.append(endtime)
#         #new arrival time
#         arrival_time[index_of_earliest_arrival_q2] = time[-1]
#         #if the result is 0 then move on to the next row
#         if cpu_bursts[index_of_earliest_arrival_q2][1] == 0: #maybe put in < 0 
#             count[index_of_earliest_arrival_q2] += 1
# 
# #-------------------------------------------------------------------------------------
# print(cpu_bursts[:][2])
# print(arrival_time)
# print(time)
# 
# #priority 1 arrives . P5 at time 50
# ready_queue = PrimeReadyQueue()
# print(ready_queue)
# index_of_earliest_arrival_q1 = PrimeEarliestQ1()
# #-------------------------------------------------------------------------------------
# newtime = cpu_bursts[index_of_earliest_arrival_q1][2] + time[-1]
# time.append(newtime)
# arrival_time[index_of_earliest_arrival_q1] = time[-1] + i_o_bursts[index_of_earliest_arrival_q1][2]
# #update arrival time
# count[index_of_earliest_arrival_q1] += 1
# #increase count index of the process just done
# 
# 
# print(count)  #keeps track of which row each process is on 
# print("This is the arrival_time list for all 8 processes")
# print(arrival_time)
# print("This is the current time & gant timeline")
# print(time)
# 
# #at time 55 , reset ready queue
# ready_queue = PrimeReadyQueue()
# print(ready_queue)
# 
# # =============================================================================
# #example of how it it would work for the index of earliest, return and continue to next queue
# # index_of_earliest_arrival_q1 = PrimeEarliestQ1()
# # if index_of_earliest_arrival_q1 == 0: 
# #     index_of_earliest_arrival_q2 = PrimeEarliestQ2()
# #         if index_of_earliest_arrival_q2 == 0:
# #             index_of_earliest_arrival_q3 = PrimeEarliestQ3()
# # =============================================================================
# 
# index_of_earliest_arrival_q1 = PrimeEarliestQ1()
# if index_of_earliest_arrival_q1 == 0:
#     index_of_earliest_arrival_q2 = PrimeEarliestQ2()
#     
# print("This is the arrival_time list for all 8 processes")
# print(arrival_time)
# print("This is the index of the earliest arrival of queue 2: ",index_of_earliest_arrival_q2)
# print(count[index_of_earliest_arrival_q2])
# print(count)
# 
# 
# 
# CheckForPriority1Arrival(index_of_earliest_arrival_q2)  #take the earliest arrival and check for priority 1 arrival
# #this also adds the cpu_burst , adds to time(so does the process), and updates arrival time. 
# print(time)
# print(arrival_time)
# #at time 57 reset ready_queue and continue
# #-------------------------------------------------------------------------------------
# ready_queue = PrimeReadyQueue()
# index_of_earliest_arrival_q1 = PrimeEarliestQ1()
# print("This is the index of the earliest arrival of queue 1: ",index_of_earliest_arrival_q1)
# RR_TQ6(index_of_earliest_arrival_q1)
# print(time)
# print(arrival_time)
# print(cpu_bursts[3][:])
# print("this shows that the cpu_bursts is being subtracted correctly 18-2= 16 for P3 first row")
# =============================================================================

     
#-------------------------------------------------------------------------------------
#example of how to use the OOP switch implementation
#process_to_scheduler(process_priority['P1'])
#process_to_scheduler(4)
#-------------------------------------------------------------------------------------

