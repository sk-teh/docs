mekiFunction
============

.. py:attribute:: Cmpr

    .. image:: _static/cmpr.png
        :width: 300
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

.. py:attribute:: Count

    .. image:: _static/count.png
        :width: 300
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

.. py:attribute:: Freq

    .. image:: _static/freq.png
        :width: 300
        :alt: Frequency component

    **Freq** is used to calculate the changing frequency of a boolean value.

    :param Pps: The changes in the frequency per second
    :type Pps: real
    :param Ppm: The changes in the frequency per minute
    :type Ppm: real
    :param In: Input value
    :type In: boolean

.. py:attribute:: Hysteresis

    .. image:: _static/hysteresis.png
        :width: 300
        :alt: Hysteresis component

    **Hysteresis** can output a boolean value according to thier rising edge and falling edge limit.

    :param In: Input value
    :type In: real    
    :param Out: Output value
    :type Out: boolean
    :param Rising_Edge: Rising edge limit, **Out** become *true* when **In** greater than it 
    :type Rising_Edge: real
    :param Falling_Edge: Falling edge limit, **Out** become *false* when **In** less than it
    :type Falling_Edge: real

.. py:attribute:: IRamp

    .. image:: _static/iramp.png
        :width: 300
        :alt: IRamp component

    **IRamp** provides linear ramping output based on time set.

    :param Out: Output value
    :type Out: integer
    :param Min: Start value of the ramping
    :type Min: integer
    :param Max: End value of the ramping
    :type Max: integer
    :param Delta: Value change every time
    :type Delta: integer
    :param Secs: Time intervals very time change
    :type Secs: integer, second