mekiPriority
============

.. py:attribute:: PriortyBinary

    .. image:: _static/img/priorty/priortybinary.png
        :width: 250
        :alt: PriortyBinary component

    **PriortyBinary** provide NULL **Out** during **Enable** is false. When **Enable** is true, **Out** equal to **In** in Boolean.

    :param Out: Equal to NULL when **Enable** is *false*, otherwise equal to **In** when **Enable** is *true*
    :type Out: option
    :param In: Input value
    :type In: boolean
    :param Enable: Enables the component
    :type Enable: boolean

.. py:attribute:: PriortyFloat

    .. image:: _static/img/priorty/priortyfloat.png
        :width: 250
        :alt: PriortyFloat component

    **PriortyFloat** provide NULL **Out** during **Enable** is false. When **Enable** is true, **Out** equal to **In** in Boolean.

    :param Out: Equal to NULL when **Enable** is *false*, otherwise equal to **In** when **Enable** is *true*
    :type Out: option
    :param In: Input value
    :type In: real
    :param Enable: Enables the component
    :type Enable: boolean