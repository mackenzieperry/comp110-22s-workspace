""""Practice func writing for quiz 02"""


def averager_grades(students_grades: dict[str, list[int]]) -> dict[str, float]:
    student_averages: dict[str, float] = {}
    for key in students_grades:
        grades: list[int] = students_grades[key]
        total_points: int = 0
        for score in grades:
            total_points += score
        average: float = 0
        average = total_points / len(grades)
        student_averages[key] = average
    return student_averages


def main() -> None:
    students: dict[str, list[int]] = {"Babe": [80, 80, 90, 90], "Belle": [70, 90], "Claire": [80, 90, 85]}
    print(averager_grades(students))


if __name__ == "__main__":
    main()