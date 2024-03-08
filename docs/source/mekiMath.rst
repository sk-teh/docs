mekiMath
========

.. py:attribute:: Add2
    
    .. image:: _static/img/math/add2.png
        :width: 250
        :alt: Add2 component

    **Add2** performs sum of inputs.
    
    .. math::
        Out  =  In1 + In2 
    
    :param Out: Output value of adding **In1** and **In2**
    :type Out: real
    :param In1: Input value 1
    :type In1: real
    :param In2: Input value 2
    :type In2: real

.. py:attribute:: Avg10

    .. image:: _static/img/math/avg10.png
        :width: 250
        :alt: Avg10 component

    **Avg10** performs the division in 10 for the last 10 input value.
    It will sample current value again if it does not change in max time (ms) duration.

    .. math::
       Out = \frac{ΣIn} {10}

    :param Out: Average output value of last 10 **In**
    :type Out: real
    :param In: Input value 
    :type In: real
    :param MaxTime: Maximum time of sampling period
    :type MaxTime: integer

.. py:attribute:: AvgN

    .. image:: _static/img/math/avgn.png
        :width: 250
        :alt: AvgN component

    **AvgN** perform the equation below. 
    The purpose is to make the output to have certain proportion inherits the input value and the previous output value.
    
    .. math::
       Out = 1* \frac{In}{DF} + \frac{(DF-1)*Out}{DF}

    DF=Damping Factor
    
    For example,
    In=A, Last output=B, DF =16
    
    .. math::
       Out = \frac{A}{16} + \frac{15B}{16}
    
    :param Out: Average output value with damping factor
    :type Out: real
    :param In: Input value 
    :type In: real
    :param DampingFactor: Decay factor (1-max)
    :type DampingFactor: integer

.. py:attribute:: Ceiling

    .. image:: _static/img/math/ceiling.png
        :width: 250
        :alt: Ceiling component

    **Ceiling** performs the least integer that is greater than or equal to the input.

    .. math::
       Out = ⌈In⌉

    :param Out: Ceiling output of **In**
    :type Out: real
    :param In: Input value 
    :type In: real

.. py:attribute:: Div2

    .. image:: _static/img/math/div2.png
        :width: 250
        :alt: Div2 component

    **Div2** performs division operation.

    .. math::
       Out = \frac{dividend} {divisor}

    :param Out: Result of divided **Divided** by **Divisor**
    :type Out: real
    :param Dividend: Input value 
    :type Dividend: real
    :param Divisor: Input value
    :type Divisor: real
    :param Div0: Equal to true when dividend=0, otherwise Div0=false (read only)
    :type Div0: boolean

.. py:attribute:: Exp

    .. image:: _static/img/math/exp.png
        :width: 250
        :alt: Exp component

    **Exp** performs the exponential function on the input.

    .. math::
       Out = e^{In}

    :param Out: Exponential value of **In**
    :type Out: real
    :param In: Input value 
    :type In: real
    
.. py:attribute:: Fabs

    .. image:: _static/img/math/fabs.png
        :width: 250
        :alt: Fabs component

    **Fabs** performs the absolute value on the input.

    .. math::
       Out = |{In}|

    :param Out: Absolute value of **In**
    :type Out: real
    :param In: Input value 
    :type In: real

.. py:attribute:: FloatOffset

    .. image:: _static/img/math/floatOffset.png
        :width: 250
        :alt: FloatOffset component

    **FloatOffset** adjusts the output value on top of the offset.

    .. math::
       Out = In  + offset

    :param Out: Output value off adding **In** and **Offset**
    :type Out: real
    :param In: Input value 
    :type In: real
    :param Offset: Input value 
    :type Offset: real

.. py:attribute:: Floor

    .. image:: _static/img/math/floor.png
        :width: 250
        :alt: Floor component

    **Floor** performs the greatest integer that is less than or equal to the input.

    .. math::
       Out = ⌊In⌋ 

    :param Out: Floor result of **In** 
    :type Out: real
    :param In: Input value 
    :type In: real
    
.. py:attribute:: Inverse

    .. image:: _static/img/math/inverse.png
        :width: 250
        :alt: Inverse component

    **Inverse** takes the inverse of input.

    .. math::
       Out = \frac{1}{In} 

    :param Out: Inverse of **In** 
    :type Out: real
    :param In: Input value 
    :type In: real

.. py:attribute:: Log

    .. image:: _static/img/math/log.png
        :width: 250
        :alt: Log component

    **Log** performs the natural logarithm of input.

    .. math::
       Out = log(In)

    :param Out: Natural logarithm of **In** 
    :type Out: real
    :param In: Input value 
    :type In: real

.. py:attribute:: Log10

    .. image:: _static/img/math/log10.png
        :width: 250
        :alt: Log10 component

    **Log10** performs the base 10 logarithm of input.

    .. math::
       Out = log_{10}(In)

    :param Out: Base 10 logarithm of **In** 
    :type Out: real
    :param In: Input value 
    :type In: real

.. py:attribute:: Max

    .. image:: _static/img/math/max.png
        :width: 250
        :alt: Max component

    **Max** compares two input values, thus outputs the larger one.

    :param Out: Output the higher value in between **In1** and **In2**
    :type Out: real
    :param In1: Input value 1
    :type In1: real
    :param In2: Input value 2
    :type In2: real

.. py:attribute:: Min

    .. image:: _static/img/math/min.png
        :width: 250
        :alt: Min component

    **Min** compares two input values, thus outputs the smaller one.

    :param Out: Output the lower value in between **In1** and **In2**
    :type Out: real
    :param In1: Input value 1
    :type In1: real
    :param In2: Input value 2
    :type In2: real

.. py:attribute:: MinMax

    .. image:: _static/img/math/minmax.png
        :width: 250
        :alt: MinMax component

    **MinMax** records the maximum and the minimum of the input value, min out outputs the minimum record while max out outputs the maximum record respectively, until they are updated.

    :param MinOut: Min recorded **In** value
    :type MinOut: real
    :param MaxOut: Max recorded **In** value
    :type MaxOut: real
    :param In: Input value 
    :type In: real
    :param Reset: Reset record value back to 0
    :type Reset: boolean

.. py:attribute:: Mul2

    .. image:: _static/img/math/mul2.png
        :width: 250
        :alt: Mul2 component

    **Mul2** performs multiplication operation.

    .. math::
       Out = In1 × In2

    :param Out: Multiplication of **In1** with **In2**
    :type Out: real
    :param In1: Input value 1
    :type In1: real
    :param In2: Input value 2
    :type In2: real

.. py:attribute:: Pow

    .. image:: _static/img/math/pow.png
        :width: 250
        :alt: Pow component

    **Pow** performs the y power of x.

    .. math::
       Out = X^{Y}

    :param Out: Result of **Y** power of **X**
    :type Out: real
    :param X: Input value 1
    :type X: real
    :param Y: Input value 2
    :type Y: real

.. py:attribute:: Neg

    .. image:: _static/img/math/neg.png
        :width: 250
        :alt: Neg component

    **Neg** negates the input value.

    .. math::
       Out = - In

    :param Out: Negative value of **In**
    :type Out: real
    :param In: Input value
    :type In: real
    
.. py:attribute:: Round

    .. image:: _static/img/math/round.png
        :width: 250
        :alt: Round component

    **Round** rounds the input value, can retain some digits according to the rounding algorithm.

    :param Out: Rounding **In** value with **DecimalPlaces**
    :type Out: real
    :param In: Input value
    :type In: real
    :param DecimalPlaces: Retains decimal point
    :type DecimalPlaces: integer

.. py:attribute:: Squareroot

    .. image:: _static/img/math/squareroot.png
        :width: 250
        :alt: Squareroot component

    **Squareroot** performs square rooted of input.

    .. math::
       Out = \sqrt{In}

    :param Out: square rooted value of **In**
    :type Out: real
    :param In: Input value
    :type In: real

.. py:attribute:: Sub2

    .. image:: _static/img/math/sub2.png
        :width: 250
        :alt: Sub2 component

    **Sub2** performs subtraction operation.

    .. math::
       Out = minuend - subtrahend

    :param Out: Subtraction of **Minuend** to **Subtrahend**
    :type Out: real
    :param Minuend: Input value 
    :type Minuend: real 
    :param Subtrahend: Input value
    :type Subtrahend: real 

.. py:attribute:: TimeAvg

    .. image:: _static/img/math/timeavg.png
        :width: 250
        :alt: TimeAvg component

    **TimeAvg** averages "In" over the configured time. The actual time is marked in a resolution of scan period such that number of sample.
    The out is NOT a running average, this object caches the average over the previous time as the out value, and updates out every "time" ms. 
    Until a full time cycle has elapsed, the out is set to the average off all samples collected up until that point. 

    .. math::
        Out = \frac{Time * In}{ScanPeriod}

    :param Out: Average of **In** over configured time
    :type Out: real
    :param In: Input value to be taken average
    :type In: real 
    :param Time: The time period over which to average the in value to get the out value
    :type Time: integer 
    :param ScanPeriod: Cycle of sampling data, units is ms
    :type ScanPeriod: integer