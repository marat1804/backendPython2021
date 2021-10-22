## 2. Написать метакласс, который в начале названий всех атрибутов и методов (кроме магических) добавляет префикс "custom_" (+тесты).
    class CustomMeta():
        pass

    class CustomClass(metaclass=CustomMeta):
        x = 50

        def __init__(self, val=99):
            self.val = val

        def line(self):
            return 100

    inst = CustomClass()
    inst.custom_x
    inst.custom_val
    inst.custom_line()

    inst.x  # ошибка
    inst.val  # ошибка
    inst.line() # ошибка
