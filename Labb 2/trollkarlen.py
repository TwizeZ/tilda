"""
Felix Larsson
Labbpartner: Anton Kancans
DD1320 Tillämpad datalogi
Labb 2
2024-09-06
"""

# from arrayQFile import ArrayQ
from linkedQFile import LinkedQ as ArrayQ

def wizard():
    # print("Skriv in ett antal nummer separerade med mellanslag")
    # user_input = input(">> ")
    # user_cards = user_input.split()

    # user_cards = [3, 1, 5, 2, 4]
    user_cards = [7, 1, 12, 2, 8, 3, 11, 4, 9, 5, 13, 6, 10]

    q = ArrayQ()

    for card in user_cards:
        q.enqueue(int(card))                            # Lägger in alla korten i en kö

    final_order = []
    for item in range(len(user_cards)):  
        q.enqueue(q.dequeue())                          # Flyttar första kortet längst bak
        current_card = q.dequeue()                      # Plockar ut det nya första kortet
        print(current_card)                             # Skriver ut det nya första kortet
        final_order.append(current_card)                # Sparar det nya första kortet i en lista

    print(final_order)                                  # Skriver ut listan med korten i rätt ordning

wizard()