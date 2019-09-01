import random
movies = ["iron man", "hulk", "captain america", "captain marvell", "grood", "vision"]

def create_question(movie):
    letters = list(movie)
    temp = []
    for ch in letters:
        if(ch!=' '):
            temp.append("*")
        else:
            temp.append(" ")
    qn = ''.join(str(x) for x in temp)
    return qn

def is_present(letter, movie):
    c = movie.count(letter)
    if(c==0):
        return False
    else:
        return True
    
def unlock(qn, movie, letter):
    ref = list(movie)
    qn_list = list(qn)
    temp = []
    n = len(movie)
    for i in range(n):
        if (ref[i]==letter or ref[i]==" "):
            temp.append(ref[i])
        else:
            if(qn_list[i]=='*'):
                temp.append('*')
            else:
                temp.append(ref[i])
        qn_new = ''.join(str(x) for x in temp)
        return qn_new
    
def play():
  name1 = input("Enter the name of player 1: ")
  name2 = input("Enter the name of player 2: ")
  pp1=0
  pp2=0
  turn=1
  willing = True
  while willing:
    if(turn%2!=0):
      print(name1, " ! It's your turn.")
      picked_movie = random.choice(movies)
      qn = create_question(picked_movie)
      print(qn)
      not_guessed = True
      modified_qn = qn
      while not_guessed:
        letter = input("Enter your guessing: ")
        if(is_present(letter, picked_movie)):
          #Display the modified name
          modified_qn = unlock(modified_qn, picked_movie, letter)
          print(modified_qn)
          d = input("Press 1 to guess the movie or 2 to unlock another letter: ")
          if(d==1):
              ans = input("Enter your guess: ")
              if(ans == picked_movie):
                  pp1 = pp1+1
                  print("Correct")
                  not_guessed = False
                  print("Your Score: ", pp1)
              else:
                  print("Not correct! \n Try unlocking another character.")
        else:
          print(letter," not found")
      c = input("Press 1 to continue or 0 to quit: ")
      if(c==0):
          print(name1, "Your Score: ", pp1)
          print(name2, "Your Score: ", pp2)
          print("Thanks for playing, Have a Good day!")
          willing = False
    else:
        
       #Player 2 coded
      print(name1, " ! It's your turn.")
      picked_movie = random.choice(movies)
      qn = create_question(picked_movie)
      print(qn)
      not_guessed = True
      modified_qn = qn
      while not_guessed:
        letter = input("Enter your guessing: ")
        if(is_present(letter, picked_movie)):
          #Display the modified name
          modified_qn = unlock(modified_qn, picked_movie, letter)
          print(modified_qn)
          d = input("Press 1 to guess the movie or 2 to unlock another letter: ")
          if(d==1):
              ans = input("Enter your guess: ")
              if(ans == picked_movie):
                  pp1 = pp1+1
                  print("Correct")
                  not_guessed = False
                  print("Your Score: ", pp1)
              else:
                  print("Not correct! \n Try unlocking another character.")
        else:
          print(letter," not found")
      c = input("Press 1 to continue or 0 to quit: ")
      if(c==0):
          print(name1, "Your Score: ", pp1)
          print(name2, "Your Score: ", pp2)
          print("Thanks for playing, Have a Good day!")
          willing = False
    turn = turn + 1
      
play()
    