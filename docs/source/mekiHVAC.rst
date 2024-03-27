mekiHVAC
========

.. py:attribute:: Drive
    
    .. image:: _static/img/hvac/drive.png
        :width: 250
        :alt: Drive component

    **Drive** component provides the mechanism to drive a floating type actuator with two outputs (open and close control). A single input with scale factor determines the desired position which controls the hardware output.
    
    The open and close operation time is based on the full stroke travel time, travel time. When the calculated position hits the minimum (0%) or maximum (100%), the open or close output will continue running for the drive travel time to make sure the actuator position is in place.
    
    :param Open: Drive current open state (read only), equal to *true* when drive is run while *false* is stop
    :type Open: boolean
    :param Close: Drive current close state (read only), equal to *true* when drive is run while *false* is stop
    :type Close: boolean
    :param Pos: Current calculated position based on drive time
    :type Pos: integer
    :param In: Drive position, scale from 0% to 100% using the *highscale* and *lowscale* parameters
    :type In: real
    :param Feedback: Actual schedule feedback signal, not calculated value
    :type Feedback: real
    :param Fb: Whether or not to use the *Fb* signal
    :type Fb: boolean
    :param Highscale: highest value of input value and equals to 100%, `default=100.00`
    :type Highscale: real
    :param Lowscale: lowest value of input value and equals to 0%, `default=0.00`
    :type Lowscale: real
    :param Hystr: minimum changes of the input value to activate the open and close operation
    :type Hystr: real
    :param TravelTime: Drives full stroke travel time in seconds(s), `default = 30s`
    :type TravelTime: integer

.. py:attribute:: Loop

    .. image:: _static/img/hvac/loop.png
        :width: 250
        :alt: Loop component

    **Loop** component provides proportional, integral and derivative (PID) control action to the output based on the process value (input) and set point value. It monitors the process value, compares the process value to the set point, and generates the output value.
    
    PID loop control can be difficult to tune and (often for this reason) is seldom used. However, in certain cases, PID control may be needed. An example is the control of a process with a “long reaction time”, such as temperature control of a large mass. For such a lag-oriented system, the derivative component of the PID loop output can help preventing “overshoot” that might otherwise result from PID control.
    
    :param Out: Result of PID loop
    :type Out: real
    :param Enable: Equal to *True* to enable the PID loop algorithm to execute at the rate selected by the execute time property,
                   equal to *False* to force the PID loop output to a value dependent on the selection in the disable action property
    :type Enable: boolean
    :param ControlledVariable: Input for the controlled parameter, input must be valid for object to function
    :type ControlledVariable: real
    :param SetPoint: Input for the set point value, input must be valid for object to function
    :type SetPoint: real
    :param LoopAction: Determines whether the control algorithm is direct or reverse acting

                        Direct acting mode
                            - increase loop output as **ControlledVariable** *greater* than **SetPoint**, consided as *cooling* application
                        Reverse acting mode
                            - increase loop output as **ControlledVariable** *less* than **SetPoint**, consided as *heating* application
    :type LoopAction: option
    :param DisableAction: Value of loop output set to when loop is disabled by setting the loop enable property to false.
                            
                            - *Max value* - max output property value
                            - *Min value* - min output property value
                            - *Hold* - maintains the output at the last calculated value
                            - *Zero* - zero (0.0) value
    :type DisableAction: option
    :param ProportionalConstant: proportional gain parameter value used by loop algorithm, to set overall gain for loop, starting point for this value is found by output range/throttling range
    :type ProportionalConstant: real
    :param IntegralConstant: integral gain parameter used repeatedly per minute by loop algorithm, reset rate act on magnitude of set point error, typical starting point is *0.5*
    :type IntegralConstant: real
    :param DerivativeConstant: derivative gain parameter used by loop algorithm, acts on rate of change of set point error
    :type DerivativeConstant: real
    :param Bias: Output bias value added to output to correct offset error, used with proportional control
    :type Bias: real
    :param MaxOutput: Maximum output value
    :type MaxOutput: real
    :param MinOutput: Minimum output value
    :type MinOutput: real
    :param CycleTime: Loop travel time in milliseconds(ms), `default value = 500ms`
    :type CycleTime: integer
    :param RampTime: Minimum time that output can ramp completely from *MinOutput* to *MaxOutput* 
                        
                        - Rate of change is enforced upon startup, or whenever the loop point transitions from disabled to enabled
                        - Once ramp time expired, it has no effect on the output, intended use is to prevent the loop from “slamming” a valve or other controlled device to a limit during startup
                        - Default ramp time is *0:00:00*, or *disabled*, ramp time enter a reasonable value when the loop starts or is enabled
    :type RampTime: integer
    :param ResetIntegral: Available action on a loop point

                        - Clears the current integral component of the output calculation if *invoked*
                        - Linked to another object to provide a quick purge of the integral effect if *needed*
                        - Provide a “debug” utility, and should not be necessary if the loop point configuration properties are correctly defined.
    :type ResetIntegral: boolean

.. py:attribute:: LSeq

    .. image:: _static/img/hvac/lseq.png
        :width: 250
        :alt: LSeq component

    **LSeq** provide a linear sequence of 2 to 16 loads based on an input 0-100 value.
    
    Analogous to a bar graph of the input value, where the delta represented by each output is (in max - in min) / num outs. So given an input value V, outputs 1 through (V - in min) / delta will be set true, and any remaining outputs will be false.
    
    :param In: Input value
    :type In: real
    :param InMin: Min scale input value
    :type InMin: real
    :param InMax: Max scale input value
    :type InMax: real
    :param NumberOutputs: Total of effective number output
    :type NumberOutputs: integer
    :param Delta: Delta calculation
    :type Delta: real
    :param DOn: Byte of d On
    :type DOn: integer
    :param Out1-Out16: Number of output (1 - 16)
    :type Out1-Out16: boolean
    :param Ovfl: Overflow state when **In** > **In Max**
    :type Lowscale: boolean

.. py:attribute:: Psychrometric

    .. image:: _static/img/hvac/psychrometric.png
        :width: 250
        :alt: Psychrometric component

    **Psychrometric** is used to support applications that need to calculate the properties of moist air using given temperature and humidity inputs.
    
    :param AmbientTemp: Input temperature value
    :type AmbientTemp: real
    :param RelHumidity: Input humidity value
    :type RelHumidity: real
    :param TempScale: Celsius or Fahrenheit
    :type TempScale: unit
    :param DewPoint: Dew point temperature value, requies valid in *temp* and in *humidity* to calculate
    :type DewPoint: real
    :param VaporPressure: Vapor pressure value, requies valid in *temp* and in *humidity* to calculate
    :type VaporPressure: real
    :param SatPressure: Satureated pressure value ,  requies valid in *temp* to calculate
    :type SatPressure: real
    :param Enthalpy: Enthalpy value, requies valid in *temp* and in *humidity* to calculate
    :type Enthalpy: real
    :param WetBulb: Wet bulb temperature value, requies valid in *temp* and in *humidity* to calculate
    :type WetBulb: boolean 

.. py:attribute:: ReheatSeq

    .. image:: _static/img/hvac/reheatseq.png
        :width: 250
        :alt: ReheatSeq component

    **ReheatSeq** will provide a linear sequence up to 4 loads based on configurable thresholds.
    
    Sets an output true if the input value is greater than corresponding threshold, and returns the output to false if the input value is less than threshold minus the hysteresis value. 
    D On is the count of outputs that are true (0 to 4). If enable is false, all outputs are set to false regardless the value.
    
    :param Out1-Out4: Output value (1 - 4)
    :type Out1-Out4: boolean
    :param In: Input value
    :type In: real
    :param Enable: Enables this object in effect
    :type Enable: boolean
    :param DOn: Byte of d On
    :type DOn: integer
    :param Hysteresis: hysteresis configuration
    :type Hysteresis: real
    :param Threshold1-Threshold4: threshold configuration (1 – 4)
    :type Threshold1-Threshold4: real
      
.. py:attribute:: ReSet

    .. image:: _static/img/hvac/reset.png
        :width: 250
        :alt: ReSet component

    **ReSet** rescales input value to output value.

    This function performs a "reset" on the input value.
    "Reset" is a HVAC term for scaling a number between two limits.\
    
    - When **In Min** < **In** < **In Max**, the output value scales linearly between Out Min and Out Max.
    - If **In** < **In Min**, the value is capped at **OutMin**.
    - If **In** > **In Max**, the value is capped at **OutMax**.
    - **Out** is calulated by equation below:

    .. math:: 
        Out= (\frac{OutMax-OutMin}{InMax-InMin}) * (In - InMin) + OutMin

    :param Out: Output value
    :type Out: real
    :param In: Input value
    :type In: real
    :param InMin: Min input value configuration
    :type InMin: real
    :param InMax: Max input value configuration
    :type InMax: real
    :param OutMin: Min output scale, `default is 0`
    :type OutMin: real
    :param OutMax: Max output scale, `default is 100`
    :type OutMax: real

.. py:attribute:: RunTime

    .. image:: _static/img/hvac/runtime.png
        :width: 250
        :alt: RunTime component

    **RunTime** record the true running time, until the state turns into false.

    :param Time: Running state time in second
    :type Time: integer
    :param State: Input value state
    :type State: boolean

.. py:attribute:: Thermostat

    .. image:: _static/img/hvac/thermostat.png
        :width: 250
        :alt: Thermostat component

    **Thermostat** provides basic thermostatic (on/off) control with a statusBoolean out property and statusNumeric inputs for controlled variable (Cv), set point (Sp), and differential (Diff). Default action is cool. 
    
    :param Out: Output value 
    :type Out: boolean
    :param Enable: Enables this object in effect
    :type Enable: boolean
    :param Mode: Cool or heat mode
    :type Mode: option
    :param Cv: Input temperature goal
    :type Cv: real
    :param Sp: Input temperature set point
    :type Sp: real
    :param CutIn: Thermostat cut in value
    :type CutIn: real   
    :param CutOut: Thermostat cut out value
    :type CutOut: real  





 