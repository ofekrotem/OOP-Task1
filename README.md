
# OOP - Task 1


## Authors

- Ofek Rotem - 209132687
- Yonatan Tal - 314666611



## Internet search

In order to understand the problem’s expanse and the possible solution methods, we have searched the internet and found a number of projects and videos that provide solutions:

- https://www.youtube.com/watch?v=JXqVvmBOyyQ       
This video explains the “decency and starvation”. Meaning, taking care of the requests according to their incoming time, taking under consideration the max and min floor in the fastest time. Therefore the idea of one direction elevators was suggested, this idea prevents starvation and maintains decency.

- https://www.youtube.com/watch?v=siqiJAJWUVg&t=568s  
This video explains the principle of “distribution to areas”. That means, for each elevator there are allocated certain floors that are the only ones it can receive calls from(it can arrive to all floors in the building). This principal preserves the decency and gives equal attention to all floors. In this situation,to each area will belong a “fast” elevator and a “slow” elevator, according to the distance of the source floor from the source floor.

- https://www.geeksforgeeks.org/fcfs-disk-scheduling-algorithms
In this site, an algorithm is suggested - "FCFS - First Come First Serve". In this algorithm, the algorithm will allocate an elevator according to the order of the incoming calls. However, this algorithm may shorten the time it takes for each passenger to complete it’s ride, but will significantly extend the waiting time for an elevator.




## Our offline algorithm
Our algorithm allocates a fare distribution of calls to each elevator depending on its speed. Meaning, an elevator with faster speed will be assigned more calls then a slower elevator.



## UML diagram
![image](https://user-images.githubusercontent.com/92383710/142611251-1b3ae374-4f32-4712-aa52-7cca6e7ad2e7.png)


## Test results

- Building 1, Calls a - Total waiting time: 11292.0,  average waiting time per call: 112.92,  unCompleted calls,0,  certificate, -274168397
- Building 1 , Calls b - Total waiting time: 1784243.6402240375,  average waiting time per call: 1784.2436402240376,  unCompleted calls,963,  certificate, -4322277396
- Building 1 , Calls c - Total waiting time: 1839360.3121899734,  average waiting time per call: 1839.3603121899735,  unCompleted calls,958,  certificate, -4659886686
- Building 1 , Calls d - Total waiting time: 1841698.4976999543,  average waiting time per call: 1841.6984976999543,  unCompleted calls,950,  certificate, -4711953150
- Building 2 , Calls a - Total waiting time: 4622.0,  average waiting time per call: 46.22,  unCompleted calls,0,  certificate, -237838967
- Building 2 , Calls b - Total waiting time: 1783199.6402240375,  average waiting time per call: 1783.1996402240375,  unCompleted calls,963,  certificate, -4321511087
- Building 2 , Calls c - Total waiting time: 1838027.3121899734,  average waiting time per call: 1838.0273121899734,  unCompleted calls,958,  certificate, -4648683979
- Building 2 , Calls d - Total waiting time: 1840413.4976999543,  average waiting time per call: 1840.4134976999544,  unCompleted calls,950,  certificate, -4707573839
- Building 3 , Calls a - Total waiting time: 3305.0,  average waiting time per call: 33.05,  unCompleted calls,0,  certificate, -26225136
- Building 3 , Calls b - Total waiting time: 540795.4193599995,  average waiting time per call: 540.7954193599995,  unCompleted calls,195,  certificate, -1757670340
- Building 3 , Calls c - Total waiting time: 581182.0161200064,  average waiting time per call: 581.1820161200064,  unCompleted calls,184,  certificate, -1886246689
- Building 3 , Calls d - Total waiting time: 539289.7960180034,  average waiting time per call: 539.2897960180034,  unCompleted calls,123,  certificate, -1770445577
- Building 4 , Calls a - Total waiting time: 2065.0,  average waiting time per call: 20.65,  unCompleted calls,0,  certificate, -54990177
- Building 4 , Calls b - Total waiting time: 212655.98924799968,  average waiting time per call: 212.65598924799968,  unCompleted calls,26,  certificate, -754555066
- Building 4 , Calls c - Total waiting time: 209858.52243999997,  average waiting time per call: 209.85852243999997,  unCompleted calls,8,  certificate, -744370538
- Building 4 , Calls d - Total waiting time: 217476.56048999997,  average waiting time per call: 217.47656048999997,  unCompleted calls,15,  certificate, -737173200
- Building 5 , Calls a - Total waiting time: 1695.0,  average waiting time per call: 16.95,  unCompleted calls,0,  certificate, -68277037
- Building 5 , Calls b - Total waiting time: 47693.038048,  average waiting time per call: 47.693038048000005,  unCompleted calls,1,  certificate, -251024353
- Building 5 , Calls c - Total waiting time: 46140.0,  average waiting time per call: 46.14,  unCompleted calls,0,  certificate, -237838967
- Building 5 , Calls d - Total waiting time: 46573.0,  average waiting time per call: 46.573,  unCompleted calls,0,  certificate, -237838967

