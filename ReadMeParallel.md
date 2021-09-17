Report

The problems that i enconter while doing the assignment was that I was not sure where to put the pymp.Parallel(). 
I tried in the inner loop but it never finished the process. I overcame the problem by putting the pymp.Parallel() in the outer loop.
This assignment took me 3 hours to finish.
I did a change to my original file, converting it into a parellel program with the pymp library.
The following are the results for each runnung test with differents threads:

 
1 thread
Test 9
444444444
444444444
444444444
444444444
444444444
444444444
444444444
444444444
444444444
Elapsed Time: 2.244999266999912 Seconds
Averaged Time per test: 2.5521168314000535

2 threads
Test 9
444444444
444444444
444444444
444444444
444444444
444444444
444444444
444444444
444444444
Elapsed Time: 2.4718823519997386 Seconds
Averaged Time per test: 2.444343911999931

4 threads
Test 9
444444444
444444444
444444444
444444444
444444444
444444444
444444444
444444444
444444444
Elapsed Time: 3.8441474819996984 Seconds
Averaged Time per test: 3.971191839099947

8 threads
Test 9
444444444
444444444
444444444
444444444
444444444
444444444
444444444
444444444
444444444
Elapsed Time: 9.244383349000145 Seconds
Averaged Time per test: 7.8544532372999125

In conlusion with more amount of threads my program took longer times to accomplish because it had to update the multiple threads and that is time consuming.
I could not run my program at first from my VM but I noticed I was using python 2 and with python 3 it ran properly.

CPU INFO:
model name	: Intel(R) Core(TM) i7-4770HQ CPU @ 2.20GHz
      4      36     220
