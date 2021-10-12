file = open('rosalind_rna.txt','r')
dna = file.read()
#defining my new 'transcribe' function
def transcribe(dna):
  return dna.replace('T', 'U')
  
#defining 'RNA_string'  
rna = transcribe(dna)

#printing result of transcribing DNA_string into RNA_string
print (rna)
