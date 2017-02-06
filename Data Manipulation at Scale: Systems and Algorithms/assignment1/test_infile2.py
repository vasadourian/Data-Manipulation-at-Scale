sent_file = open('AFINN-111.txt')

per_row = []
for line in sent_file:
    per_row.append(line.strip().split('\t'))

per_column = zip(*per_row)

scored_words = list(per_column[0])

scored_nums = list(per_column[1])

scored_dict = dict(zip(scored_words, scored_nums))


print scored_dict
