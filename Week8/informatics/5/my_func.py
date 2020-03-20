#function which takes question and checks answer  then return number of correctly answered questions
class PythonTest:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


q1 = PythonTest("What will return this string function?\nIf string is s=abbsfdg\ns.find(fdg)", "4")
q2 = PythonTest("Which of the operators return int value from division?", "//")
q3 = PythonTest("What does self keyword mean in Python", "this")
q4 = PythonTest("Is increment(++) work on Python? Yes/No", "No")
questions = [q1, q2, q3, q4]


def right_questions(test_ques):
    cnt = 0
    for i in range(len(test_ques)):
        print(str(i+1) + "." + test_ques[i].question)
        x = input()
        if test_ques[i].answer == x:
            cnt += 1
    return cnt


ans = right_questions(questions)

if ans == 4:
    print("Very Good!")
elif ans == 0 or ans == 1:
    print("Bad")
else:
    print("Good")