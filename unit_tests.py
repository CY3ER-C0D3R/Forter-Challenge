from count_unique_names import countUniqueNames, get_max_num_of_typos, set_new_max_num_of_typos
import platform, os
import datetime


def print_menu():
    """

    :return: Function prints the main menu to screen
    """
    main_menu_text = "\n\rOptions (enter a number from the list bellow):\n\r" \
                     "  1) Run Unit Tests (Automatically)\n\r" \
                     "  2) Run Unit Test (Manual)\n\r" \
                     "  3) Change Max Number Of Typos\n\r" \
                     "  4) Print the current Max Number Of Typos\n\r" \
                     "  5) Help\n\r" \
                     "  6) Clear Screen\n\r" \
                     "  7) Exit\n\r"
    print main_menu_text


def clear_screen():
    """

    :return: clears the screen depending on the os
    """
    if platform.system() == "Windows":
        _ = os.system("cls")
    elif platform.system() == "Linux":
        _ = os.system('clear')


def print_help():
    """

    :return: prints a short help text to user
    """
    help_text = "\n\rChoose an option from the options menu (1-6).\n\r" \
                "Follow the instructions in order to run unit tests on the function.\n\r" \
                "Press 1 to run an automatic test run to check the function.\n\r" \
                "Press 6 or 'cls' to clear the screen.\n\r" \
                "Type 'help' to display main menu again.\n\r"
    print help_text


def run_test(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard):
    """

    :param billFirstName: string, the first name in the billing address form (could include middle names)
    :param billLastName: string, the last name in the billing address form
    :param shipFirstName: string, the first name in the shipping address form (could include middle names)
    :param shipLastName: string, the last name in the shipping address form
    :param billNameOnCard: string, the full name as it appears on the credit card
    :return: runs the countUniqueNames function and prints the number of unique people to screen
    """
    print 'Running new Test with parameters: '
    print 'billFirstName = %s' % billFirstName
    print 'billLastName = %s' % billLastName
    print 'shipFirstName = %s' % shipFirstName
    print 'shipLastName = %s' % shipLastName
    print 'billNameOnCard = %s' % billNameOnCard
    unique_people = countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard)
    print 'Num of unique people found in transaction: %d' % unique_people


def describe_unit_test(description):
    """

    :param description: string, some text to print out
    :return: Function used for pretty printing
    """
    print '***************' + '*' * len(description) + '***************'
    print '                ' + description + '                '
    print '***************' + '*' * len(description) + '***************'


def run_unit_tests():
    """

    :return: Function runs a full range of USE CASES tests on the function. All tests are pretty printed to screen.
    """
    print 'Run Unit Test? (y/n)',
    request = raw_input()
    if request == 'y':
        # test number 1
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        describe_unit_test('Should count perfectly equal unique names')
        run_test("Deborah", "Egli", "Deborah", "Egli", "Deborah Egli")  # should print 1
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        # test number 2
        describe_unit_test('Should count non-equal unique names')
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test('Michele', 'Egli', 'Deborah', 'Egli', 'Michele Egli')  # should print 2
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test('Michele', 'Egli', 'Deborah', 'Egli', 'Andy Egli')  # should print 3
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        # test number 3
        describe_unit_test('Should match nicknames')
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test('Deborah', 'Egli', 'Debbie', 'Egli', 'Debbie Egli')  # should print 1
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test('Andy', 'Egli', 'Andrew', 'Egli', 'Andy Egli')  # should print 1
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        # test number 4
        describe_unit_test('Should allow flipping of first and last names in non-explicit name field')
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test('Deborah', 'Egli', 'Deborah', 'Egli', 'Egli Deborah')  # should print 1
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        # test number 5
        describe_unit_test('Should accept minor typos')
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test('Deborah', 'Egni', 'Deborah', 'Egli', 'Deborah Egli')   # should print 1
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test('Mary', 'Egln', 'Maryd', 'Egli', 'Mar Egli')  # should print 1
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        # test number 6
        describe_unit_test('Should not accept significantly diverging names')
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test('Deborah', 'Edfi', 'Deborah', 'Egli', 'Deborah Egli')  # should print 2
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        # test number 7
        describe_unit_test('Should accept one unique middle name as equivalent to a missing middle name')
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test('Deborah S', 'Egli', 'Deborah', 'Egli', 'Deborah Egli')  # should print 1
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        describe_unit_test('Should not accept multiple differing middle names as equivalent to any other middle name')
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test('Deborah S', 'Egli', 'Deborah F', 'Egli', 'Deborah S Egli')  # should print 2
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test('Deborah S', 'Egli', 'Deborah F', 'Egli', 'Deborah G Egli')  # should print 3
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        # test number 8
        describe_unit_test('Original Assignment USE CASES')
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test("Deborah", "Egli", "Deborah", "Egli", "Deborah Egli")  # should print 1
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test("Deborah", "Egli", "Debbie", "Egli", "Debbie Egli")  # should print 1
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test("Deborah", "Egni", "Deborah", "Egli", "Deborah Egli")  # should print 1
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test("Deborah S", "Egli", "Deborah", "Egli", "Egli Deborah")  # should print 1
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test("Michele", "Egli", "Deborah", "Egli", "Michele Egli")  # should print 2
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        # test number 9
        describe_unit_test('Additions to Original Assignment USE CASES')
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test("Michele", "Egli", "Deborah", "Egli", "Michele Egfli")  # should print 2
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        run_test("Michele", "Egli", "Deborah", "Egli", "Egfli b Michele")  # should print 2
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print '**************************************************************************************'
        print ''*16 + 'Finished tests. Results should have been as following:' + ''*16
        print ''*16 + '        1,2,3,1,1,1,1,1,2,1,2,3,1,1,1,1,2,2,2         ' + ''*16
        print '**************************************************************************************\n\r'


def run_unit_test():
    """

    :return: Function is used to run a single test manually requested from the user. Pretty prints the test to screen.
    """
    print 'Enter values for the following fields:'
    print 'billFirstName = ',
    billFirstName = raw_input()
    print 'billLastName = ',
    billLastName = raw_input()
    print 'shipFirstName = ',
    shipFirstName = raw_input()
    print 'shipLastName = ',
    shipLastName = raw_input()
    print 'billNameOnCard = ',
    billNameOnCard = raw_input()
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    run_test(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard)
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'


def change_max():
    """

    :return: Function changes the MAX_NUM_OF_TYPOS for the countUniqueNames function.
    """
    print 'Enter new Max: ',
    request = raw_input()
    try:
        num = int(request)
        set_new_max_num_of_typos(num)
    except Exception as e:
        print e.message


def print_max():
    """

    :return: Function prints the the current MAX_NUM_OF_TYPOS allowed in the countUniqueNames function.
    """
    print 'Current Max number of allowed Typos is %d.' % get_max_num_of_typos()


def exit_program():
    """

    :return: Function exits the program if user says yes.
    """
    print 'Are you sure you want to exit? (y/n)',
    request = raw_input()
    if request == 'y':
        exit(0)


def main():
    """

    :return: Main loop for using the program. Gets requests from the user and runs them accordingly.
    """
    now = datetime.datetime.now()
    print now.strftime("%d/%m/%Y %H:%M") + "\t Program written by: Yuval Stein\n\r"
    print 'Welcome to my countUniqueNames function!'
    print 'This function counts the number of unique names in a transaction.'
    raw_input('Press any key to continue...')
    clear_screen()
    print_menu()
    while True:
        request = raw_input("> ")
        if request == 'h' or request == 'help' or request == "?":
            print_menu()
        elif request == '1':
            run_unit_tests()
        elif request == '2':
            run_unit_test()
        elif request == '3':
            change_max()
        elif request == '4':
            print_max()
        elif request == '5':
            print_help()
        elif request == '6' or request == 'cls':
            clear_screen()
        elif request == '7' or request == 'exit' or request == 'quit':
            exit_program()
        elif request == '':  # enter key pressed, ignore.
            continue
        else:  # none of the above options entered
            print 'Please Choose a valid option.'

if __name__ == "__main__":
    main()
