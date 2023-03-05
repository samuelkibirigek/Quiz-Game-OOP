import data


class Quiz:
    def __init__(self):
        self.quiz_list = data.question_data
        self.qsn_position = 0
        self.qsn_number = 1
        self.user_answer = ""
        self.score = 0
        self.game_is_on = True

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
            print(f"The correct answer was: {answer}")
            print(f"Your current score is: {self.score}/{self.qsn_number}")
            self.qsn_number += 1
        else:
            print("That's wrong.")
            print(f"The correct answer was: {answer}")
            print(f"Your current score is: {self.score}/{self.qsn_number}")
            self.qsn_number += 1

    def play_game(self):
        if self.qsn_number > 12:
            self.game_is_on = False
        else:
            pass

