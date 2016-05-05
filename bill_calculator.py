"""This program calculates the total bill and the split in a check """

def tip (bill_amount,percentage):
    tip = bill_amount * percentage *.01
    return tip

def total_bill(tip,bill_amount):
    total_bill = (bill_amount + tip)
    return total_bill

def split(total_bill,people):
    split = total_bill/people
    return split

def main():
    print "Hello, This is your Bill Calculator. Please choose one option "
    print "1 - Calculate tip"
    print "2 - Split the bill"
    user_choice = int(raw_input())

    if user_choice == 1:
        bill_amount = int(raw_input("How much was your bill: "))
        tip_percentage = int(raw_input("What percentage tip: "))
        tip_total = tip(bill_amount,tip_percentage)
        bill_total = total_bill(tip_total,bill_amount)
        print "The tip is %i." %(tip_total)
        print "The bill total is %i." %(bill_total)
        print "Would you like the bill split, Y/N: "
        ask_split = raw_input()
        if ask_split.upper() == "Y":
            split_number = int(raw_input("How many ways would you like to split the check: "))
            split_total = split(bill_total,split_number)
            print "The bill is %f for each person." %(split_total)
    elif user_choice == 2:
        bill_amount = int(raw_input("How much was your bill? "))
        split_number = int(raw_input("How many ways would you like to split the check: "))
        split_total = split(bill_amount,split_number)
        print "The bill is %i. for each person." %(split_total)


if __name__ == '__main__':
   main()  