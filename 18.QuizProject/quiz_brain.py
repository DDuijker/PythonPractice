
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_input = input(f"Q.{self.question_number + 1}: {current_question.text}. (True/False)?: ")
        self.check_answer(user_input, current_question.answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("That's correct!")
        else:
            print("That answer is wrong.")
        print(f"The correct answer is: {correct_answer}")
        print(f"{self.score}/{self.question_number + 1} answered correctly")
        print("\n")
