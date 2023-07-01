import random

print('Skyblock Challenge Randomizer')
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
    'Kill a Tier 2 Voidgloom Slayer, or kill 10 Tier 1 Voidglooms.',
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

challenges_insane = [
    'Solo M7 100,000 times.',
    'Kill 100 T4 Voidglooms',
    'Kill 100 T4 Blazes',
    'Solo M5 in no armor and with no talismans or weapons.',
    'Drop 95 Necron\'s Handles.'
]

sanity_count = 0
sanity_meter = ('----------')
sanity_percentage = (str(sanity_count) + str('%'))
hashes = sanity_count//10

difficulty = input('Choose challenge difficulty. Easy/Medium/Hard').lower()
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
        "Type F to fulfill the challenge, R to reroll it, C to change difficulty, and Q to quit.").lower()
    if choice == "f":
        if sanity_count_addition == -100:
            print('Reset Sanity Meter!')
        else:
            print('Added +' + str(sanity_count_addition) + ' Sanity Points!')
        sanity_count = int(sanity_count) + sanity_count_addition
        if sanity_count > 99:
            # sanity meter is at atleast 100
            print('The Sanity Meter is now at 100%!')
            print('The next challenge will be of insane difficulty.')
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
    elif choice == "c":
        difficulty = 0
        while difficulty == 0:
            difficulty = input('What is the new difficulty?').lower()
            if difficulty != 'easy' and difficulty != 'medium' and difficulty != 'hard':
                difficulty = 0
    else:
        print("Input not specified.")
# Patch Notes:
# Made Easy/Medium/Hard not case-sensitive
# No longer overflows sanity meter
