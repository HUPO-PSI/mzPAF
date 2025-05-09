# HUPO-PSI mzSpecLib reference molecule and ion list

*Describe reference molecules or ions found in spectral libraries*

## Pattern Properties

- <a id="patternProperties"></a>**`.{1,}`**: Refer to *[#/definitions/molecule](#definitions/molecule)*.
## Definitions

- <a id="definitions/molecule"></a>**`molecule`** *(object)*: A single molecule that may be present as a reporter ion or signature ion, or be a component of a neutral loss.
  - <a id="definitions/molecule/properties/name"></a>**`name`** *(string)*: The formal name for this molecule by which it should be referenced.
  - <a id="definitions/molecule/properties/cv_term"></a>**`cv_term`** *(array)*
    - <a id="definitions/molecule/properties/cv_term/items"></a>**Items** *(string)*
  - <a id="definitions/molecule/properties/neutral_mass"></a>**`neutral_mass`** *(number)*: The neutral mass of the molecule not including any charge or charge carrier.
  - <a id="definitions/molecule/properties/molecule_type"></a>**`molecule_type`** *(string)*: A categorical label for this molecule.

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

  - <a id="definitions/molecule/properties/ion_mz"></a>**`ion_mz`** *(number)*: The m/z of the molecule if it is expected to be reasonably different from the uncharged version.
  - <a id="definitions/molecule/properties/chemical_formula"></a>**`chemical_formula`** *(string)*: The elemental formula of the neutral molecule.
  - <a id="definitions/molecule/properties/ion_chemical_formula"></a>**`ion_chemical_formula`** *(string)*: The chemical formula of the charged molecule.
  - <a id="definitions/molecule/properties/references"></a>**`references`** *(array)*: An array of sources and references describing this entity.
    - <a id="definitions/molecule/properties/references/items"></a>**Items** *(string)*
