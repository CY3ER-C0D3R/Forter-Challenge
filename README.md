# Forter-Challenge
Count number of unique names in a transaction

## Getting Started

After cloning the repository, run the file named unit_tests.py.  
Preferably, run via the command prompt. Works also in any python IDE.

### Installing and Running
 
The Function `def countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard)` is the main function being tested in this program and can be found in the count_unique_names.py file.  
Make sure all three files are in the same directory. Then, run unit_test.py. 

Output should be as following:

```
Welcome to my countUniqueNames function!
This function counts the number of unique names in a transaction.
Press any key to continue...
```

After pressing any key, the following screen should appear:

```
Options (enter a number from the list bellow):
  1) Run Unit Tests (Automatically)
  2) Run Unit Test (Manual)
  3) Change Max Number Of Typos
  4) Print the current Max Number Of Typos
  5) Help
  6) Clear Screen
  7) Exit

>
```

To run a manual unit test press 2 and enter the transaction information.  
To run a pre-written unit test press 1.  
*Advice: Run the pre-written unit test first*.  

Output should be something of the sort:

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
***********************************************************************
                Should count perfectly equal unique names
***********************************************************************
Running new Test with parameters:
billFirstName = Deborah
billLastName = Egli
shipFirstName = Deborah
shipLastName = Egli
billNameOnCard = Deborah Egli
Num of unique people found in transaction: 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*****************************************************************
```

## Running the tests

Use the options menu to change the max number of allowed typos.  
Enter different information and get different outputs.  
Also, check if automatic unit test gave the desired output.

## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/) - The IDE used

## Authors

* **Yuval Stein** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Thanks to Dan Connor for the nickname list - see original [here](https://github.com/onyxrev/common_nickname_csv).


