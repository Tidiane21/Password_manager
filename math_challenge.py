import random
import time


Operators=["+","-","*"]
min_operands=3 
max_operands=15
Problems=10

def challenge_generator():
    first_number=random.randint(min_operands,max_operands)
    second_number=random.randint(min_operands,max_operands)
    operator=random.choice(Operators)

    expr= str(first_number)+" "+operator+" "+str(second_number)
    answer=eval(expr)
    return expr,answer

wrong=0
input("Press ENTER to start")
print("---------------------")

start_time=time.time()
for i in range(Problems):
    expr,answer=challenge_generator()
    while True:
        guess=input("Problem #"+str(i+1)+": "+expr+" = ")
        if int(guess)==answer:
            break
        wrong=+1

end_time=time.time()
total_time=end_time-start_time

print("----------------------------------")
print(f"Nice work!!! You finished in {round(total_time)} seconds")