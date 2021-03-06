import uuid


class QuizAnswer(object):
    def __init__(self, quiz):
        self.quiz = quiz
        self.id = uuid.uuid4()
        self.answers = []

    def add_answer(self, answer):
        self.answers.append(answer)


class Answer(object):
    def __init__(self, answers, question):
        self.question = question
        self.answers = answers

    def __str__(self):
        message = ''
        for answer in self.answers:
            message = f'Title: {self.question}  ' \
                      f'Answer: {answer}'
        return message

