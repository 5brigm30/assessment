"""
THIS MODULE SHOULD NOT BE MODIFIED.

This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, querying of the database and for visualising information.

"""

# Import required modules
import tui
import file
import process
import database
import visual


def run():
    # Display a greeting
    tui.greeting()

    # Display the path to the sales data file
    tui.status(f'Data file is located at: {file.file_path()}')

    # Load the data.
    tui.status('Loading data from file', 0)
    headings, sales_records = file.load_data()
    tui.status('Finished loading data from file', 100)

    # Display how many records have been loaded
    tui.total_records(len(sales_records))

    while True:
        # Display a menu of options
        option = tui.main_menu()

        # Check if the user entered a valid option
        if option == -1:
            continue
        # Check if the user wishes to exit the program
        elif option == 4:
            tui.status('Exiting...')
            break
        # Handle selected option
        else:
             [process, database, visual, file][option - 1].execute(tui.sub_menu(option), headings, sales_records)


if __name__ == "__main__":
    run()
