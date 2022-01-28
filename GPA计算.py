credits = []
scores = []
credit0s = []

def gpa(credits, credit0s, scores):
    sum = 0
    result = 0
    for credit in credit0s:
        sum += credit
    for n in range(len(credits)):
        result += credits[n]*credit0s[n]/sum
    return result

while 1:

    score = int(input('请输入单科成绩：'))
    if score == 0:
        break
    credit0 = float(input('请输入单科学分：'))
    if credit0 == 0:
        break
    if score == 100:
        credit = 5.0
    elif score >= 95 and score < 100:
        credit = 4.5
    elif score >= 90 and score < 95:
        credit = 4.0
    elif score >= 85 and score < 90:
        credit = 3.5
    elif score >= 80 and score < 85:
        credit = 3.0
    elif score >= 75 and score < 80:
        credit = 2.5
    elif score >= 70 and score < 75:
        credit = 2.0
    scores.append(score)
    credits.append(credit)
    credit0s.append(credit0)
print('绩点为：', gpa(credits, credit0s, scores))






