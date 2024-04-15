# Ohm's law V = IR
resistors = []
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
    for i in range(0, res_num_series):
      resistance = input("Enter the resistance in Ohms for this resistor")
      resistors.append(resistance)
    total_resistance = sum(resistors)
    
      


    
    
  
