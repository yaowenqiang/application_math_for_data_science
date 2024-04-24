coin_outcomes = ['H', 'T']
die_outcomes = [1,2,3,4,5,6]

all_combinations = [(c,d) for c in coin_outcomes for d in die_outcomes]

head_and_6 = [t for t in all_combinations if t[0] == 'H' and t[1] == 6]

print(float(len(head_and_6)) / float(len(all_combinations)))