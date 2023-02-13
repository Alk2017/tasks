
student_tuples = (
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),


)
if __name__ == '__main__':
    print(sorted(student_tuples, key=lambda student: student[2]))
