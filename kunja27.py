from question import question

question_prompts=[
    "What is color of apple?\n(a) Red\n(b) Yellow\n(c) Blue\nyou have choose:",
    "\nWhat is color of mango?\n(a) Red\n(b) Yellow\n(c) Blue\nyou have choose:",
    "\nWhat is color of sky?\n(a) Red\n(b) Yellow\n(c) Blue\nyou have choose:"
]

nameofquestion=[
    question(question_prompts[0],"a"),
    question(question_prompts[1],"b"),
    question(question_prompts[2],"c")
]
def run_test(questions):
    score=0
    for q in nameofquestion:
        answer=input(q.prompt)
        if answer == q.answer:
            score+=1
    print("You got "+str(score)+ "/"+str(len(nameofquestion))+" correct")

run_test(question)