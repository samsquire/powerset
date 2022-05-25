# from stackoverflow
# https://stackoverflow.com/a/41626844/10662977
def pset(myset):
  if not myset: # Empty list -> empty set
    return [set()]

  r = []
  for y in myset:
    sy = set((y,))
    for x in pset(myset - sy):
      if x not in r:
        r.extend([x, x|sy])
  return r

# print(pset(set([1,2,3])))

# pset2 Samuel Squire's implementation
# based on recursive set definition

def intersect(collection, items):
  for item in items:
    if sorted(item) not in collection:
      collection.append(sorted(item))
      


def pset2(myset):
  if not myset:
    return []
    
  # F (e, T) = { X ∪ {e} | X ∈ T }
  def F(e, myset):
    intermediary = []
    
    for outer in myset:
      new = [e]
      for inner in myset:
        if inner != e:
          new.append(inner)
      intermediary.append(new)
    return intermediary
# T = S\{e} (where \ means relative complement or subtraction)
    # P(S) = P(T) ∪ F ( e, P(T))
  

  T = []
  for item in myset:
    
      
      Tgroup = []
      for inneritem in myset:
        
        
        if inneritem != item:
          Tgroup.append(inneritem)
      
      T.append(Tgroup)


  
  # for item in myset:  
    
  #   items = []
  #   print(T)
  sets = []
  
  for Tgroup in T:
      if Tgroup:
        intersect(sets, [Tgroup])

  
  
  for Tgroup in T:
    sublist = pset2(Tgroup)
    for item in myset:
      intersect(sets, F(item, myset))
    
    if sublist:
      
      
      intersect(sets, sublist)
  
  
  #   items.extend(sublist)
  #   sets.append(items)
  return sets

# print(pset2([1,2,3]))
items = pset2([1,2,3])
results = []
print(items)
for item in items:
  for subitem in item:
    results.append(subitem)
print(len(results))
