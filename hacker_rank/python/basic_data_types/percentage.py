from decimal import Decimal

def get_average(student_marks, query_name):
    scores = student_marks[query_name]
    avg = Decimal(sum(scores)/len(scores))
    print(round(avg, 2))

if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    get_average(student_marks, query_name)
