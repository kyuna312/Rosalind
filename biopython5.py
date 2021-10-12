def Compute_GC (seq):
    GC = 0
    total =0
    for i in range(0, len(seq)):
        if seq[i] in ['A','T','G','C']:
            total = total +1
        if seq[i] in ['G', 'C']:
            GC = GC+1
    return float(GC)/total*100
 
def getMaxIndex(my_list):
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return my_list.index(max)
 
file=open('rosalind_gc.txt','r')
id=list()
GC=list()
long_seq=''
nowlen=1
for seq in file.readlines():
        #print(seq)
        if(seq.startswith('>')):
            id.append(seq.lstrip('>'))
        else:
            seq=seq.rstrip('\n')
            long_seq=long_seq+seq
            #print(long_seq)
        if(len(id)>nowlen):
            nowlen=len(id)
            GC.append(Compute_GC(long_seq))
            long_seq=''
GC.append(Compute_GC(long_seq))
#print(long_seq)
no=getMaxIndex(GC)
print(id[no])
print("%.6f"%GC[no])

