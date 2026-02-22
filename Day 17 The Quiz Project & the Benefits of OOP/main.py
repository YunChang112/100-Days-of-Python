from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    text = item["question"]
    answer = item["correct_answer"]
    Questions = Question(text, answer)
    question_bank.append(Questions)

# 在这个main.py里面，把原始数据通过class Question，转化成了一个一个object.text or object.answer的小信封，并放进了question_bank这个大邮筒里。

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    # user_input = quiz.next_question()
    #
    # quiz.check_answer(user_input)



# 以下是我的与angela不同的现实最终结果的方式：
# quiz.to_show_result()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.total_score}/{len(question_bank)}.")


