import random

word1 = 'happiness'
word2 = 'pouch'
word3 = 'pineapple'
word4 = 'eight'
word5 = 'rat'

nums = ['1', '2', '3', '4', '5']

print('\n888888888888888888888888+*. H A N G M A N .*+888888888888888888888888')
print('\n GUESS THE WORD! YOU ONLY HAVE 6 TRIES')
print(f'\n     Random word selected. Game starting...\n')
choice = random.choice(nums)

if choice == '1':
    word=word1
    print('\n hint: emotion')
elif choice == '2':
    word=word2
    print('\n hint: something to carry your school supplies with')
  
elif choice == '3':
    word=word3
    print('\n hint: a fruit')

elif choice == '4':
    word=word4
    print('\n hint: a number')

elif choice == '5':
    word=word5
    print('\n hint: an animal')

else:
    print('\n ERROR! :/')


length = len(word)
k = 0
m = 0
correct=0
tries_left = 6 
wrong = 0
guessed_correct = ['_'] * length


while wrong < 6 and '_' in guessed_correct:  
    guess = input('\n\nenter your guessed letter! :) ')
    
    k = 0 
    found = False  

    while k < length:
        if guess == word[k]:
            correct+=1
            if not found:  
                print('\nGOOD JOB! :D')
                found = True
            guessed_correct[k] = word[k]  
        k += 1  

    
    if found:
        print('--------------------------------------------------------')
        print('word:', ' '.join(guessed_correct))
        print('--------------------------------------------------------')

    else:
        wrong += 1  
        tries_left = 6 - wrong
        print('\nBUMMER... :C')
        print('tries left =', tries_left)
        print('--------------------------------------------------------')
        print('word', ' '.join(guessed_correct))
        print('--------------------------------------------------------')



if correct >= 5:
    print('\n\nCONGRATULATIONS! YOU WON! :D ')
else:
    print('\n\nawwwww :C GAME OVER! The word was:', word)
print('\n8888888888888888888888888888888888888888888888888888888')
