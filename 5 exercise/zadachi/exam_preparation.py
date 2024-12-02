number_bad_grades = int(input())
failed_times = 0
solved_problem_count = 0
grades_sum = 0
last_problem = ""
has_failed = True

while number_bad_grades > failed_times:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_sum += grade
    solved_problem_count += 1
    last_problem = problem_name

average_grade = grades_sum / solved_problem_count

if has_failed:
    print(f"You need a break, {number_bad_grades} poor grades.")
else:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {solved_problem_count}")
    print(f"Last problem: {last_problem}")


