
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
    value_type = {v: t for t, v in type_value.items()}
    card_value = {'A': 12, 'K': 11, 'Q': 10, 'J': 0, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}

    def __init__(self, s: str):
        self.id = Hand.next_id
        Hand.next_id += 1

        self.cards = list(s.split()[0])
        self.bid = int(s.split()[1])

        if 'J' in self.cards:
            self.has_joker = True
        else:
            self.has_joker = False

        c = {a: self.cards.count(a) for a in set(self.cards)} # card: amount
        c = dict(
                sorted(
                    c.items(),
                    key=lambda item: item[1],
                    reverse=True
                    )
                )# sorted by amount

        self.type = self._calc_type(c)

        self.order = [Hand.type_value[self.type]] + [Hand.card_value[card] for card in self.cards]

        if self.has_joker and self.cards != list('JJJJJ'):
            print(self.id)
            print(self)
            print(c)
            if list(c)[0] == 'J':
                print('0 is J')
                self.joker_as = c[list(c)[1]]
                c[list(c)[1]] += c.pop('J')
            else:
                print('0 is not J')
                self.joker_as = c[list(c)[0]]
                c[list(c)[0]] += c.pop('J')
            self.type = self._calc_type(c)
            self.order[0] = Hand.type_value[self.type]
            print(c)
            print(self)
            print()

    def _calc_type(self, c):
        if len(c) == 1:
            return 'fiveofakind'
        elif len(c) == 2:
            if c[list(c)[0]] == 4:
                return 'fourofakind'
            else:
                return 'fullhouse'
        elif len(c) == 3:
            if c[list(c)[0]] == 3:
                return 'threeofakind'
            else:
                return 'twopair'
        elif len(c) == 4:
            return 'onepair'
        else:
            return 'highcard'

    def __str__(self):
        return f'''{''.join(self.cards)} ({self.type}): {self.bid} [id: {self.id}: {self.order}]'''

    def get_order(self):
        return self.order


#inp = open('../../input/2023/7/example1', 'r').read().splitlines()[:-1]
inp = open('../../input/2023/7/input', 'r').read().splitlines()[:-1]

hands = [Hand(line) for line in inp]

hands.sort(key=Hand.get_order)
part2 = 0

for idx, hand in enumerate(hands):
    hand.rank = idx + 1
    part2 += hand.rank * hand.bid

print(f'Part 2: {part2}')

