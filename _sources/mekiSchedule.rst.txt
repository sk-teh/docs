mekiSchedule
============

.. py:attribute:: DailyScheduleBool

    .. image:: _static/img/schedule/dailyschedulebool.png
        :width: 250
        :alt: DailyScheduleBool component

    **DailyScheduleBool** produce scheduler output, according to the scheduled time setting. The output value is Boolean.

    :param StartHour1: The first start session time of hour. Format is "0 - 23"
    :type StartHour1: integer
    :param StartMinute1: The first start session time of minute. Format is "0 - 59"
    :type StartMinute1: integer
    :param StopHour1: The first stop session time of hour. Format is "0 - 23"
    :type StopHour1: integer
    :param StopMinute1: The first stop session time of minute. Format is "0 - 59"
    :type StopMinute1: integer
    :param StartHour2: The second start session time of hour. Format is "0 - 23"
    :type StartHour2: integer
    :param StartMinute2: The second start session time of minute. Format is "0 - 59"
    :type StartMinute2: integer
    :param StopHour2: The second stop session time of hour. Format is "0 - 23"
    :type StopHour2: integer
    :param StopMinute2: The second stop session time of minute. Format is "0 - 59"
    :type StopMinute2: integer
    :param Out: Output value
    :type Out: boolean
    :param Val1: First session default output
    :type Val1: boolean
    :param Val2: Second session default output
    :type Val2: boolean
    :param Def: Default output
    :type Def: boolean

.. py:attribute:: DailyScheduleFloat

    .. image:: _static/img/schedule/dailyschedulefloat.png
        :width: 250
        :alt: DailyScheduleFloat component

    **DailyScheduleFloat** produce scheduler output, according to the scheduled time setting. The output value is floating value.

    :param StartHour1: The first start session time of hour. Format is "0 - 23"
    :type StartHour1: integer
    :param StartMinute1: The first start session time of minute. Format is "0 - 59"
    :type StartMinute1: integer
    :param StopHour1: The first stop session time of hour. Format is "0 - 23"
    :type StopHour1: integer
    :param StopMinute1: The first stop session time of minute. Format is "0 - 59"
    :type StopMinute1: integer
    :param StartHour2: The second start session time of hour. Format is "0 - 23"
    :type StartHour2: integer
    :param StartMinute2: The second start session time of minute. Format is "0 - 59"
    :type StartMinute2: integer
    :param StopHour2: The second stop session time of hour. Format is "0 - 23"
    :type StopHour2: integer
    :param StopMinute2: The second stop session time of minute. Format is "0 - 59"
    :type StopMinute2: integer
    :param Out: Output value
    :type Out: real
    :param Val1: First session default output
    :type Val1: real
    :param Val2: Second session default output
    :type Val2: real
    :param Def: Default output
    :type Def: real

.. py:attribute:: DateTime

    .. image:: _static/img/schedule/datetime.png
        :width: 250
        :alt: DateTime component

    **DateTime** provide the current RTC time for reference (read only).

    :param Year: RTC year
    :type Year: real
    :param Month: RTC month
    :type Month: real
    :param Day: RTC Day
    :type Day: real
    :param Weekday: RTC weekday
    :type Weekday: real
    :param Minute: RTC minute
    :type Minute: real
    :param Second: RTC second
    :type Second: real
   