#Everardo Camarena
#cecs 174, homework 3, April 22 2020
students = {}

def main():
    menu = ' 1. Input how many tests will be given\n 2. Add a new student to the class\n 3. Delete an existing student\n 4. Update a student\'s name\n 5. Update scores for a student\n 6. Calculate average test score per student\n 7. Calculate average test scores for each test for the whole class\n 8. Display all the records\n 9.Quit\n'
    print(menu)
    selection = int(input('Please select an action from the menu: '))
    menu_select(selection, menu)
    print('Good Bye')

def menu_select(value, menu):
    number_tests = None
    while value !=9:
        if value == 1:
            number_tests = int(input('How many tests will be given: '))
            print('The class will have {} tests\n'.format(number_tests))
        elif value == 2:
            if number_tests == None:
                print('Please select 1 from the menu first')
            else:
                add_new(number_tests)
        elif value == 3:
            if students == {}:
                print('No student to delete')
            else:
                delete("")
        elif value == 4:
            if students == {}:
                print('No student names to update')
            else:
                update_name()
        elif value == 5:
            if students == {}:
                print('No scores to update')
            else:
                update_scores()
        elif value == 6:
            if students == {}:
                print('No scores to find individual average')
            else:
                student_average()
        elif value == 7:
            if students == {}:
                print('No test scores from the class to find the average')
            else:
                class_test_average(number_tests)
        elif value == 8:
            print('Here are all the records:\n', students)
        else:
            print('Invalid selection. Please select again\n')
        print(menu)
        value = int(input('Please select an action from the menu: '))

def add_new(number_tests):
    name = input('Enter the new student name: ')
    scores = []
    for x in range(0, number_tests):
        test = int(input('Enter test score: '))
        scores.append(test)
    students[name] = scores
    print('You have successfully added {}\n'.format(name))

def delete(passed_name):
    if passed_name == "":
        name = input('Enter the students current name: ')
        while validate(name) != True:
            print('That is not a valid name')
            name = input('Enter student name: ')
        del students[name]
        print('You have successfully deleted {}\n'.format(name))
    else:
        del students[passed_name]

def update_name():
    old_name = input('Enter the students current name: ')
    while validate(old_name) != True:
        print('That is not a valid name')
        old_name = input('Enter the students current name: ')
    scores = students[old_name]
    delete(old_name)
    name = input('Enter new student name: ')
    students[name] = scores
    print('Student {} is updated to {}\n'.format(old_name, name))

def update_scores():
    name = input('Enter which student you want to update: ')
    validate(name)
    scores = students[name]
    index = -1
    index = int(input('Enter which test you want to change type 0 to exit: '))
    while index != 0:
        new_score = int(input('Enter new score: '))
        scores[index-1] = new_score
        print('{} scores are now {}'.format(name, scores))
        index = int(input('Enter which test you want to change type 0 to exit: '))

def student_average():
    for person, grade in students.items():
        average_grade = sum(grade)/len(grade)
        scores = students[person]
        scores.append(average_grade)
    print('Each student\'s average is calculated and stored\n')
    pass

def class_test_average(number_tests):
    test_grade_averages = []
    grades = []
    average = 0
    for person, grade in students.items():
        grades.append(grade)
    test_number = 0
    while test_number <= len(grades):
        i = 0
        test_grades = []
        for x in grades:
            test_scores = grades[i][test_number]
            test_grades.append(test_scores)
            i += 1
        average = sum(test_grades)/len(test_grades)
        test_grade_averages.append(average)
        test_number += 1
    students['Class Test'] = test_grade_averages
    print('Class average is calculated and stored\n')

def validate(student):
    if students.get(student):
        return True
    else:
        return False
main()
