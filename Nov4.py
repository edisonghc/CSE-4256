h = [20,16,25,10,35,40,20,10]

p = [1,5,8,9,10,17,17,20]
c = {}

# def rod(n):


# def rod_helper(n,memo):
#     if memo.get(n):
#         return memo[n]
#     else:
#         memo[n]
#         return 

def sum(a):
    rs = 0
    for i in range(len(a)):
        rs += a[i]
    return rs

def h_v(h):
    memo = {}
    return h_v_helper(h,memo)

def take_out(i,a):
    if i == 0:
        return a[1:]
    elif i == len(a)-1:
        return a[:len(a)-1]
    else:
        return a[:i-1]+a[i+2:]

def h_v_helper(h,memo):
    if memo.get(h):
        return memo[h]
    else:
        for i in range(len(h)):
            result = h[i] + h_v_helper(take_out(i,h))
            memo[h] = result
        return max(memo)


def house_robber(h):
  d = dict()
  holdMax = 0

  for i in range(len(h)):
    curVal = h[i]

    if i == 0:
      holdMax = curVal
    elif i == 1:
      if curVal > holdMax:
        holdMax = curVal
    else:
      if(curVal + d[i-2] > holdMax):
        holdMax = curVal + d[i-2]
       

    d[i] = holdMax
  return holdMax

h = [20,16,25,10,35,40,20,10]
print(house_robber(h))