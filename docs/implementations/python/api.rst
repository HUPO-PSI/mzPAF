**********
Python API
**********

.. automodule:: mzpaf
    :members:
    :imported-members:


    .. manually documented as parse_annotation is undocumented

    .. function:: parse_annotation

        Parse a string into one or more :class:`IonAnnotationBase` instances.

        Parameters
        ----------
        annotation_string : str
            The string to be parsed
        wrap_errors : bool, optional
            Whether or not to capture parsing errors as :class:`InvalidAnnotation` or not. Defaults to :const:`False`.

        Returns
        -------
        list[:class:`IonAnnotationBase`] :
            The annotations parsed

        See Also
        --------
        :class:`mzpaf.AnnotationStringParser`