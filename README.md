# SevenSegmentsDisplay

Running

<pre>
python sevensegments.py

The 7 segments display.

Enter the size of the display: 3
Enter the numbers that you want display (comma separated: 1,2,3): 0,1,2,3,4,5,6,7,8,9

 ---       ---  ---       ---  ---  ---  ---  --- 
|   |    |    |    ||   ||    |        ||   ||   |
           ---  ---  ---  ---  ---       ---  --- 
|   |    ||        |    |    ||   |    ||   |    |
 ---       ---  ---       ---  ---       ---  --- 
</pre>

To run all the tests use this command in the directory

<pre>
python -m unittest discover -s . -p 'test*.py'
</pre>
