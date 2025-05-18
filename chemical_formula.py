print("let's find out chemical bond formula ")
import pubchempy as pcp

chemical_name=input("Enter the name of chemial to find formula: ")

try:
    compound=pcp.get_compounds(chemical_name,"name")[0] 
    # print(compound)
    print(f"IUPAC name:{compound.iupac_name}")
    print(f"common name:{compound.synonyms[0]}")
    print(f"MOleculer weight:{compound.molecular_weight}")
    print(f"Molecular formula:{compound.molecular_formula}")
except IndexError:
    print(f"No information found for {chemical_name}")


