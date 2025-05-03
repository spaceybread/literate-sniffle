from string import ascii_lowercase

starts = {l : [] for l in ascii_lowercase}
ends = {l : [] for l in ascii_lowercase}


with open("filtered_list.txt") as f:
  for xi in f:
    x = xi.strip()
    starts[x[0]].append(x)
    ends[x[-1]].append(x)


for a in starts.keys():
    print(starts[a])
    print(ends[a])
