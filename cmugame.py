print(r'''
                                               /\      /\
                                               ||______||
                                               || ^  ^ ||
                                               \| |  | |/
                                                |______|
              __                                |  __  |
             /  \       ________________________|_/  \_|__
            / ^^ \     /=========================/ ^^ \===|
           /  []  \   /=========================/  []  \==|
          /________\ /=========================/________\=|
       *  |        |/==========================|        |=|
      *** | ^^  ^^ |---------------------------| ^^  ^^ |--
     *****| []  [] |           _____           | []  [] | |
    *******        |          /_____\          |      * | |
   *********^^  ^^ |  ^^  ^^  |  |  |  ^^  ^^  |     ***| |
  ***********]  [] |  []  []  |  |  |  []  []  | ===***** |
 *************     |         @|__|__|@         |/ |*******|
***************   ***********--=====--**********| *********
***************___*********** |=====| **********|***********
 *************     ********* /=======\ ******** | *********
''')
print("Welcome to Clown Math University, we hope you enjoy the tour.\nWhat's your name again professor? I do apologize, my age is catching up with me.")

player_name = input("My name is ")

print(f"Hello Professor {player_name}, follow me please.")

decision_1 = input("Follow the mysterious tour guide? Type Yes or No.\n")

if decision_1 == "Yes":
    input(f"So professor {player_name}, what brings you to this campus?\n")
    print("How fascinating. Well forgive me for forgetting to introduce myself but my name is Oscar,\nI am the head of DevOps here at Clown Math University.\nI was supposed to teach my cousin how to code but I prefer taking people on tours instead and visiting foreign countries near the equator.")
    decision_2 = input("What would you like to see first? The Library or the Lake? (Type Library or Type Lake to continue)")
    if decision_2 == "Library":
        print("You go to the Library and are in awe of the collection of books they have.\nThe tour guide is going on and on about the history of the library and all its glory.\nYou feel at peace here.")
        decision_3 = input(f"Hey {player_name}, Are you listening? I have to run to the gentlemens room, can you just wait here?\nIts imperative that you don't mess with anything in the library until I come back.\n[the tour guide leaves and you're left with a dilemma.\nHe told you not to leave but your curiosity is getting the better of you.\nYou can either wait here, start messing with the books on the shelf, or go get some coffee at the cafe.]\n[Type wait, books, or cafe to continue]")
        if decision_3 == "wait":
            print(f"You patiently wait for the tour guide to come back.\nHe definitely took his sweet time, you are practically falling asleep. '{player_name} its time I take you to your future classroom.'\nHe takes you about two miles north of where the library is and you arrive at a large building with beautiful columns.\n He walks you inside, up the marble staircase and shows you to your new classroom.\n'I hope you enjoyed the tour Mr.{player_name}.We can't wait for you to start next semester. [You have won the game, great job].\nCMU is going to be a full dating sim game coming soon(Don't worry it'll have an actual GUI..)")
        elif decision_3 == "books":
            print("You decide you know better than this dusty tour guide.\n You walk up to the books and pull the one that isn't pushed in all the way.\nThe librarian sees you and knows you clearly didnt follow directions.\nThey ask you if you have a library card and you answer that you do not.\nInfuriated, she grabs the book you took and whacks you as hard as they can and you hit the ground cold. (GAME OVER :P)")
        elif decision_3 =="cafe":
            print("You decide you know better than this dusty tour guide.\nYou walk up to the cafe and you start to browse the menu before the cute barista starts to talk to you.\nThey ask 'waddaya buyin, handsome'. You are speechless because no one has ever called you handsome before except you mom(sarcastically).\nYou respond back with a pickup line and someone overhears.\nYou hear large thumping as if a rhino was headed in your direction.\nAs you turn around to investigate this large thumping, you see a man that's 3x your size.\nHe says 'Why are you hitting on my girlfriend you animal?!'.\nWith one swift punch he knocks you out and says 'These hands are rated E for everyone, loser'.[GAME OVER HAHAHA] ")
        else:
            print("I guess you don't know how to follow directions.\nWhatever you typed just got you arrested by the campus police and now you have to share a cell with the other campus criminals.\nYou get stabbed as soon as the guards walk away and bleed out.[GAME OVER]")
    else:
        "You went to the lake, saw its beauty and reflection of yourself and thought 'wow im handsome'.\nThen the loch ness monster comes out and eats you whole (GAME OVER)"

else: print("Well maybe you shouldn't have come if you weren't feeling adventurous... (GAME OVER)")

