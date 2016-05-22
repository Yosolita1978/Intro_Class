
# def calculate_bil(string):
#     string = string.split(",")
#     for i in string:
#         item = string[0].split(":")[1]
#         quantity = float(string[1].split(":")[1])
#         price = float(string[2].split(":")[1])
#     return quantity * price 

# example = "item:apples,quantity:4,price:1.50"
# print calculate_bil(example)


def process_file():
    with open('/Users/cristina/Source/intro_class_cristina/class_grades.txt') as my_file:
        grade_list = []
        for line in my_file:
            grade = line.strip().replace("\xef\xbb\xbf", "")
            grade_list.append(grade)
        return grade_list

def convert_score(grade_list):
    class_grades_letters = []
    for score in grade_list:        
        grades_score = int(score)
        if grades_score >= 90:
            class_grades_letters.append("%i is a A" %(grades_score))
        elif grades_score >= 80 and grades_score < 90:
            class_grades_letters.append("%i is a B" %(grades_score))
        elif grades_score >= 70 and grades_score < 80:
            class_grades_letters.append("%i is a C" %(grades_score))
        elif grades_score >= 60 and grades_score < 70:
            class_grades_letters.append("%i is a D" %(grades_score))
        else:
            class_grades_letters.append("%i is a F" %(grades_score))
    return class_grades_letters

def write_newgrades(grade_list):
    with open('/Users/cristina/Source/intro_class_cristina/class_grades_letters.txt', 'w') as my_file:
        for line in grade_list:
            my_file.write(line)
            my_file.write("\n")


def main():
    grade_list = process_file()
    class_grades_letters = convert_score(grade_list)
    write_newgrades(class_grades_letters)

if __name__ == '__main__':
    main()



