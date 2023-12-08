**********
Python API
**********

.. manually documented as parse_annotation is undocumented (returned by the AnnotationStringParser
   class)

.. function:: mzpaf.parse_annotation(annotation_string: str)

   Parses an mzPAF string into a list of ion annotations.

   :param annotation_string: mzPAF string with peak annotations.
   :type annotation_string: str
   :returns: A list of annotations.
   :rtype: list[mzpaf.IonAnnotationBase]

.. automodule:: mzpaf
   :members:
   :imported-members:
