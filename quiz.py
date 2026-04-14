print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
score = 0
if playing.lower() != "yes":
    quit()
else:  
    print("Alright! Let's play :)")    

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1 
else:
    print("Incorrect!")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('correct!') 
    score += 1 
else:
    print("Incorrect!")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('correct!') 
    score += 1 
else:
    print("Incorrect!")
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('correct!') 
    score += 1 
else:
    print("Incorrect!")      
answer = input("What does SSD stand for?")
if answer.lower() == "solid state drive":
    print('correct!')
    score += 1
else:
    print("Incorrect!")     
answer = input("What does OS stand for?")
if answer.lower() == "operating system":
    print('correct!')
    score += 1       

print("You got " + str(score) + " questions correct!")  
print("You got " + str((score/5) * 100) + "%")           
