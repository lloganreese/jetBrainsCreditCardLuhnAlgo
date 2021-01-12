import random
import _sqlite3


class Banking:
    balance = 0
    card_number = 0
    card_pin = 0

    # main constructor with first interface for user
    def __init__(self):
        print(
            """1. Create an account
2. Log into account
0. Exit""")

        Banking.take_input(self)

        if self.user_input == "1":
            Banking.create_card(self)
        elif self.user_input == "2":
            Banking.login(self)
        elif self.user_input == "0":
            print(f"\nBye!")
            exit()

    # used for all inputs throughout the program
    def take_input(self):
        self.user_input = input()

    # creates a card/PIN for the user based on a random range of integers with '400000' leading
    def create_card(self):
        print(f"\nYour card has been created")

        print("Your card number: ")
        Banking.luhn_check(self)
        print(self.card_number)

        print("Your card PIN:")
        self.card_pin = '{:04d}'.format(random.randrange(0000, 9999))
        print(self.card_pin + "\n")

        Banking.__init__(self)

    # references previously created card/PIN to allow user to login
    def login(self):
        print(f"\nEnter your card number:")
        user_card = input()
        print("Enter your PIN:")
        user_pin = input()

        if user_card == self.card_number and user_pin == self.card_pin:
            print(f"\nYou have successfully logged in!\n")
            Banking.logged_in(self)
        else:
            print("Wrong card number or PIN!")
            Banking.__init__(self)

    # interface shown to user after successful login
    def logged_in(self):
        print(
            """1. Balance
2. Log out
0. Exit""")

        Banking.take_input(self)

        if self.user_input == "1":
            print("\nBalance: 0\n")
            Banking.logged_in(self)
        elif self.user_input == "2":
            print("\nYou have successfully logged out!\n")
            Banking.__init__(self)
        elif self.user_input == "0":
            print(f"\nBye!")
            exit()

    # creates a cc number based on luhn algorithm parameters
    def luhn_check(self):
        card_list = []

        self.card_number = (str(400000)
                            + '{:09d}'.format(random.randrange(000000000, 999999999))
                            + str(random.randint(0, 9)))

        # creates a integer list out of the numbers within the credit card
        for x in self.card_number:
            card_list.append(int(x))

        # stores the last digit of the original cc number
        # into a variable & removes from the cc for calculations
        checksum = card_list.pop(-1)

        # multiplies each odd index of the credit card by 2
        for i in range(len(card_list)):
            if i % 2 == 0:
                card_list[i] = card_list[i] * 2

        # subtracts 9 from all digits greater than 9
        for j in range(len(card_list)):
            if card_list[j] > 9:
                card_list[j] -= 9

        if (sum(card_list) + checksum) % 10 != 0:
            Banking.luhn_check(self)


Banking()
