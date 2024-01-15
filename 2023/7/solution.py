
class Hand:
    next_id = 0
    type_value = {
            'fiveofakind': 6,
            'fourofakind': 5,
            'fullhouse': 4,
            'threeofakind': 3,
            'twopair': 2,
            'onepair': 1,
            'highcard': 0
            }
    card_value = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}

    def __init__(self, s: str):
        self.id = Hand.next_id
        Hand.next_id += 1

        self.cards = list(s.split()[0])
        self.bid = int(s.split()[1])

        c = {a: self.cards.count(a) for a in set(self.cards)}
        if len(c) == 1:
            self.type = 'fiveofakind'
        elif len(c) == 2:
            if c[list(c)[0]] == 4 or c[list(c)[1]] == 4:
                self.type = 'fourofakind'
            else:
                self.type = 'fullhouse'
        elif len(c) == 3:
            if c[list(c)[0]] == 3 or c[list(c)[1]] == 3 or c[list(c)[2]] == 3:
                self.type = 'threeofakind'
            else:
                self.type = 'twopair'
        elif len(c) == 4:
            self.type = 'onepair'
        else:
            self.type = 'highcard'

        self.order = [Hand.type_value[self.type]] + [Hand.card_value[card] for card in self.cards]

    def __str__(self):
        return f'''{''.join(self.cards)} ({self.type}): {self.bid} [id: {self.id}: {self.order}]'''

    def get_order(self):
        return self.order


#inp = open('../../input/2023/7/example1', 'r').read().splitlines()[:-1]
inp = open('../../input/2023/7/input', 'r').read().splitlines()[:-1]

hands = [Hand(line) for line in inp]

hands.sort(key=Hand.get_order)
part1 = 0

for idx, hand in enumerate(hands):
    print(idx+1, hand)
    hand.rank = idx + 1
    part1 += hand.rank * hand.bid

print(f'Part 1: {part1}')

