
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

![UML](https://ibb.co/nkJS4wQ)


