def comp(S):
  Nucleotide = ""
  for DNA in S:
    if DNA == 'G':
      Nucleotide += 'C'
    elif DNA == 'C':
      Nucleotide += 'G'
    elif DNA == 'A':
      Nucleotide += 'T'
    elif DNA == 'T':
      Nucleotide += 'A'
  return Nucleotide
  
print(comp("ATCAAGGCCTATTCCGGGAAAGG"))
