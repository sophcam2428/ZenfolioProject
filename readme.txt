Instructions:

This project was written in python3, I used Pycharm IDE but it can also run form the terminal.

Steps to run project from the terminal:

1)	Clone the project from this repo.
2)	Step into ZenfolioProject folder.
3)	To run the program execute the following command: Python3 CodingProject.py
4)	To run unittests execute the following command: 
python3 -m unittest discover /path/to/ZenfolioProject


Notes and assumptions:

1) In the function handle_numeric I use the sorted method that uses Timesort algorithm which is a hybrid algorithm of merge sort and insertion sort that is design to handle real world data.
The average performance if this algorithm is O(nlogn).
The Worst case space is O(n).
2) Optional specs: 
	a) add the ability to handle negative and decimal numbers - done.
	b) add the ability to handle special characters and case sensitivity - I assumed that you      meant:
		I) The ability to count special characters as well as alphabetical ones – I assumed that space is not considered as a special character, theoretically I could consider it since it has an ASCII value but it didn’t feel right.
		II) Case sensitivity – sum up capital and non-capital together,
		If those assumptions are current then it is done as well.




