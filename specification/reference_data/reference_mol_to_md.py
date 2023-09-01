import pandas as pd

df = pd.read_json("reference_molecules.json").T
buf = df.T.to_markdown().replace(' nan ', '     ')

with open('./reference_molecules.md', 'wt') as fh:
    fh.write(buf)