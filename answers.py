def get_answer(question):
	answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
	return answers.get(question.lower())

a = get_answer(input(''))

print(a)