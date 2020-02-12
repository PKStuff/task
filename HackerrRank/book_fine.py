import datetime
def func(d1,m1,y1,d2,m2,y2):
    fine = 0
    returned_date = datetime.datetime(y1,m1,d1)
    due_date = datetime.datetime(y2,m2,d2)
    if due_date >= returned_date:
        fine = 0
    else:
        if int(returned_date.strftime("%m")) == int(due_date.strftime("%m")) and int(returned_date.strftime("%y")) == int(due_date.strftime("%y")):
            fine = 15 * (int(returned_date.strftime("%d")) - int(due_date.strftime("%d")))
        elif int(returned_date.strftime("%y")) == int(due_date.strftime("%y")):
            fine = 500 * (int(returned_date.strftime("%m")) - int(due_date.strftime("%m")))
        else:
            fine = 10000
    return fine

fine = func(9, 6, 2015, 6, 6, 2015)
print(fine)
