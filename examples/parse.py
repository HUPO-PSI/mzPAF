#!/usr/bin/env python3
import sys
import json

from mzpaf import parse_annotation

data_model = {"m/z array": [], "intensity array": [], "annotations": []}

for i, line in enumerate(sys.stdin):
    if line.startswith("#"):
        continue
    tokens = line.strip().split(" ")
    if tokens:
        index, mz, intensity, annotation_text = filter(bool, tokens)
        annotations = parse_annotation(annotation_text)
        data_model['m/z array'].append(float(mz))
        data_model['intensity array'].append(float(intensity))
        data_model["annotations"].append([annot.to_json() for annot in annotations])

print(json.dumps(data_model, sort_keys=True, indent=2))