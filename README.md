# oop_Ex1
# oop_Ex1

the problem:
number of people that want to use at number of elevators in one building.
everyone has the possibility to up and down from each floor and for each floor.
our goal is reduce the waiting time to minimal time from the moment that the person call to the elevator until he arrived to his destination.
בעית שיבוץ המעליו ת
הבעיה: מספר אנשים שרוצים להשתמש במספר מוסים של מעליות באותו הבניין לפני כל אדם עומדת האפשרות לעלות ולרדת בכל רחבי הבניין. 
מטרתנו לצמצם את זמן ההמתנה של כל אדם לזמן המינמאלי ביותר מרגע שבו הוא קורא למעלית עד הגעו לקומת היעד.

we assume that everyone can arrived from every floor, and call the elevator from every floor in the building.
אנחנו יוצאים נקודת הנחה שבן אדם יכול להגיע לכל קומה בבנין,ולקרוא למעלית מכל קומה בבנין  
In our algorithm we were help by the next articles:
בקוד עצמ ונעזרנו במקורות הבאים:

algorithm offline: In this method we get the data in advanced, therfore this method is over effective because the algorithm designed so that the calls be executed at the Highly effective way.
algorithm oמline: In this method we get the data at runtime, and the algorithm need to send the appropriate elevator in this moment.

we suggest offline algorithm solution, so we get all the data in advanced.
אנחנו נציע פתרון אופליון כלומר 
we create a list of all the elevators of the building, the function run over the list and check the speed of all elevator.
we deviced the number of calls in proportionately, so that the fastes elevator get the most number of calls, the slowest elevator get the low number of calls and relatively all other elevators.
we accept to get for every call the minimal execution time.

algorithm offline: ניצור רשימה של כל מעליות הבניין, נרוץ על הרשימה ונבדוק את המהירות של כל מעלית.
נחלק את מספר הקריאות באופן יחסי, כך שהמעלית המהירה ביותר תקבל מספר רב של קריאות, המעלית האיטית ביותר תקבל את מספר הקריאות הקטן ביותר וכך כל שאר המעליות בפרופורציה. 
נצפה לקבל עבור כל קריאה את הזמן המינימלי ביותר.


