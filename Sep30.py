#%% returns a dictionary that gives the number of people in each party.
def party_count():
  from collections import defaultdict
  d = defaultdict(int)

  with open("voter_data.txt") as f:
    header = f.readline().split(',')
    
    for i in range(len(header)):
      if header[i] == 'PARTY':
        a = i
    
    for voter in f:
      voter = voter.split(',')
      d[voter[a]] += 1

  print(d)  
  return d

#%% returns a dictionary that for each party gives the average age of people in the party.
#You should use a python function to find the current year; don't hard-code the current year in the code.
def average_age():
    from collections import defaultdict
    from datetime import datetime
    current_year = datetime.now().year

    d = defaultdict(lambda:{'sum_ages':0,'count':0})

    with open("voter_data.txt") as f:
        header = f.readline().split(',')
        
        for i in range(len(header)):
            if header[i] == 'PARTY':
                a = i
            if header[i] == 'DATE OF BIRTH':
                b = i
        
        for voter in f:
            voter = voter.split(',')
            oldSumAges = d[voter[a]]['sum_ages']
            oldCount = d[voter[a]]['count']
            d[voter[a]] ={
                'sum_ages': oldSumAges + current_year - int(d[voter[b]]),
                'count': oldCount + 1
            }

        for party in d:
            avg = d[party]['sum_ages'] / d[party]['count']
            print (party, avg)

#%% find the percent of republicans and percent of democrats that voted in the 2018 general election and not the 2016 general election. You should return the
#data as a tuple, with the republican data first.
def g2018_not_g2016():
  pass


#Find the names of people who have voted for a different party than the party they are currently registered with. Note that an X should be ignored
#in the voting data, since this doesn't indicate a different party. You should return a set of strings. The strings should be the concatenation of
#the first name, first intial of the middle name and last name. Also include the suffix and the end of the name, if the person has one.
def diff_party():
  pass

