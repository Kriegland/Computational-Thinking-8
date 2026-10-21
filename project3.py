Imperium = 0
Xenos = 0
Chaos = 0

answer1 = input ("Would you, (A) fight for humanity across the stars, (B) follow your own goal with your own reason to conqure the stars, or (C) fight your friends and family ust because you thought it would be funny and someone told you to.")

if answer1 == "A" or answer1 == "a":
    Imperium += 1
elif answer1 == "B" or answer1 == "b":
    Xenos += 1
elif answer1 == "C" or answer1 == "c":
    Chaos += 1

answer2 = input ("Would you rather live in a (B)medeival city, (A)futuristic city, or (C)a random/hellish city.")
if answer2 == "A" or answer2 == "a":
    Xenos +=1
elif answer2 == "B" or answer2 == "b":
    Imperium +=1
elif answer2 == "C" or answer2 == "c":
    Chaos +=1

answer3 = input ("What would you do in a family conflict? (A)side with your family, (B)side against your family, or (C)appear and join for no apparent reason.")
if answer3 == "A" or answer3 == "a":
    Imperium +=1
elif answer3 == "B" or answer3 == "b":
    Chaos +=1
elif answer3 == "C" or answer3 == "c":
    Xenos +=1

answer4 = input ("What would you rather have, (A)the ability to get powers from a natural gods, (B)be able to make anything happen if enough friends believe it, or (C)call upon your god for protection in dire situations as a special ability?")
if answer4 == "A" or answer4 == "a":
    Chaos +=1
elif answer4 == "B" or answer4 == "b":
    Xenos +=1
elif answer4 == "C" or answer4 =="c":
    Imperium +=1

answer5 = input ("Would you rather, (A) eat food such as this very mysterious tofu or other human food, (B) food that you raided and pillaged from villages, or (C) eat anything you see from scrap metal to biomass?")
if answer5 == "A" or answer5 == "a":
    Imperium +=1
elif answer5 == "B" or answer5 == "b":
    Chaos +=1
elif answer5 == "C" or answer5 == "c":
    Xenos +=1

print (f"Thank you for cooperation in taking this quiz to see your faction. Your score is {Chaos} for the legions Chaos, {Imperium} for the Imperium, and {Xenos} for the filthy Xenos.")

# end of questions
if Imperium > Chaos and Imperium > Xenos:
    print ("Welcome to the Imperium and may you have the Emporer's blessing.")
elif Chaos > Xenos and Chaos > Imperium:
    print ("So youve chosen heracy. Tell you what I will give you a minute head start.")
elif Xenos > Imperium and Xenos > Chaos:
    print ("Brothers we must PURGE THE UNCLEAN!!!")