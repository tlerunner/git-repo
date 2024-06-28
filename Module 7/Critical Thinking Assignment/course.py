# Create list of courses, rooms, instructors, times so they only occur once in the program.  Indexes line up.
course_numbers = ['CSC101','CSC102','CSC103','NET110','COM241']
course_rooms = ['3004','4501','6755','1244','1441']
instructor_names = ['Haynes','Alvarado','Rich','Burke','Lee']
course_times = ['8:00 a.m.','9:00 a.m.','10:00 a.m.','11:00 a.m.','1:00 p.m.']

# Create rooms dictionary
rooms = {}
index = 0
for course in course_numbers:
    rooms[course] = course_rooms[index]
    index += 1

# Create instructors dictionary
instructors = {}
index = 0
for course in course_numbers:
    instructors[course] = instructor_names[index]
    index += 1
    
# Create times dictionary
times = {}
index = 0
for course in course_numbers:
    times[course] = course_times[index]
    index += 1

def print_menu(course_numbers):
    print('\nAvailable courses:\n')
    for course in course_numbers:
        print(course)
    print('q to quit')
    return input('\nInput the course number: ')
 
if __name__ == "__main__":
    course_number = ''
    while course_number != 'q':
        course_number = print_menu(course_numbers)
        if course_number != 'q':
            try:
                print('\nCourse {} meets in room {} at {} with Dr. {}.'.format(course_number,rooms[course_number],times[course_number],instructors[course_number]))
            except:
                print('\nUnknown course, try again.')