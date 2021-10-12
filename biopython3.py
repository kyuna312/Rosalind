def reverse_complement(seq):
	ntComplement = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
	revSeqList = list(reversed(seq))
	revComSeqList = [ntComplement[k] for k in revSeqList]
	revComSeq = ''.join(revComSeqList)
	return revComSeq
seq = ''
with open('rosalind_revc (1).txt') as f:
	for line in f:
		line = line.rstrip()
		seq += line.upper()

f= open("hariu.txt","w+")
f.write(reverse_complement(seq))	











