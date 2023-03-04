import data


class Quiz:
    def __init__(self):
        self.quiz_list = data.question_data
        self.qsn_position = 0
        self.qsn_number = 1
        self.user_answer = ""
        self.score = 0

    def question(self):
        qsn = self.quiz_list[self.qsn_position]
        self.qsn_position += 1
        self.user_answer = input(f"Q.{self.qsn_number}: {qsn['text']} (True/False):").lower()

    def check_answer(self):
        user_ans = self.user_answer
        answer = self.quiz_list[self.qsn_position]['answer']
        if user_ans.lower() == answer.lower():
            self.score += 1
            print("That's correct.")
            print(f"Your current score is: ")
            print(answer)
        else:
            print("answer is wrong")
            print(user_ans)
            print(answer)
