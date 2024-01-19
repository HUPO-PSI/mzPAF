*************
Example Usage
*************

.. code-block:: python

    import mzpaf

    annotations: list[mzpaf.IonAnnotationBase] = mzpaf.parse_annotation("y1")

    annot: mzpaf.PeptideFragmentIonAnnotation = annotation[0]
    assert annot.series == 'y'
    assert annot.position == 1
    assert annot.charge == 1