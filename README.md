# oop_Ex1
# oop_Ex1



the problem:
number of people that want to use at number of elevators in one building.
everyone has the possibility to up and down from each floor and for each floor.
our goal is reduce the waiting time to minimal time from the moment that the person call to the elevator until he arrived to his destination.


we assume that everyone can arrived from every floor, and call the elevator from every floor in the building.


In our algorithm we were help by the next articles:
http://www.intertent.co.il/2011/07/elevator-algorithm.html
http://cs.huji.ac.il/~ai/projects/2014/The_intelevator/files/report.pdf
https://studylib.net/doc/7878746/on-line-algorithms-versus-off-line-algorithms-for-the-ele

algorithm offline: In this method we get the data in advanced, therfore this method is over effective because the algorithm designed so that the calls be executed at the Highly effective way.
algorithm oמline: In this method we get the data at runtime, and the algorithm need to send the appropriate elevator in this moment.

we suggest offline algorithm solution, so we get all the data in advanced.
 
algorithm offline: we create a list of all the elevators of the building, the function run over the list and check the speed of all elevator.
we deviced the number of calls in proportionately, so that the fastes elevator get the most number of calls, the slowest elevator get the low number of calls and relatively all other elevators.
we expect to get for every call the minimal execution time.




