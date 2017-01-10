def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count
#print 'test'
#print "the count of patter 'CGCG' is ", PatternCount("CGCG","CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC")

def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    return FrequentPatterns

#print "most frequent 3-mer of 'CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT'? is", FrequentWords('CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT', 3)

def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates 

def remove_duplicates(Items):
    ItemsNoDuplicates = [] # output variable
    # your code here
    for item in Items:
        if item not in ItemsNoDuplicates:
            ItemsNoDuplicates.append(item)
    return ItemsNoDuplicates
'''
Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"

k = 10

print FrequentWords(Text,k)
'''
def ReverseComplement(Pattern):
    revComp = '' # output variable
    # your code here
    revComp = reverse(Pattern)
    return revComp



def ReverseComplement(Pattern):
    revComp = '' # output variable
    # your code here
    revComp = reverse(Pattern)
    return revComp


# Copy your reverse function from the previous step here.
def reverse(text):
    text_fi = ""
    for x in range(0, len(text)):
        text_fi += text[len(text) - 1 - x]
    return text_fi

# HINT:   Filling in the following function is optional, but it may come in handy when solving ReverseComplement
# Input:  A character Nucleotide
# Output: The complement of Nucleotide
def complement(Nucleotide):
    comp = '' # output variable
    # your code here
    for x in range(0,len(Nucleotide)):
        if Nucleotide[x] == "A":
            comp += "T"
        elif Nucleotide[x] == "T":
            comp += "A"
        elif Nucleotide[x] == "G":
            comp += "C"
        else:
            comp += "G"    
    return comp

Nucleotide = "ACACAC"
print complement(ReverseComplement("GCTAGCT"))
#print complement(ReverseComplement(Nucleotide))

def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    # your code here
    for x in range(0,len(Genome) - len(Pattern) + 1):
        if Genome[x:x+len(Pattern)] == Pattern:
            positions.append(x)
    return positions

