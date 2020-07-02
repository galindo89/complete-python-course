score=0

questions=open ("questions.txt","r")

questions_list=[line.strip() for line in questions.readlines()]

questions_and_result=[question.split("=") for question in questions_list]

questions.close()

print(questions_and_result)

def score_quizz(score,user_answer,correct_answer):

    if user_answer==correct_answer:
        score+=1

    else:
        score+=0

    return score


for quizz in questions_and_result:

    user_answer=input(f"{quizz[0]}= ")
    correct_answer=quizz[1]
    score=score_quizz(score,user_answer,correct_answer)

result_file = open('result.txt', 'w')
result_file.write(f"Your final score is {score}/{len(questions_list)}.")
print(score)









