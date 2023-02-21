mekiFunction
============

.. py:data:: Cmpr

    .. image:: _static/cmpr.png
        :width: 400
        :alt: Compare component

    **Cmpr** is used to compare two input values.   

    :param Xgy: *true* when **X** is greater than **Y**, else *false*
    :type Xgy: boolean
    :param Xey: *true* when **X** is equal to **Y**, else *false*
    :type Xey: boolean
    :param Xly: *true* when **X** is less than **Y**, else *false*
    :type Xly: boolean
    :param X: Input value
    :type X: real
    :param Y: Input value
    :type Y: real

.. py:data:: Count

    .. image:: _static/count.png
        :width: 400
        :alt: Count component

    **Count** is used to count the transistion of a boolean value from *false* to *true*.

    :param Out: Number of times *In* has transitioned from *false* to *true*
    :type Out: integer
    :param In: Input value
    :type In: boolean
    :param Present: Presets the counter to a specific value, defaults to 0
    :type Present: integer
    :param Dir: Count direction, *true* for up while *false* for down
    :type Dir: boolean
    :param Enable: To enable **In** counting
    :type Enable: boolean
    :param Reset: If *true*, **out** = **preset** and no counting. It act as a reset switch
    :type Reset: boolean