"""
NO FUNCTIONS SHOULD BE ADDED OR REMOVED FROM THIS MODULE. SIMPLY COMPLETE EACH FUNCTION AS DESCRIBED.
YOU SHOULD ALSO NOT REMOVE ANY OF THE COMMENTS OR CHANGE THE STRUCTURE IN ANY WAY OTHER THAN AS INSTRUCTED.

This module is responsible for visualising the data retrieved from a database using Matplotlib.
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import database


def execute(action, headings, records):
    """
    Task 28: Execute database action.

    The function should check the value of action (which is the visual menu option specified by the user)
    and execute the relevant database function.
    For example,
        If action is 1 then the function should invoke the static_summary function.
        If action is 2 then the function should invoke the animated_summary function.

    In each case, matplotlib should be used to produce the visualisation.

    If the action is invalid then the error message 'Invalid selection.' should be displayed using the tui error
    function.

    :param action: An integer indicating which action (visual option) to perform.
    :return: Does not return anything.
    """
    # TODO: Your code here (replace this TODO and remove the keyword pass)
    pass


def static_summary():
    """
    Task 29: Display a static visualisation.

    The function should display the total sales for each product
    The visualisation should show the name of the product and the number of sales for that product.
    There may be many products so a suitable approach should be taken to ensure that the visualisation is
    meaningful and clear.

    :return: Does not return anything.
    """
    # TODO: Your code here (replace this TODO and remove the keyword pass)
    pass


def animated_summary():
    """
    Task 30: Display an animated visualisation.

    The function should display an animated summary of the top 3 product sub-categories for a range of dates.
    The dates will be supplied by the user.
    The visualisation will show in ascending date order how the sales for the top 3 sub-categories varies from one
    date to another.

    For higher marks (advance task):
        - The visualisation will include multiple subplots

    For even higher marks (advance task):
        - The visualisation will handle a large number of dates by showing a 'sliding window' animation.
        For example, if the user enters 20 dates and the animation only shows 10 dates at a time then
        the animation for the first 10 dates will be shown first.  Each new date after that will be added
        to the animation by removing the earliest date and then adding the new date to the end so as to
        create a 'sliding window' effect.

    :return: Does not return anything.
    """
    # TODO: Your code here (replace this TODO and remove the keyword pass)
    pass