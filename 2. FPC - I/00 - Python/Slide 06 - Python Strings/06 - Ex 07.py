dna = "AGCT"
rna_m = ""

for letra in dna:
    if letra == "A":
        rna_m += "U"

    elif letra == "G":
        rna_m += "C"

    elif letra == "C":
        rna_m += "G"
        
    elif letra == "T":
        rna_m += "A"

print(rna_m)
