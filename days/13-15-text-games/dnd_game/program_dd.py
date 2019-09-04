from actors_dd import Creature, Wizard, Dragon
import random

def main():
    print_header()
    game_loop()


def print_header():
    print('---------------------')
    print('    Wizard Game      ')
    print('---------------------')
    print()

def game_loop():
    creatures = [
        Creature('Bat', 5),
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Dragon('Black Dragon', 5, scaliness=2, breaths_fire=False),
        Wizard('Evil Wizard', 1000)
    ]

    hero = Wizard('Ruben', 75)

    while True:

        active_creature = random.choice(creatures)

        print(f'A {active_creature.name} of level {active_creature.level}' 
        f' has appeared from a dark and foggy forest...')
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                print('The wizard defeated {}'.format(active_creature.name))
            else:
                print(f"The wizard has been defeated by the powerful "
                f"{active_creature.name}")
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!!!')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'
                  .format(hero.name))
            for c in creatures:
                print(" * {} of level {}".format(
                    c.name, c.level
                ))
         
        else:
            print("OK, exiting game... bye!")
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

        print()


if __name__ == "__main__":
    main()