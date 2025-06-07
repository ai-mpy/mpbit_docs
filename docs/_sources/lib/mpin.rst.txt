.. currentmodule:: mpbit
.. _mpbit.MPin:

class MPin -- 引脚扩展
=============================

读写数字模拟引脚值,电平变化事件,模拟值改变事件

构造函数
-------------------------------

.. class:: MPin(pin, mode=PinMode.IN, pull=None)

   创建一个引脚对象。

   :param int pin: 引脚编号
   :param PinMode mode: 引脚模式, 可选值: ``PinMode.IN``, ``PinMode.OUT``, ``PinMode.ANALOG``
   :param pull: 引脚上拉模式, 可选值: ``Pin.PULL_UP``, ``Pin.PULL_DOWN``, ``Pin.PULL_NONE``

   .. method:: read_digital()

      读取引脚的数字电平值。(必须是 ``PinMode.IN`` 模式)

      :return: 引脚的数字电平值, 0 或 1

   .. method:: write_digital(value)

      设置引脚的数字电平值。(必须是 ``PinMode.OUT`` 模式)

      :param int value: 要设置的数字电平值, 0 或 1

   .. method:: read_analog()
      读取引脚的模拟值。(必须是 ``PinMode.ANALOG`` 模式)

      :return: 引脚的模拟值, 范围在 0 到 4095 之间

   .. method:: write_analog(value)
      设置引脚的模拟值。(必须是 ``PinMode.ANALOG`` 模式)

      :param int value: 要设置的模拟值, 范围在 0 到 1023 之间

      用例:

      .. code-block:: python

         from mpbit import MPin,PinMode
         # 初始化数字输出引脚
         p0 = MPin(0, PinMode.PWM)
         # 设置模拟值
         p0.write_analog(1023)

   .. method:: irq(trigger=0, handler=None)
      设置引脚的中断触发条件和中断处理函数。

      :param int trigger: 中断触发条件, 可选值: ``Pin.IRQ_FALLING``, ``Pin.IRQ_RISING``, ``Pin.IRQ_RISING | Pin.IRQ_FALLING``
      :param function handler: 中断处理函数, 接收一个参数, 为触发中断的引脚对象

      用例:

      .. code-block:: python

         from mpbit import MPin
         # 定义中断处理函数
         def on_p0_rising(_):
            pass
         # 创建一个引脚对象
         p0 = MPin(0, PinMode.IN)
         # 设置中断触发条件和中断处理函数
         p0.irq(Pin.IRQ_RISING,on_p0_rising)

示例:

.. code-block:: python

    from mpbit import MPin
    # 创建一个引脚对象
    p0 = MPin(0, MPin.IN)
    # 读取引脚的数字电平值
    value = p0.read_digital()
    print("引脚电平值:", value)


