mekiLogic
=========

.. py:attribute:: ADemux2

    .. image:: _static/img/logic/ademux2.png
        :width: 250
        :alt: ADemux2 component

    **ADemux2** outputs the input value according to selected the output channel.

    :param Out1: Equal to **In** when **Sel** is *Out1*, otherwise remains unchanged
    :type Out1: real
    :param Out2: Equal to **In** when **Sel** is *Out2*, otherwise remains unchanged
    :type Out2: real
    :param In: Input value
    :type In: real
    :param Sel: Select the output channel, *Out1* or *Out2*
    :type Sel: option

.. py:attribute:: And4

    .. image:: _static/img/logic/and4.png
        :width: 250
        :alt: And4 component

    **And4** performs a logical AND towards all inputs and writes the result to the out property. 
    
    +-------+-------+-------+-------+-------+
    |  In1  |  In2  |  In3  |  In4  |  Out  |
    +=======+=======+=======+=======+=======+
    | false | false | false | false | false |
    +-------+-------+-------+-------+-------+
    | true  | false | false | false | false |
    +-------+-------+-------+-------+-------+
    | false | true  | false | false | false |
    +-------+-------+-------+-------+-------+
    | false | false | true  | false | false |
    +-------+-------+-------+-------+-------+
    | false | false | false | true  | false |
    +-------+-------+-------+-------+-------+
    | true  | true  | false | false | false |
    +-------+-------+-------+-------+-------+
    | true  | false | true  | false | false |
    +-------+-------+-------+-------+-------+
    | true  | false | false | true  | false |
    +-------+-------+-------+-------+-------+
    | false | true  | true  | false | false |
    +-------+-------+-------+-------+-------+
    | false | true  | false | true  | false |
    +-------+-------+-------+-------+-------+
    | false | false | true  | true  | false |
    +-------+-------+-------+-------+-------+
    | true  | true  | true  | false | false |
    +-------+-------+-------+-------+-------+
    | true  | true  | false | true  | false |
    +-------+-------+-------+-------+-------+
    | true  | false | true  | true  | false |
    +-------+-------+-------+-------+-------+
    | false | true  | true  | true  | false |
    +-------+-------+-------+-------+-------+
    | true  | true  | true  | true  | true  |
    +-------+-------+-------+-------+-------+
    
    truth table when using four inputs.

.. py:attribute:: ASW

    .. image:: _static/img/logic/asw.png
        :width: 250
        :alt: ASW component

    **ASW** outputs the input value according to selected the input channel.

    :param Out: Equal to **In1** when **S1** is *In1*, otherwise equal to **In2**  
    :type Out: real
    :param In1: Input value
    :type In1: real
    :param In2: Input value
    :type In2: real
    :param S1: Select the input channel, *In1* or *In2*
    :type S1: option

.. py:attribute:: B2P

    .. image:: _static/img/logic/b2p.png
        :width: 250
        :alt: B2P component

    **B2P** is short of “Boolean to pulse”. It outputs a pulse signal when input value is made to true.

    :param Out: Pulse signal output  
    :type Out: boolean
    :param In: Input value
    :type In: boolean

.. py:attribute:: BSW

    .. image:: _static/img/logic/bsw.png
        :width: 250
        :alt: BSW component

    **BSW** outputs the input values according to selected the input channel.

    :param Out: Equal to **In1** when **S1** is *In1*, otherwise equal to **In2**  
    :type Out: boolean
    :param In1: Input value
    :type In1: boolean
    :param In2: Input value
    :type In2: boolean
    :param S1: Select the input channel, *In1* or *In2*
    :type S1: option

.. py:attribute:: Demuxl2B4

    .. image:: _static/img/logic/demux2b4.png
        :width: 250
        :alt: Demuxl2B4 component

    **Demuxl2B4** outputs the input values according to selected the input channel.

    :param In: Input value
    :type In: integer
    :param Out1-Out4: Only 1 *Out* equal to true each time base on logic:
                        Out(x) = true, while x = **In** – **StartsAt** + 1,
                        all *Out* equal to false if x > 4 and x < 1
    :type Out1-Out4: boolean
    :param StartsAt: Offset value for **In** selection
    :type StartsAt: integer

.. py:attribute:: ISW

    .. image:: _static/img/logic/isw.png
        :width: 250
        :alt: ISW component

    **ISW** outputs the input values according to selected the input channel.

    :param Out: Equal to **In1** when **S1** is *In1*, otherwise equal to **In2**  
    :type Out: integer
    :param In1: Input value
    :type In1: integer
    :param In2: Input value
    :type In2: integer
    :param S1: Select the input channel, *In1* or *In2*
    :type S1: option

.. py:attribute:: Not

    .. image:: _static/img/logic/not.png
        :width: 250
        :alt: Not component

    **Not** outputs a contrary of the input value.

    :param Out: Opposite value of **In** 
    :type Out: boolean
    :param In: Input value
    :type In: boolean

.. py:attribute:: Or4

    .. image:: _static/img/logic/or4.png
        :width: 250
        :alt: Or4 component

    **Or4** outputs the input values according to selected the input channel.

    :param Out: Equal to true if one of the *In1-In4* is true 
    :type Out: boolean
    :param In1-In4: Input value
    :type In1-In4: boolean

.. py:attribute:: Xor

    .. image:: _static/img/logic/xor.png
        :width: 250
        :alt: Xor component

    **Xor** outputs the input values according to selected the input channel.

    :param Out: Equal to true if both *In1* and *In2* are not identical
    :type Out: boolean
    :param In1: Input value
    :type In1: boolean
    :param In2: Input value
    :type In2: boolean


   


   




   