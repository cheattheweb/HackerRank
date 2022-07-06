if __name__ == '__main__':
    n = int(input())
    students_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        students_marks[name] = scores

    query_name = input()

result = (sum(students_marks[query_name]) / len(students_marks[query_name]))
print(format(result, '.2f'))
