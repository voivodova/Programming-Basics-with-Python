name = input()
grades_counter = 0
years_counter = 0
failed_years = 0

while True:
    annual_grade = float(input())

    if annual_grade < 4:
        failed_years += 1
        if failed_years > 1:
            print(f"{name} has been excluded at {years_counter + 1} grade")
            break

        continue

    else:
        grades_counter += annual_grade

    years_counter += 1

    if years_counter == 12:
        average_grade = grades_counter / 12
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break
