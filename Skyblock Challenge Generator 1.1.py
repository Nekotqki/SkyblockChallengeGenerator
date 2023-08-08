import random
from colorama import Fore, Back, Style

print(Fore.YELLOW + 'Skyblock Challenge Randomizer' + Fore.WHITE)
print('')
print(Fore.GREEN + Back.CYAN + 'Version 1.1' + Fore.WHITE)
print('')
challenges_easy = [
    'Kill a Tier 4 Revenant Slayer.',
    'Kill a Tier 3 Sven Slayer.',
    'Kill a Tier 3 Tarantula Slayer.',
    'Kill a Tier 1 Voidgloom Slayer.',
    'Beat Floor 1, 3 times.',
    'Beat Floor 2, 3 times.',
    'Beat Floor 3, 1 time.',
    'Give a hub beggar 100k coins.',
    'Make 1m Coins.'
]

challenges_medium = [
    'Kill a Tier 5 Revenant Slayer.',
    'Kill a Tier 4 Sven Slayer.',
    'Kill a Tier 4 Tarantula Slayer.',
    'Kill a Tier 2 Voidgloom Slayer, or kill 10 Tier 1 Voidglooms.',
    'Beat Floor 3, 5 times.',
    'Beat Floor 5, 3 times',
    'Beat Floor 6, 2 times.',
    'Give a hub beggar 500k coins.',
    'Kill 1 Boss in Crimson Isle.'
    'Make 5m Coins'
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
    'Make 10m Coins.'
]

challenges_insane = [
   'Kill 10 Bosses in Crimson Isle.',
   'Beat M1, 5 times.'
   'Beat F7, 25 times.'
   'Beat Tier 1 Inferno Slayer, 1 time.'
   'Make 25m Coins.'
]

sanity_count = 0
sanity_meter = ('----------')
sanity_percentage = (str(sanity_count) + str('%'))
hashes = sanity_count//10

difficulty = input(Back.RESET + Fore.CYAN + 'Choose challenge difficulty. Easy/Medium/Hard' + Fore.WHITE).lower()
while True:
    challenge = ''
    sanity_count_addition = 0
    if sanity_count == 100:
        challenge = random.choice(challenges_insane)
        sanity_count_addition = -100
    elif difficulty == 'easy':
        challenge = random.choice(challenges_easy)
        sanity_count_addition = 5
    elif difficulty == 'medium':
        challenge = random.choice(challenges_medium)
        sanity_count_addition = 10
    elif difficulty == 'hard':
        challenge = random.choice(challenges_hard)
        sanity_count_addition = 20

    sanity_meter = '#' * hashes + '-' * (10-hashes)
    print('')
    print("Your challenge is:", challenge)
    print('Sanity meter:', sanity_meter, sanity_percentage)
    choice = input(
        "Type C to complete the challenge, R to reroll it, D to change difficulty, and Q to quit.").lower()
    if choice == "c":
        if sanity_count_addition == -100:
            print(Fore.RED + Style.DIM + 'Sanity Meter Restarted!' + Fore.RESET + Style.NORMAL)
        else:
            print('Added +' + str(sanity_count_addition) + ' Sanity Points!')
        sanity_count = int(sanity_count) + sanity_count_addition
        if sanity_count > 99:
            # sanity meter is at atleast 100
            print(Fore.RED + 'The Sanity Meter is now at 100%!' + Fore.WHITE)
            print(Fore.RED + 'The next challenge will be insane difficulty.' + Fore.WHITE)
            sanity_count = 100
        hashes = sanity_count//10
        sanity_meter = '#' * hashes + '-' * (10-hashes)
        sanity_percentage = (str(sanity_count) + str('%'))
        print('')
    elif choice == "r":
        print('Challenge rerolled!')
        print('')
    elif choice == "q":
        print('Script turned off.')
        break
    elif choice == "d":
        difficulty = 0
        while difficulty == 0:
            difficulty = input('Choose the new difficulty: Easy/Medium/Hard.').lower()
            if difficulty != 'easy' and difficulty != 'medium' and difficulty != 'hard':
                difficulty = 0
    else:
        print(Style.DIM + Fore.RED + "Input not specified." + Style.NORMAL + Fore.WHITE)