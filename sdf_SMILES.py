import os
from rdkit import Chem

def sdf_to_smiles(sdf_file, output_dir='uploads'):
    try:
        suppl = Chem.SDMolSupplier(sdf_file)
        mols = [x for x in suppl if x is not None]
        print(f"Total Molecules: {len(mols)}")

        # Define the output SMILES file path
        base_name = os.path.splitext(os.path.basename(sdf_file))[0]
        smiles_file = os.path.join(output_dir, f"{base_name}.smi")

        # Write molecules to the SMILES file
        with Chem.SmilesWriter(smiles_file, includeHeader=False) as w:
            for m in mols:
                w.write(m)

        return smiles_file
    except Exception as e:
        raise RuntimeError(f"Error processing SDF file: {e}")

