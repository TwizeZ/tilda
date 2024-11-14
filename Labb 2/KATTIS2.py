"""
Felix Larsson
Labbpartner: Anton Kancans
DD1320 Tillämpad datalogi
Labb 2
2024-09-06
"""

import sys
from linkedQFile import LinkedQ

def wizard():
    indata = sys.stdin.readline()
    # indata = "3 1 5 2 4"
    user_cards = indata.split(" ")

    q = LinkedQ()

    for card in user_cards:
        q.enqueue(card)                            

    final_order = ""
    for i in range(len(user_cards)):  
        deq_card = q.dequeue()
        q.enqueue(deq_card)
        current_card = q.dequeue()
        final_order = final_order + str(current_card) + " "
    print(final_order)

wizard()