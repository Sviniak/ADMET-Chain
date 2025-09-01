from rdkit import Chem
from rdkit.Chem import Draw

#m = Chem.MolFromMolFile('SFAHFA-S-34.mol') #Define the variable m to have the value of the mol file
suppl = Chem.SDMolSupplier('LC_GPCR_Receptor_Based_Targeted_Library.sdf')
mols = [x for x in suppl]
print("Total Molecules are:", len(mols))

with Chem.SmilesWriter('LC_GPCR_Receptor_Based_Targeted_Library.smi', includeHeader=False) as w: #w defined var
    for m in mols:
        w.write(m) 

# m = Chem.MolFromMolFile('SFAHFA-S-34.mol') #Define the variable m to have the value of the mol file
# m_new = Chem.MolToSmiles(m, isomericSmiles=False) #execute the function here'
# print("SMILES:", m_new)
# img = Draw.MolToImage(m) #call the Draw function and set it = to img
# img.show() #Show the image in PIL 

