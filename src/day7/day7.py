import time

def read(filename) :
    with open(filename,'r') as f :
        data = [line.strip() for line in f]
        data = [ [d.split()[0].strip(),int(d.split()[1].strip())]  for d in data ]
        return data

def sort_string(str) :
    return ''.join(sorted(str))

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


def compare(hand1, hand2) :
    type_order = {'5_kind' : 7,'4_kind' : 6,'full_house' : 5,'3_kind' : 4,'2_pair' : 3,'1_pair' : 2,'none' : 1}
    card_order = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}

    #Check hand type
    if type_order[hand1[2]] != type_order[hand2[2]] :
        return type_order[hand1[2]] - type_order[hand2[2]]

    #check cards order
    else :
        card_rank = [ (card_order[hand1[0][i]] - card_order[hand2[0][i]] ) for i in range(5) ]
        return next((value for value in card_rank if value != 0),0)


def compare_2(hand1, hand2) :
    type_order = {'5_kind' : 7,'4_kind' : 6,'full_house' : 5,'3_kind' : 4,'2_pair' : 3,'1_pair' : 2,'none' : 1}
    card_order = {'A':13, 'K':12, 'Q':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2,'J':1}

    #Check hand type
    if type_order[hand1[2]] != type_order[hand2[2]] :
        return type_order[hand1[2]] - type_order[hand2[2]]

    #check cards order
    else :
        card_rank = [ (card_order[hand1[0][i]] - card_order[hand2[0][i]] ) for i in range(5) ]
        return next((value for value in card_rank if value != 0),0)


def get_hand_type(data) :
    def is_five_kind(hand) :
        return hand[0] == hand[1] == hand[2] == hand[3] == hand[4]

    def is_four_kind(hand) :
        hand = sort_string(hand)
        return (hand[0] != hand[1] == hand[2] == hand[3] == hand[4]) or (hand[0] == hand[1] == hand[2] == hand[3] != hand[4])

    def is_full_house(hand) :
        hand = sort_string(hand)
        return ( (hand[0] == hand[1]) & (hand[2] == hand[3] == hand[4]) & (hand[0] != hand[2]) ) or ( (hand[0] == hand[1] == hand[2]) & (hand[3] == hand[4]) & (hand[0] != hand[3]) )

    def is_three_kind(hand) :
        hand = sort_string(hand)
        return (hand[0] == hand[1] == hand[2] != hand[3] != hand[4]) or (hand[0] != hand[1] != hand[2] == hand[3] == hand[4]) \
            or (hand[0] != hand[1] == hand[2] == hand[3] != hand[4])

    def is_two_pair(hand) :
        hand = sort_string(hand)
        pair_index = list(range(5))
        for i in pair_index :
            pair = list(range(5))
            pair.remove(i)
            if (hand[pair[0]] == hand[pair[1]]) & (hand[pair[2]] == hand[pair[3]]) & (hand[pair[0]] != hand[pair[2]]) :
                return True
        return False

    def is_one_pair(hand) :
        hand = sort_string(hand)
        for i in range(4) :
            if hand[i] == hand[i+1] :
                return True
        return False


    types = []
    for hands in data :
        hand = hands[0]
        if is_five_kind(hand) :
            types.append('5_kind')
            continue
        elif is_four_kind(hand) :
            types.append('4_kind')
            continue
        elif is_full_house(hand) :
            types.append('full_house')
            continue
        elif is_three_kind(hand) :
            types.append('3_kind')
            continue
        elif is_two_pair(hand) :
            types.append('2_pair')
            continue
        elif is_one_pair(hand) :
            types.append('1_pair')
            continue
        else :
            types.append('none')

    return types

def get_hand_type_2(data) :
    types = get_hand_type(data)
    for idx,hand in enumerate(data) :
        count_j = sum([hand[0][i] == 'J' for i in range(5)])
        if count_j == 1 :
            if types[idx] == '4_kind' :
                types[idx] = '5_kind'
            elif types[idx] == '3_kind' :
                types[idx] = '4_kind'
            elif types[idx] == '2_pair' :
                types[idx] = 'full_house'
            elif types[idx] == '1_pair' :
                types[idx] = '3_kind'
            elif types[idx] == 'none' :
                types[idx] = '1_pair'
        elif count_j == 2 :
            if types[idx] == 'full_house' :
                types[idx] = '5_kind'
            elif types[idx] == '2_pair' :
                types[idx] = '4_kind'
            elif types[idx] == '1_pair' :
                types[idx] = '3_kind'
        elif count_j == 3 :
            if types[idx] == 'full_house' :
                types[idx] = '5_kind'
            elif types[idx] == '3_kind' :
                types[idx] = '4_kind'

        elif count_j == 4 :
            types[idx] = '5_kind'

    return types


data = read('day7.txt')
types = get_hand_type_2(data)
hands = [hands + [type] for hands,type in zip(data,types)]
hands = sorted(hands,key = cmp_to_key(compare_2),reverse=False)
value = sum([hand[1]*(rank+1) for rank,hand in enumerate(hands)])
print(value)

