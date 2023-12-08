###########
JSON Schema
###########

About
=====

Instead of representing mzPAF as a single string, it can alternatively be expressed as a JSON
object. This format is more compatible for inter-program communication, especially through web
APIs. You can find the JSON schema for mzPAF on GitHub via the following link:

https://raw.githubusercontent.com/HUPO-PSI/mzPAF/main/specification/annotation-schema.json

Replace ``main`` in the URL with the desired version tag to access the schema for a particular
version.

Examples
========

.. literalinclude:: ../../../specification/annotation-example-1.json
    :language: json

.. literalinclude:: ../../../specification/annotation-example-2.json
    :language: json

.. literalinclude:: ../../../specification/annotation-example-3.json
    :language: json



Full schema documentation
=========================

.. include:: ../../../specification/annotation-schema.md
   :parser: myst_parser.sphinx_
   :start-line: 4
