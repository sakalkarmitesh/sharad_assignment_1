"""A teacher is conducting a camp for a group of five children. Based on their performance and behavior during the camp, the teacher rewards them with chocolates.

Write a Python function to
1. Find the total number of chocolates received by all the children put together. Assume that each child is identified by an id and it is stored in a tuple and the number of chocolates given to each child is stored in a list.
2. The teacher also rewards a child with few extra chocolates for his/her best conduct during the camp.
    If the number of extra chocolates is less than 1, an error message "Extra chocolates is less than 1", should be displayed.
    If the given child Id is invalid, an error message "Child id is invalid" should be displayed. Otherwise, the extra chocolates provided for the child must be added to his/her existing number of chocolates and display the list containing the total number of chocolates received by each child.
"""
child_ids = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]
def calculate_total_chocolates(chocolates_received):
    total_chocolates = 0
    for chocolates in chocolates_received:
        total_chocolates += chocolates
    return total_chocolates

def reward_child(child_id, extra_chocolates, child_ids, chocolates_received):
    if extra_chocolates < 1:
        print("Extra chocolates is less than 1")
    elif child_id not in child_ids:
        print("Child id is invalid")
    else:
        chocolates_received[child_ids.index(child_id)] += extra_chocolates
        print(chocolates_received)


print(calculate_total_chocolates(chocolates_received))

reward_child(20, 2, child_ids, chocolates_received)