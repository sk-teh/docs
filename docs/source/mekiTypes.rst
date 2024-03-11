mekiTypes
=========

.. py:attribute:: B2F

    .. image:: _static/img/types/b2f.png
        :width: 250
        :alt: B2F component
    
    **B2F** is a 16-bits binary to float encoder object.
    
    **Out** = Encoded input values, as **In16** is the MSB and **In1** is the LSB
    
    **Count** = Sum of the inputs that are active

    :param Out: Encoded output value
    :type Out: real
    :param Count: Sum of the (read only)input that are active
    :type Count: real
    :param In1-In16: Input value
    :type In1-In16: boolean

.. py:attribute:: ConstBool

    .. image:: _static/img/types/ConstBool.png
        :width: 250
        :alt: ConstBool component
    
    **ConstBool** is a Boolean object.
    
    **Out** should never be a link destination
    
    :param Out: Output value
    :type Out: real

.. py:attribute:: ConstFloat

    .. image:: _static/img/types/constfloat.png
        :width: 250
        :alt: ConstFloat component
    
    **ConstFloat** is a real object.
    
    **Out** should never be a link destination
    
    :param Out: Output value
    :type Out: real

.. py:attribute:: ConstInt

    .. image:: _static/img/types/constint.png
        :width: 250
        :alt: ConstInt component
    
    **ConstInt** is an integer object.
    
    **Out** should never be a link destination
    
    :param Out: Output value
    :type Out: integer

.. py:attribute:: F2B

    .. image:: _static/img/types/f2b.png
        :width: 250
        :alt: F2B component
    
    **F2B** is a float to 16-bits decoder object.
    
    **Out1** to **Out16** are decoded as **Out1** is *LSB* while **Out16** is *MSB*

    :param In: Input value
    :type In: real
    :param Out1-Out16: Output value
    :type Out1-Out16: boolean
    :param Ovrf: Overflow flag when **In** is exceed the decoder range (0 – 65535)
    :type Ovrf: boolean

.. py:attribute:: F2I

    .. image:: _static/img/types/f2i.png
        :width: 250
        :alt: F2I component
    
    **F2I**  is a float-to-integer converter object.
    
    :param In: Input value
    :type In: real
    :param Out: Output value
    :type Out: integer

.. py:attribute:: I2F

    .. image:: _static/img/types/i2f.png
        :width: 250
        :alt: I2F component
    
    **I2F**  is an integer-to-float converter object.
    
    :param In: Input value
    :type In: integer
    :param Out: Output value
    :type Out: real