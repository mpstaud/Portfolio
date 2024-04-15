# Ohm's law V = IR

def voltage(i, r):
  volt = i * r
  return volt

def current(v, r):
  cur = v / r
  return cur

def resistance(v, i):
  res = v / i
  return res

def main():
  circuit_type = input('Press S for Series, P for Parallel, C for a combination of the 2: ')
  if circuit_type == 'S':
    res_num_series = input('How many resistors do you have? ')
    
    
  
