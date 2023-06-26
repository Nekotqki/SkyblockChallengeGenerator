import random

print ('Skyblock Challenge Randomizer')
challenges_easy = [
 'Kill a Tier 4 Revenant Slayer.',
 'Kill a Tier 3 Sven Slayer.',
 'Kill a Tier 3 Tarantula Slayer.',
 'Kill a Tier 1 Voidgloom Slayer.',
 'Beat Floor 1, 3 times.',
 'Beat Floor 2, 3 times.',
 'Beat Floor 3, 1 time.',
 'Give a hub beggar 100k coins.',
]

challenges_medium = [
 'Kill a Tier 5 Revenant Slayer.',
 'Kill a Tier 4 Sven Slayer.',
 'Kill a Tier 4 Tarantula Slayer.',
 'Kill a Tier 2 Voidgloom Slayer, or kill 10 Tier 1 Voidglooms.'
 'Beat Floor 3, 5 times.',
 'Beat Floor 5, 3 times',
 'Beat Floor 6, 2 times.',
 'Give a hub beggar 500k coins.',
 'Kill 1 Boss in Crimson Isle.'
]

challenges_hard = [
 'Kill a Tier 5 Revenant Slayer, 3 times.',
 'Kill a Tier 4 Sven Slayer, 5 times.',
 'Kill a Tier 4 Tarantula Slayer, 5 times.',
 'Kill a Tier 2 Voidgloom Slayer, 10 times.',
 'Kill a Tier 3 Voidgloom Slayer.',
 'Beat Floor 5, 10 times.',
 'Beat Floor 6, 10 times.',
 'Beat Floor 7, 3 times.',
 'Kill 3 Bosses in Crimson Isle.',
]

sanity_count = 0
sanity_meter = ('----------')
sanity_percentage = (str(sanity_count) +str('%'))
hashes = sanity_count//10

difficulty = input('Choose challenge difficulty. Easy/Medium/Hard')
if difficulty == 'easy':
 while True:
   challenge_easy = random.choice(challenges_easy)

   sanity_meter = '#' * hashes + '-' * (10-hashes)
   print('')
   print("Your challenge is:", challenge_easy)
   print('Sanity meter:', sanity_meter, sanity_percentage)
   choice = input("Type C to complete the challenge, R to reroll it, and Q to quit.").lower()
   if choice == "c":
    print('Added +5 Sanity Points!')
    sanity_count = int(sanity_count) + int(5)
    hashes = sanity_count//10
    sanity_meter = '#' * hashes + '-' * (10-hashes)
    sanity_percentage = (str(sanity_count) +str('%'))
    print('')
   elif choice == "r":
    print('Challenge rerolled!')
    print('')
   elif choice == "q":
    print('Script turned off.')
    break
   else:
    print("Input not specified.")

if difficulty == 'medium':
 while True:
   challenge_medium = random.choice(challenges_medium)

   sanity_meter = '#' * hashes + '-' * (10-hashes)
   print('')
   print("Your challenge is:", challenge_medium)
   print('Sanity meter:', sanity_meter, sanity_percentage)
   choice = input("Type C to complete the challenge, R to reroll it, and Q to quit.").lower()
   if choice == "c":
    print('Added +10 Sanity Points!')
    sanity_count = int(sanity_count) + int(10)
    hashes = sanity_count//10
    sanity_meter = '#' * hashes + '-' * (10-hashes)
    sanity_percentage = (str(sanity_count) +str('%'))
    print('')
   elif choice == "r":
    print('Challenge rerolled!')
    print('')
   elif choice == "q":
    print('Script turned off.')
    break
   else:
    print("Input not specified.")

if difficulty == 'hard':
 while True:
   challenge_hard = random.choice(challenges_hard)

   sanity_meter = '#' * hashes + '-' * (10-hashes)
   print('')
   print("Your challenge is:", challenge_hard)
   print('Sanity meter:', sanity_meter, sanity_percentage)
   choice = input("Type C to complete the challenge, R to reroll it, and Q to quit.").lower()
   if choice == "c":
    print('Added +20 Sanity Points!')
    sanity_count = int(sanity_count) + int(20)
    hashes = sanity_count//10
    sanity_meter = '#' * hashes + '-' * (10-hashes)
    sanity_percentage = (str(sanity_count) +str('%'))
    print('')
   elif choice == "r":
    print('Challenge rerolled!')
    print('')
   elif choice == "q":
    print('Script turned off.')
    break
   else:
    print("Input not specified.")