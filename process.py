"""
NO FUNCTIONS SHOULD BE ADDED OR REMOVED FROM THIS MODULE. SIMPLY COMPLETE EACH FUNCTION AS DESCRIBED.
YOU SHOULD ALSO NOT REMOVE ANY OF THE COMMENTS OR CHANGE THE STRUCTURE IN ANY WAY OTHER THAN AS INSTRUCTED.

This module is responsible for processing the data.
"""
import tui


def execute(action, headings, records):
    """
    Task 17: Execute process action

    The function should check the value of action (which is the process menu option specified by the user)
    and execute the relevant process function.
    For example,
        If action is 1 then the function should invoke the record_by_id function.
        If action is 2 then the function should invoke the records_by_customers function.

    In each case, the result of executing relevant process function should be displayed using the appropriate tui
    function.
    For example,
        The result of executing the record_by_id function should be displayed using the tui display_record function.
        The result of executing the records_by_shipment_mode function should be displayed using the tui display_groups
        function

    If the action is invalid then the error message 'Invalid selection.' should be displayed using the tui error
    function.

    :param action: An integer indicating which action (process option) to perform.
    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: Does not return anything.
    """
    # TODO: Your code here (replace this TODO and remove the keyword pass)
    if action == 1:
        user_input = record_by_id(headings, records)
    elif action == 2:
        user_input= records_by_customers(headings, records)
    elif action == 3:
        user_input = records_by_shipment_mode(headings, records)
    elif action == 4:
        user_input = records_summary(headings, records)
    else:
        user_input = "invalid selection"
    print(user_input)


def record_by_id(headings, records):
    """
    Task 18: Retrieve a record by a record id.

    The function should use the appropriate tui function to retrieve a record id.
    The function should then find the record with a matching record id and return the record.
    The parameter 'records' contains the records that are to be searched.

    For higher marks (advance task):
        - The function should create a list of valid ids. These are ids for which a record exists in the 'records' list.
        - The function should pass the list of valid ids to the tui function when retrieving a record id

    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: An individual record with the specified record id.
    """
    # TODO: Your code here (replace this TODO and remove the keyword pass)
    id = tui.record_id()
    data = []
    for record in records:

        if int(record[0]) == id:
            data.append(record)
    return data



def records_by_customers(headings, records):
    """
    Task 19: Retrieve records for specified customers.

    The function should use the appropriate function in tui to retrieve a list of customer ids.
    The function should return a list containing records where the customer id matches one of the customer ids
    specified by th user.
    The parameter 'records' contains the list of records that are to be searched.


    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: A list of records where a record contains a specified customer id.
    """
    # TODO: Your code here (replace this TODO and remove the keyword pass)
    user = tui.customers()
    print(user)
    user_input = []
    for record in records:
        if record[5] in user:
            user_input.append(record)
    return user_input



def records_by_shipment_mode(headings, records):
    """
    Task 20: Retrieve records grouped by shipment mode.

    The function should return a dictionary where the keys are the different shipment modes and the values are a list
    of records for each shipment mode.

    For example, the key could be 'Standard Class' and the value for this key would be a list of records where
    the shipment mode is 'Standard Class'.

    For higher marks (advance task):
        - The function should retrieve a sample size from the user by invoking the tui sample_size function.
        The default size for the function should be the number of records in (parameter) 'records'.
        - The function should use the sample size to control how many records are added to each group.
        - For example, if the sample size is 5 then only 5 records should be added to each shipment mode group.

    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: A dictionary with shipment mode as the keys and a list of records for each shipment mode as the values.
    """
    # TODO: Your code here (replace this TODO and remove the keyword pass)
    shipment_lt = []
    shipment_md = {}
    for record in records:
        md = record[4]
        if md not in shipment_lt:
            shipment_lt.append(md)
            shipment_md[md] = []
            shipment_md[md].append(record)
            return shipment_md




def records_summary(headings, records):
    """
    Task 21: Retrieve a sales summary for each state.

    The function should return a dictionary where the keys are the states and the values are nested dictionaries
    containing sales, quantity, discount and profit totals.

    The structure of the dictionary should be as follows:
    state: { 'sales': total_sales, 'quantity': total_quantity, 'discount': total_discount, 'profit': total_profit }

    E.g. New York: {'sales': 215336.16, 'quantity': 2935, 'discount': 44.4, 'profit': 50887.75}

    Where total_sales, total_quantity, total_discount and total_profit are the totals for the state.

    For higher marks (advance task):
        - The final totals for sales, quantity, discount and profit for each state should be rounded
        to 2 decimal places.

    :param headings: A list of headings for the records.
    :param records: A list of records.
    :return: A dictionary where the keys are the names of the states and the values are dictionaries containing
    the totals for sales, quantity, discount and profit.
    """
    # TODO: Your code here (replace this TODO and remove the keyword pass)
    state_list = []
    sales_states = {}
    state_index = headings.index('State')
    sales_index = headings.index('Sales')
    qty_index = headings.index('Quantity')
    profit_index = headings.index('Profit')
    dis_index = headings.index('Discount')
    for record in records:
        state = record[state_index]
        if state not in state_list:
            state_list.append(state)
            sales_states[state] = {'sales': 0, 'quantity': 0, 'discount': 0, 'profit': 0}
        sales_states[state]['sales'] = round(sales_states[state]['sales'] + float(record[sales_index]), 2)
        sales_states[state]['quantity'] = round(sales_states[state]['quantity'] + float(record[qty_index]), 2)
        sales_states[state]['discount'] = round(sales_states[state]['discount'] + float(record[dis_index]), 2)
        sales_states[state]['profit'] = round(sales_states[state]['profit'] + float(record[profit_index]), 2)
    return sales_states
