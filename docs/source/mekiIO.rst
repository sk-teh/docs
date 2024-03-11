mekiIO
======

.. py:data:: AO

    .. image:: _static/img/IO/ao.png
        :width: 300
        :alt: AO component

    **AO** is the component provides an interface for the physical analogue output point that is able to source/drive a 0 to 20mA current or 0 to 10V voltage signal. 
    The output type is selected via AO configuration and hardware jumper setting.
    
    The analogue output provides 16 levels of prioritized command to control to the physical point. 
    **In1** has the highest priority whereas **In16** has the lowest. 
    The input may have a commanded value (valid floating value) or a null value (usually NaN in floating point). 
    A *null* value indicates that there is no value (or not active) in that priority. 
    The analogue output continuously monitors all prioritized inputs (**In1** to **In16**) to locate the entry with the highest priority non-NULL value and outputs it.

    :param Out: Output value
    :type Out: real, percentage
    :param Rawvalue: Raw output value depending on the **AOType**, equal to 0-10 when **AOType** is set to 0V-10V
    :type Rawvalue: real
    :param Minvalue: Min output value
    :type Minvalue: real, percentage
    :param Maxvalue: Max output value
    :type Maxvalue: real, percentage
    :param In1-In16: 16-level priority input, higher level input have higher priority to control **Out** value
    :type In1-In16: real
    :param Fallback: Default **Out** value when all **In1-In16** are *Null*
    :type Fallback: real
    :param ReverseOutput: Enables to reverse the output.
                        
                        - *False* = normal output, *True* = reverse output
                        - **ReverseOutput** (%) = 100 - **Out** (%)
    :type ReverseOutput: boolean
    :param OutofServices: Enables the output to make loss of every function.

                        - *False* = normal output, *True* = out of service.
                        - When **OutofService** is *true*, the **Out** is always *0*
    :type OutofServices: boolean

    :param SquarerootOutput: Enables the output to take the square root operation.

                        - Relationship between output value and physical value: 
                            - *Physical Calculated Value* (%) = *Out* (%) * *Out* (%)
                            - *Physical Value* = *Physical Calculated Value* (%) * (*Out High* - *Out Low*) + *Out Low*
                            - **Out** (%) = 100 * **Out**/ (**ScaleHigh** - **ScaleLow**)
                            - *Out*(High) = 10V (voltage type), 20mA (current type)
                            - *Out*(Low) = 0V (voltage type), 0mA (current type 0 - 20mA), 4mA (current type 4 - 20mA)
    :type SquarerootOutput: boolean
    :param ClampingHighEnable: Enables the clamping *high* limit control for the output value.
    :type ClampingHighEnable: boolean
    :param ClampingLowEnable: Enables the clamping *low* limit control for the output value.
    :type ClampingLowEnable: boolean
    :param ResetMinvalue: Enables to reset the **MinValue** back to 0.
    :type ResetMinvalue: boolean
    :param ResetMaxvalue: Enables to reset the **MaxValue** back to 0.
    :type ResetMaxvalue: boolean
    :param ClampingHigh: Output *high* limit, set the **Maxvalue** value even if it *exceeds* the processed value
    :type ClampingHigh: real
    :param ClampingLow: Output *low* limit, set the **Minvalue** value even if it *falls* the processed value
    :type ClampingLow: real
    :param ScaleHigh: Output scale *high* value
    :type ScaleHigh: real
    :param ScaleLow: Output value when physical output value equals to lowest value
                
                    - Voltage (0 - 10V): 0V
                    - Current (0 - 20mA): 0mA
                    - Current (4 - 20mA): 4mA
                
                    AO uses the **scalelow** and **scalehigh** to convert the output value to physical value. Raw value register shows the physical output.
                        - Physical Value = (**Out** (%)) * (**ScaleHigh** - **ScaleLow**)
                    
                    For instance:
                        - **AOType** = Current 4 - 20mA
                        - **ScaleLow** Value = 0%
                        - **ScaleHigh** Value = 100%
                        - **Out** Value = 50%
    :type ScaleLow: real 
    :param AOType:                     
                    - Voltage, 0-10V
                    - Current, 4mA-20mA
                    - Current, 0mA-20mA
    :type AOType: option           

.. py:data:: DI

    .. image:: _static/img/IO/di.png
        :width: 300
        :alt: DI component

    **DI** component is used for reading the digital value connected to one of the physical digital input points on the controller.
    It is typically used to monitor the status of contact closures from various field devices such as switches, open/close sensors or any other dry contact devices. 
    
    There are 16 digital input points on *IO28U/DDC28P* controller. Eight of them are derived directly from digital input detection circuitry (+5Vdc pulled up), named as *DI1* to *DI8*. 
    Whereby the other eights are derived from universal input (*UI* or *AI*) using value conversion (DI9 to D16). *DI1* to *DI8* might have different characteristics comparing to *DI9* to *DI16* depend on the AI settings. 
    Please refer to AI component section regarding the conversion.

    :param Out: Output state
    :type Out: boolean
    :param Alarm: Digital alarm state
    :type Alarm: boolean
    :param OffLatch: Off lock status
    :type OffLatch: boolean
    :param OnLatch: On lock status
    :type OnLatch: boolean
    :param OffCounter: Accumulate number when *off* counter, from ranges of 0 - 65535 
    :type OffCounter: integer
    :param OnCounter: Accumulate number when *on* counter, from ranges of 0 - 65535 
    :type OnCounter: integer
    :param OnTimer: Accumulate counting value when *on* timer, from ranges of 0 - 65535 
    :type OnTimer: integer
    :param OffTimer:  Accumulate counting value when *off* timer, from ranges of 0 - 65535 
    :type OffTimer: integer
    :param OutofServices: Enables the output to make loss of every function.

                        - *False* = normal output, *True* = out of service.
                        - When **OutofService** is *true*, the **Out** is always *0*
    :type OutofServices: boolean
    :param Polarity: Inverts the output polarity
                        
                        - *Direct* = normal output
                        - *Reverse* = negation
    :type Polarity: option
    :param UserSetState: Does not work until **OutofService** is *true*, **Out** equal to *User Set State* when **OutofService** is *true*
    :type UserSetState: boolean
    :param AlarmEnable: Digital input set to alarm state, based of alarm type
    
                        - *Enable* when alarm is triggered
                        - *Disable* when alarm failure
    :type AlarmEnable: boolean
    :param AlarmMonitorState: DI alarm state 
    
                        - *off* = Alarm is triggered when DI is off
                        - *on* = Alarm is triggered when DI is on
    :type AlarmMonitorState: boolean
    :param AlarmResetType: Mode of alarm recovery
    
                        - *Auto* = When DI is not in the alarm monitor state, alarm will be restored back to normal
                        - *Manual* = When DI produces alarm, it only can be manually recovered
    :type AlarmResetType: option
    :param ResetAlarm:  Alarm recovered manually when **AlarmResetType** is set to Manual
    :type ResetAlarm: option
    :param ResetOffCounter: Enables to reset the **OffCounter** to 0 
    :type ResetOffCounter: boolean
    :param ResetOnCounter: Enables to reset the **OnCounter** to 0  
    :type ResetOnCounter: boolean
    :param ResetOffTimer: Enables to reset the **OffTimer** to 0 
    :type ResetOffTimer: boolean
    :param ResetOnTimer: Enables to reset the **OnTimer** to 0  
    :type ResetOnTimer: boolean
    :param ClearOffLatch: Clear **OffLatch**  
    :type ClearOffLatch: boolean
    :param ClearOnLatch:  Clear **OnLatch**
    :type ClearOnLatch: boolean
    :param AlarmDelayTime: Alarm delay time when alarm triggered
    :type AlarmDelayTime: integer, millisecond

.. py:data:: DO

    .. image:: _static/img/IO/do.png
        :width: 300
        :alt: DO component

    **DO** is used for switching a physical digital output point *OFF* or *ON*. 
    The typical usage is starting/stopping the external equipment such as light, valve, fan or any other digital control equipment. 
    The DO component monitors the required set state and determines the proper hardware output action based on its settings. 
    There are eight digital output points on *IO28U/IO22U/DDC28P* controller. 
    Each of them is driven by a dry contact relay (SPST Relay) which is able to drive the external devices up to 1 Ampere (AC/DC).
    
    Digital output is a prioritized command with 16 priorities control plus a default value (relinquish default). 
    *In1* has the highest priority while in16 has the lowest. In6 is reserved for minimum/maximum time controlling. 
    The value can be commanded value (false = 0, true = 1) or a *null* value (= 2). 
    A *null* value indicates that there is no value (or not active) in that priority.

    :param Out: Output state
    :type Out: boolean
    :param In1-In16: 16-level priority input, higher level input have higher priority to control **Out** value
    :type In1-In16: real
    :param Fallback: Default **Out** value when all **In1-In16** are *Null*
    :type Fallback: boolean
    :param OffCounter: Accumulate number when *off* counter, from ranges of 0 - 65535 
    :type OffCounter: integer
    :param OnCounter: Accumulate number when *on* counter, from ranges of 0 - 65535 
    :type OnCounter: integer
    :param OnTimer: Accumulate counting value when *on* timer, from ranges of 0 - 65535 
    :type OnTimer: integer
    :param OffTimer:  Accumulate counting value when *off* timer, from ranges of 0 - 65535 
    :type OffTimer: integer
    :param OutofServices: Enables the output to make loss of every function.

                        - *False* = normal output, *True* = out of service.
                        - When **OutofService** is *true*, **Out** is always *0*
    :type OutofServices: boolean
    :param Polarity: Inverts the output polarity,
                        
                        - *Direct* = normal output
                        - *Reverse* = negation
    :type Polarity: option
    :param MinOffOnStart: Time delay of output conversion, based on **MinOffTime** and **MinOnTime**
    :type MinOffOnStart: boolean
    :param ResetOnCounter: Enables to reset the **OnCounter** to 0  
    :type ResetOnCounter: boolean 
    :param ResetOffCounter: Enables to reset the **OffCounter** to 0 
    :type ResetOffCounter: boolean
    :param ResetOffTimer: Enables to reset the **OffTimer** to 0 
    :type ResetOffTimer: boolean
    :param ResetOnTimer: Enables to reset the **OnTimer** to 0  
    :type ResetOnTimer: boolean
    :param ResetOffTimer: Enables to reset the **OffTimer** to 0 
    :type ResetOffTimer: boolean
    :param InterOutputDelay: Output delay time
    :type InterOutputDelay: integer, second
    :param MinOffTime: Minimum time delay when output transitioned from on to off
    :type MinOffTime: integer, second
    :param MinOnTime: Minimum time delay when output transitioned from off to on
    :type MinOnTime: integer, second

.. py:data:: UI

    .. image:: _static/img/IO/ui.png
        :width: 300
        :alt: UI component

    **UI** is used for reading the analogue value connected to one of the physical universal input points on a controller. 
    There are eight universal input points on *IO22U/IO28U/DDC28P* controller that support voltage, current, resistance and temperature sensors. 
    The input type is selected via AI configuration and hardware jumper setting. 
    For temperature sensors, the standard curves for 10K Thermistor (with or without 11K shunt), 1K Balco and 1K Platinum (in degree C and Fahrenheit F) are provided within the internal tables. 
    Additional tables are also available as user defined curves.

    :param Out: UI Output physical value
    :type Out: real
    :param MaxValue: Maximum record UI received
    :type MaxValue: real
    :param MinValue: Minimum record UI received
    :type MinValue: real
    :param Rawvalue: Raw output value depending on the **UIType**, equal to 0-10 when **UIType** is set to 0V-10V
    :type Rawvalue: real
    :param Reliability: Display object state
    :type Reliability: boolean
    :param Alarm: Alarm state of selected channel based on limit of configurations
    :type Alarm: boolean
    :param AlarmType: Alarm type
    :type AlarmType: state
    :param AlarmResetType: Auto or manually recovery alarm
    :type AlarmResetType: option
    :param HighAlarmEnable: Enable **AlarmHighLimit**
    :type HighAlarmEnable: boolean
    :param LowAlarmEnable: Enable **AlarmLowLimit**
    :type LowAlarmEnable: boolean
    :param LowCutOffEnable: Enable low level cuttoff

                            - Low cutoff function helps to filter unstable value by forcing the output value to scale low value when iput valvue is lower than low cutoff value.
                            - The cutoff enable can only be applied to current and voltage input type selection
    :type LowCutOffEnable: boolean
    :param OutofServices: Enables the output to make loss of every function.

                        - *False* = normal output, *True* = out of service.
    :type OutofServices: boolean
    :param Linearization: Squareroot operation on input value, only applicable for input type voltage and current
                        
                        - *Direct* = linearization
    :type Linearization: option
    :param AlarmReset: Reset alarm state, only applies to manual alarm reset
    :type AlarmReset: boolean
    :param ResetMinvalue: Enables to reset the **MinValue** back to 0
    :type ResetMinvalue: boolean
    :param ResetMaxvalue: Enables to reset the **MaxValue** back to 0
    :type ResetMaxvalue: boolean
    :param AlarmDeadband: Output alarm deadband value, deadband applied to AlarmLowLimit and AlarmHighLimit value to determine the return from alarm trip points.

                        - **Out** must lower than the **AlarmHighLimit** by alarm deadband limit to return from high alarm trip point
                        - **Out** must greater than the **AlarmLowLimit** by alarm deadband limit to return from low alarm trip point
    :type AlarmDeadband: boolean
    :param AlarmDelay: UI alarm delay time, maximum 65535 seconds
    
                        The delay duration that **Out** must be:
                            - in the alarm condition before alarm state is generated
                            - in the non-alarm condition before returning from alarm state
    :type AlarmDelay: integer, second
    :param AlarmHighLimit: High limit value
    :type AlarmHighLimit: real
    :param AlarmLowLimit: Low limit value
    :type AlarmLowLimit: real
    :param DecimalPoint: decimal point precision of **Out** for roundup during conversion
    :type DecimalPoint: integer
    :param DigitalOffLevel: Off state level of *Out* value for digital transformation, *positive* level value means greater than, and a *negative* levle means lower than comparison
    :type DigitalOffLevel: real
    :param DigitalOnLevel: On state level of *Out* value for digital transformation, *positive* level value means greater than, and a *negative* levle means lower than comparison
    :type DigitalOnLevel: real
    :param LowCutOffValue: **Out** value be set to *ScaleLowValue* whenever the input value is lower than the *LowCutOffValue* if **LowCutOffEnable** is enabled, only applicable to current and voltage input type
    :type LowCutOffValue: real
    :param Offset: Offset adjustment for input
    :type Offset: real
    :param ScaleHighValue: Applicable for volatge and current input only
    :type ScaleHighValue: real
    :param ScaleLowValue: Applicable for volatge and current input only
    :type ScaleLowValue: real
    :param TemperatureTable: UI temperature selection from table 1 to 16

                            - This temperature table defines the temperature curve table index used for looking up conversion for temperature sensor Input type
                            - The controller has built-in 8 default temperature tables (9 to 16) and 8 user defined temperature tables (1 to 8) which are customizable in Virtual Device software (Setting->Temperature Table)     
    :type TemperatureTable: option
    :param UIType: Sensor type connected to physical point and determines conversion algorithm                  
                   
                    - Voltage, 0-10V
                    - Voltage, 0-5V
                    - Current, 4mA-20mA
                    - Current, 0mA-20mA
                    - Resistance
                    - Sensor
    :type UIType: option  
    :param UserSetValue: **Out** equal to *UserSetValue* when **OutofService** is *true*
    :type UserSetValue: real

  


