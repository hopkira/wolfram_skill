from wolframqa import K9QA
import time
k9qa = K9QA()
questions = ["What temperature is it on Jupiter?","What is its radius?","How far is Jupiter from the sun?", "Who if Stephen Wolfram?","Where am I?", "What time is it?", "Who is Einstein?"]
for question in questions:
    answer = k9qa.ask_question(question)
    print(answer)
    time.sleep(3)