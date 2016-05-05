""" This program is a test for functions with 3 parameters"""

BILL = 100
TIP = 0
SPLIT = 0

def calculate_bill(bill,tip = 18,split = 1):
    total_bill = bill * tip *.01 / split
    return total_bill

def main():
    bill = 100
    print "The original bill is %i." %(bill)
    tip = 20
    print "The tip amount is %f." %(tip)
    total_amount = calculate_bill(bill,tip,2)
    print "The total bill is %f for each person." %(total_amount)


if __name__ == '__main__':
   main() 


