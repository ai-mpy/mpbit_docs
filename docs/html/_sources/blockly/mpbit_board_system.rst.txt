板载输入
=============


读取触摸按鍵的值
--------------------

.. figure:: img/mpbit_touchpad_read.png
    :height: 40px
    :class: block-figure

**功能**:

- 读取指定触摸按键的值,1为按下,0为松开
- 触摸键 P,Y,T,H,O,N

生成代码示例:

.. code-block:: python

    from mpbit import touchpad_p

    touchpad_p.read()

