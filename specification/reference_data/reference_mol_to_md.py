import pandas as pd

df = pd.read_json("reference_molecules.json")
df.T.to_markdown("reference_molecules.md")