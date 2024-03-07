mekiFunction
============

.. py:attribute:: Cmpr

    .. image:: _static/img/func/cmpr.png
        :width: 250
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

    .. image:: _static/img/func/count.png
        :width: 250
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

    .. image:: _static/img/func/freq.png
        :width: 250
        :alt: Frequency component

    **Freq** is used to calculate the changing frequency of a boolean value.

    :param Pps: The changes in the frequency per second
    :type Pps: real
    :param Ppm: The changes in the frequency per minute
    :type Ppm: real
    :param In: Input value
    :type In: boolean

.. py:attribute:: Hysteresis

    .. image:: _static/img/func/hysteresis.png
        :width: 250
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

    .. image:: _static/img/func/iramp.png
        :width: 250
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

.. py:attribute:: Limiter

    .. image:: _static/img/func/limiter.png
        :width: 250
        :alt: Limiter component

    **Limiter** limits the output according to the upper limit and lower limit.

    :param Out: Output value
    :type Out: real
    :param In: Input value
    :type In: real
    :param lowLmt: Lower limit for **Out**
    :type lowLmt: real
    :param highLmt: Upper limit for **Out**
    :type highLmt: real

.. py:attribute:: Linearize

    .. image:: _static/img/func/linearize.png
        :width: 250
        :alt: Linearize component

    **Linearize** defines 8 sets of corresponding data, and calculate the output value according to the input value with linearization data.

    :param Out: Output value
    :type Out: real
    :param In: Input value
    :type In: real
    :param x0-x9: Range for **In**
    :type x0-x9: real
    :param y0-y9: Range of converted **Out**
    :type y0-y9: real

.. py:attribute:: Ramp

    .. image:: _static/img/func/ramp.png
        :width: 250
        :alt: Ramp component

    **Ramp** provides a triangle or sawtooth type ramping output.

    :param Out: Output value
    :type Out: real
    :param Min: Minimum value of the ramping **Out**
    :type Min: real
    :param Max: Maximum value of the ramping **Out**
    :type Max: real
    :param Period: The time for one complete **Min** / **Max** in second for ramp **Out**, range from 0 to 65535 
    :type Period: integer, second
    :param ScanPeriod: The time for **Out** updating interval, range from 100 to 65535
    :type ScanPeriod: integer, millisecond
    :param RampType: Ramp type, *triangle* or *sawtooth*
    :type RampType: option

.. py:attribute:: SRLatch

    .. image:: _static/img/func/srlatch.png
        :width: 250
        :alt: SRLatch component

    **SRLatch** keeps output value to true as long as the set value is true, until the reset is triggered.   

    :param Out: Output value
    :type Out: boolean
    :param Set: Triggers to set **Out** to *true*
    :type Set: boolean
    :param Reset: Triggers to restore **Out** back to *false*
    :type Reset: boolean

.. py:attribute:: TickTock

    .. image:: _static/img/func/ticktock.png
        :width: 250
        :alt: TickTock component

    **TickTock** outputs *true* and *false* values alternately according to the frequency

    :param Out: Constantly change between *true* and *false*
    :type Out: boolean
    :param TickPerSec: Change frequency of **Out**, range from 1 to 10
    :type TickPerSec: integer

.. py:attribute:: UpDn

    .. image:: _static/img/func/updn.png
        :width: 250
        :alt: UpDn component

    **UpDn** records the changes of the input value, the record number can be documented in increasing or reducing order. The records can be reset too.

    :param Out: Output Value
    :type Out: real
    :param Ovr: *true* when **Out** is greater than **Limit**
    :type Ovr: boolean
    :param In: Input Value
    :type In: boolean
    :param Rst: Triggers to restore **Out** to *0*
    :type Rst: boolean
    :param CDwn: The trend of recorded **Out**, either *Up* or *Down*
    :type CDwn: option
    :param Limit: Limits **Out** when **HoldAtLimit** is *true*
    :type Limit: real
    :param HoldAtLimit: Enable the **Limit** function
    :type HoldAtLimit: boolean