mekiTiming
==========

.. py:attribute:: DlyOff

    .. image:: _static/img/timing/dlyoff.png
        :width: 250
        :alt: DlyOff component
    
    **DlyOff** delays the on to off transition by a time delay.

    :param Out: Output value
    :type Out: boolean
    :param In: Input value
    :type In: boolean
    :param DelayTime: Delays time from on to off transition, units is second(s)
    :type DelayTime: integer
    :param Hold: Countdown of delay time, units is millisecond(ms)
    :type Hold: integer

.. py:attribute:: DlyOn

    .. image:: _static/img/timing/dlyon.png
        :width: 250
        :alt: DlyOn component

    **DlyOn** delays the off to on transition by a time delay.

    :param Out: Output value
    :type Out: boolean
    :param In: Input value
    :type In: boolean
    :param DelayTime: Delays time from off to on transition, units is second(s)
    :type DelayTime: integer
    :param Hold: Countdown of delay time, units is millisecond(ms)
    :type Hold: integer

.. py:attribute:: OneShot

    .. image:: _static/img/timing/oneshot.png
        :width: 250
        :alt: OneShot component

    **OneShot** generating boolean one-shot pulse. 
    **Out** = *true* for **pulseWidth** sec, beginning at rising edge of **In**, the pulse retriggers on each rising edge of **In**, when **canRetrig** = *true*. 

    :param Out: Output value
    :type Out: boolean
    :param In: Input value
    :type In: boolean
    :param PulseWidth: Pulse width, units is second(s)
    :type PulseWidth: integer
    :param CanRetrig: Enable the retrigger function
    :type CanRetrig: boolean

.. py:attribute:: Override

    .. image:: _static/img/timing/override.png
        :width: 250
        :alt: Override component

    **Override** provide output of true for **OverrideTime** during **Trigger** is triggered from *false* to *true*. The remaining override time is counted in **RemainTime**. 

    :param Out: Output value
    :type Out: boolean
    :param RemainTime: Remaining override time, in min
    :type RemainTime: integer
    :param OverrideTime: Override time, in min
    :type OverrideTime: integer
    :param Trigger: Triggers the component start
    :type Trigger: boolean

.. py:attribute:: Timer

    .. image:: _static/img/timing/timer.png
        :width: 250
        :alt: Timer component

    **Timer** outputs a pulse for the configured amount of **Time**, **Run** is used to trigger the timer:
            
        - If *low*, **Out** is forced to be *false*
        - If *high*, **Out** = 1 until timer reaches *time* seconds
    Alternatively, the pulse can be fired from the “start Timer” action if in is not linked. 

    :param Out: Output value
    :type Out: boolean
    :param Run: fire the timer on transition from false to true
    :type Run: option
    :param Time: Duration of output pulse
    :type Time: integer
    :param Left: Remaining time before output transition from true to false
    :type Left: integer