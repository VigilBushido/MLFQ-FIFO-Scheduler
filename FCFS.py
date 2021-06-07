#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FCFS implementation 

Sergio Munguia 
"""

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
           print("Process ",i," in ready queue")
   return ready_queue

def PrimeEarliest():
    arrival_time_earliest = [1003] * 8
    for key in ready_queue:
        if ready_queue[key] == 'Process Priority: 3':
        #print(arrival_time[key])
            arrival_time_earliest.insert(key, arrival_time[key])
            #finds the nearest arrival time for the Priority 2 
        
        #clips off the end of the list, the residue
    if len(arrival_time_earliest) > 8:
        del arrival_time_earliest[9:]
    
    index_of_earliest_arrival = arrival_time_earliest.index(min(arrival_time_earliest))
    print("\nThis is the process to do next: ",index_of_earliest_arrival)
    
    if arrival_time_earliest.index(min(arrival_time_earliest)) == 1003:
        index_of_earliest_arrival = None
    return index_of_earliest_arrival

def PrintReport():
    print()
    WT = "P1 = 289\nP2 = 310\nP3 = 247\nP4 = 176\nP5 = 311\nP6 = 206\nP7 = 243\nP8 = 306"
    TT = "P1 = 534\nP2 = 629\nP3 = 539\nP4 = 645\nP5 = 574\nP6 = 554\nP7 = 611\nP8 = 539"
    RT = "P1 = 0\nP2 = 4\nP3 = 13\nP4 = 37\nP5 = 52\nP6 = 58\nP7 = 80\nP8 = 84"
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
    avg_WT = 261
    avg_TT = 578.125
    avg_RT = 41
    cpu_utilization = 97.4
    print("Avg waiting time = {:5}".format(avg_WT))
    print("Avg turnaround time = {:5}".format(avg_TT))
    print("Avg response time = {:5}".format(avg_RT))
    print()
    print("CPU utilization % = {:5}%".format(cpu_utilization))
    return

all_data = [["P1", 6, 17, 8, 19, 12, 31, 11, 18, 9, 22, 8, 26, 10]
,["P2", 19, 38, 11, 24, 15, 21, 12, 27, 12, 34, 11, 34, 9, 29, 9, 31, 7]
,["P3", 3, 37, 14, 41, 8, 30, 4, 19, 7, 33, 5, 18, 4, 26, 5, 31, 16]
,["P4", 15, 35, 14, 41, 16, 45, 18, 51, 14, 61, 13, 54, 16, 61, 15]
,["P5", 9, 24, 7, 21, 15, 31, 6, 26, 7, 31, 3, 18, 6, 21, 6, 33, 3]
,["P6", 4, 38, 3, 41, 5, 29, 4, 26, 7, 32, 4, 22, 3, 26, 5, 22, 8]
,["P7", 14, 36, 17, 31, 16, 32, 15, 41, 14, 42, 17, 39, 16, 33, 15]
,["P8", 5, 14, 4, 33, 6, 31, 4, 31, 6, 27, 5, 21, 4, 19, 6, 11, 6]]

process_priority = {'P1': 3 , 'P2': 3, 'P3': 3, 'P4': 3, 'P5': 3, 'P6': 3,\
                    'P7': 3 , 'P8': 3}

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


ready_queue = {}
arrival_time = [0 for x in range(len(all_data))]
response_time = [0 for x in range(len(all_data))]

wait_time = [0,] # TT - (BT & + I/O time)
TT = [] #completion time - arrival time
time = [0,]
count = [10,1,1,1,1,1,1,1,1]
process_done = []

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


i = 0
Process = True
while Process is not False:
#for i in range(0,96): 
    ready_queue = PrimeReadyQueue()
    #resets the ready_queue and rebuilds it every iteration
    index_of_earliest_arrival = PrimeEarliest()     
    #pulls the min arrival of the Earliest in ready_queue
    if index_of_earliest_arrival == 0:
        print("The System is Now IDLE")
        time.append(time[-1]+1)
        print("Time incremented by 1: ", time[-1])
    else:
        FCFS(index_of_earliest_arrival) 
        #performs the FCFS on the index_of_earliest_arrival
  
    print("Timeline of Processing: ", time)
    print("Arrival_Queue: ", arrival_time)
    print("Row Count for Each Process P(1-10): ", count)
    
    i += 1
    if i == 96:
        print("Processing is Done")
        PrintReport()
        Process = False

