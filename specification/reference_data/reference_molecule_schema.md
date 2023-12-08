# HUPO-PSI mzSpecLib reference molecule and ion list

*Describe reference molecules or ions found in spectral libraries*

## Pattern Properties

- **`.{1,}`**: Refer to *[#/definitions/molecule](#definitions/molecule)*.
## Definitions

- <a id="definitions/molecule"></a>**`molecule`** *(object)*: A single molecule that may be present as a reporter ion or signature ion, or be a component of a neutral loss.
  - **`name`** *(string)*: The formal name for this molecule by which it should be referenced.
  - **`cv_term`** *(array)*
    - **Items** *(string)*
  - **`neutral_mass`** *(number)*: The neutral mass of the molecule not including any charge or charge carrier.
  - **`molecule_type`** *(string)*: A categorical label for this molecule.

    Examples:
    ```json
    "monosaccharide"
    ```

    ```json
    "reporter"
    ```

    ```json
    "reporter+balance"
    ```

  - **`ion_mz`** *(number)*: The m/z of the molecule if it is expected to be reasonably different from the uncharged version.
  - **`chemical_formula`** *(string)*: The elemental formula of the neutral molecule.
  - **`ion_chemical_formula`** *(string)*: The chemical formula of the charged molecule.
  - **`references`** *(array)*: An array of sources and references describing this entity.
    - **Items** *(string)*
