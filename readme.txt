For this project there are two main files.
One of them is doing the core functionality where there is only a main 
function and all of them are being done sequentially with a bunch of 
if statements.
For the second and with the advice of Doctor Baris, i modified the code
to create a multithreading code where the left sensor and the right sensor
are funtioning at the same time, there is a critical section on the middle 
of the code that will acquire a lock whenever they want to access to the 
CS.

To be honest this code works only for a single sensor, on the left i can 
sense and record as usual, on the right i have some problems sensing when 
there is a multithread.
The core theme of our project is multithreads and locking a limited 
resource (such as the rotor + the camera)
I have mentioned all the resources i have used, most of the code was written
from scratch but some of them are borrowed from tutorials.
