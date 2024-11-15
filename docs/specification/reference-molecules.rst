###################
Reference molecules
###################

About
=====

.. include:: ../../specification/reference_data/README.md
   :parser: myst_parser.sphinx_
   :start-line: 2
   :end-line: -1
..
   skip including title and last line with reference to this page

See :ref:`Reference molecule ions` in the specification document for more information.


Reference molecule table
========================

The following analytes can be annotated as reference molecules with the ``r`` prefix and the
listed name between square brackets (e.g. ``r[TMT127N]``).

.. include:: ../../specification/reference_data/reference_molecules.md
   :parser: myst_parser.sphinx_


JSON schema
===========

The ``reference_molecules.json`` file is defined by the following schema:

.. include:: ../../specification/reference_data/reference_molecule_schema.md
   :parser: myst_parser.sphinx_
   :start-line: 3
