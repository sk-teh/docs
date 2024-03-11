mekiRegs
========
DDC28P/IO22U/28U/28P/KXM16P/22P/IP0080
--------------------------------------

.. py:data:: BooleanPoint

    .. image:: _static/img/reg/bool.png
        :width: 300
        :alt: BooleanPoint component

    **Boolean Point** is used to access to controller Boolean point type (read only) register = Modbus discrete input. The register address is 0-based whereby controller documented address is 1-based.
    
    :param Addr: Boolean point register address, a total of 16 non-repeating address (from 2000 to 2015)
    :type Addr: address
    :param In: Boolean point register (read only) input value
    :type In: boolean

.. py:data:: BooleanWritable

    .. image:: _static/img/reg/boolwr.png
        :width: 300
        :alt: BooleanWritable component

    **Boolean Writable** is used to access to controller Boolean writable type register = Modbus coil output. The register address is 0-based whereby controller documented address is 1-based.
    
    :param Addr: Boolean writable register address, a total of 16 non-repeating address (from 2000 to 2015)
    :type Addr: address
    :param Out: Boolean writable register output value
    :type Out: boolean
    :param In: Input value
    :type In: boolean

.. py:data:: ShortPoint

    .. image:: _static/img/reg/short.png
        :width: 300
        :alt: ShortPoint component

    **Short Point** is used to access to controller short point type (read only) register = Modbus input register (16-bits integer). The register address is 0-based whereby controller documented address is 1-based.
    
    :param Addr: Short point register address, a total of 16 non-repeating address (from 2000 to 2015)
    :type Addr: address
    :param In: Short point register (read only) input value
    :type In: integer

.. py:data:: ShortWritable

    .. image:: _static/img/reg/shortwr.png
        :width: 300
        :alt: ShortWritable component

    **Short Writable** is used to access to controller short writable type register = Modbus holding register (16-bits integer). The register address is 0-based whereby controller documented address is 1-based.
    
    :param Addr: Short writable address, a total of 16 non-repeating address (from 2000 to 2015)
    :type Addr: address
    :param Out: Writable register output value
    :type Out: integer
    :param In: Input value
    :type In: integer

.. py:data:: FloatPoint
    
    .. image:: _static/img/reg/float.png
        :width: 300
        :alt: FloatPoint component

    **Float Point** is used to access to controller float point type (read only) register = Modbus input register (floating point). The register address is 0-based whereby controller documented address is 1-based.
    
    :param Addr: Float point address, a total of 16 non-repeating address (from 2016 to 2046)
    :type Addr: address
    :param In: Float point register (read only) input value
    :type In: real

.. py:data:: FloatWritable
    
    .. image:: _static/img/reg/floatwr.png
        :width: 300
        :alt: FloatWritable component

    **Float Writable** is used to access to controller float writable type register = Modbus holding register (floating point). The register address is 0-based whereby controller documented address is 1-based.
    
    :param Addr: Float writable address, a total of 16 non-repeating address (from 2016 to 2046)
    :type Addr: address
    :param Out: Float Writable register output value
    :type Out: real
    :param In: Input value
    :type In: real

.. py:data:: LongPoint
    
    .. image:: _static/img/reg/long.png
        :width: 300
        :alt: LongPoint component

    **Long Point** is used to access to controller long point type (readonly) register = Modbus input register (32-bits integer). The register address is 0-based whereby controller documented address is 1-based.
    
    :param Addr: Long point address, a total of 16 non-repeating address (from 2016 to 2046)
    :type Addr: address
    :param In: Long point register (read only) input value
    :type In: integer

.. py:data:: LongWritable
    
    .. image:: _static/img/reg/longwr.png
        :width: 300
        :alt: LongWritable component

    **Long Writable** is used to access to controller float writable type register = Modbus holding register (floating point). The register address is 0-based whereby controller documented address is 1-based.
    
    :param Addr: Long writable address, a total of 16 non-repeating address (from 2016 to 2046)
    :type Addr: address
    :param Out: Long Writable register output value
    :type Out: integer
    :param In: Input value
    :type In: integer

