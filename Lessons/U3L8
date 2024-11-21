def validate(S):
  for i in range(len(S)):
    if not (S[i] == "C" or S[i] == "G" or S[i] == "A" or S[i] == "T"):
      print("Not valid: %s found in position %d." % (S[i], i + 1))  
      return False
  return True
  
if validate("ATCAAGGCCTATTCCGGGAAAGG"):
  print("Valid")
  
if validate("TAGWGTGAAGTGCCATAGTT"):
  print("Valid")
  
if validate("CGCAGATGCCGCTGGTATGA"):
  print("Valid")
    
if validate("ATAGGTTAGCGGACCGAGAC"):
  print("Valid")
