if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        students.append([name, score])
    m = min(scores)
    stud_new = [[ns, sc] for [ns,sc] in students if sc != m]
    sc_new = [i for i in scores if i != m]
    m1 = min(sc_new)
    stud_new1 = [ns for [ns,sc] in stud_new if sc == m1]
    for i in sorted(stud_new1):
        print(i)