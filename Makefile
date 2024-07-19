
all: publish-references

publish-references:
	cp ./specification/reference_data/reference_molecules.json ./implementations/python/mzpaf/data/reference_molecules.json
	cd ./specification/reference_data/ && python reference_mol_to_md.py