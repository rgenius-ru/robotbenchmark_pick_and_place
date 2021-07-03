"""Пример программы для симулятора Webots в соревновании по перемещению кубика."""

from controller import Robot

# Создать экземпляр робота.
robot = Robot()

# Получить шаг (тик) времени текущего мира.
timestep = int(robot.getBasicTimeStep())

# Инициализировать основные двигатели.
wheels = []
wheels.append(robot.getMotor("wheel1"))  # Колесо 1
wheels.append(robot.getMotor("wheel2"))  # Колесо 2
wheels.append(robot.getMotor("wheel3"))  # Колесо 3
wheels.append(robot.getMotor("wheel4"))  # Колесо 4
for wheel in wheels:
    # Активируйте управление двигателями, задав скорость.
    # В противном случае по умолчанию двигатель ожидает управления силой или положением,
    # и setVelocity установит максимальную скорость двигателя вместо целевой скорости.
    wheel.setPosition(float('+inf'))  # Установить позицию колеса = Бесконечность

# Инициализировать двигатели манипулятора.
armMotors = []
armMotors.append(robot.getMotor("arm1"))  # Плечо 1
armMotors.append(robot.getMotor("arm2"))  # Плечо 2
armMotors.append(robot.getMotor("arm3"))  # Плечо 3
armMotors.append(robot.getMotor("arm4"))  # Плечо 4
armMotors.append(robot.getMotor("arm5"))  # Плечо 5
# Установить максимальную скорость двигателей.
armMotors[0].setVelocity(0.2)
armMotors[1].setVelocity(0.5)
armMotors[2].setVelocity(0.5)
armMotors[3].setVelocity(0.3)

# Инициализировать датчики позици плеч.
# Эти датчики можно использовать для получения текущей позиции суставов и для отслеживания их движения.
armPositionSensors = []
armPositionSensors.append(robot.getPositionSensor("arm1sensor"))
armPositionSensors.append(robot.getPositionSensor("arm2sensor"))
armPositionSensors.append(robot.getPositionSensor("arm3sensor"))
armPositionSensors.append(robot.getPositionSensor("arm4sensor"))
armPositionSensors.append(robot.getPositionSensor("arm5sensor"))
for sensor in armPositionSensors:
    sensor.enable(timestep)

# Инициализация двигателей захвата.
finger1 = robot.getMotor("finger1")  # Палец 1
finger2 = robot.getMotor("finger2")  # Палец 2
# Установить максимальную скорость двигателей.
finger1.setVelocity(0.03)
finger2.setVelocity(0.03)
# Получить мин и макс позиции двигателей захвата.
fingerMinPosition = finger1.getMinPosition()
fingerMaxPosition = finger1.getMaxPosition()

# Двигаться вперёд.
for wheel in wheels:  # Для каждого колеса ...
    wheel.setVelocity(7.0)  # Установить скорость 7.0
# Ждать пока робот подъедет к транспортной ленте.
robot.step(520 * timestep)  # 520 шагов времени (тиков)

# Остановить движение вперёд.
for wheel in wheels:  # Для каждого колеса ...
    wheel.setVelocity(0.0)  # Установить скорость 0.0

# Привести манипулятор в движение и открыть захват.
armMotors[1].setPosition(-0.55)  # Плечо 1 - Задать позицию ..
armMotors[2].setPosition(-0.9)  # Плечо 2 - Задать позицию ..
armMotors[3].setPosition(-1.5)  # Плечо 3 - Задать позицию ..
finger1.setPosition(fingerMaxPosition)  # Палец 1 - Задать макс позицию
finger2.setPosition(fingerMaxPosition)  # Палец 2 - Задать макс позицию

# Следить за положением сустава манипулятора, чтобы определить, когда движение завершено.
while robot.step(timestep) != -1:  # До тех пор пока запущена симуляция выполнять оператор ЕСЛИ
    if abs(armPositionSensors[3].getValue() - (-1.2)) < 0.01:  # ЕСЛИ позиция 3й оси равна -1.2 с точностью до 0.01, то выйти из цикла while
        # Движение завершено.
        break  # Выйти из цикла while

# Закрыть захват.
finger1.setPosition(0.013)
finger2.setPosition(0.013)
# Ждать пока захват закрывается.
robot.step(50 * timestep)

# Поднятие руки.
armMotors[1].setPosition(0)
# Ждать пока рука не поднята.
robot.step(200 * timestep)

# Развернуть робота.
wheels[0].setVelocity(2.5)
wheels[1].setVelocity(-2.5)
wheels[2].setVelocity(2.5)
wheels[3].setVelocity(-2.5)
# Ждать пока робот развернётся за фиксированное количество шагов времени (тиков).
robot.step(690 * timestep)

# Двигаться вперёд.
wheels[1].setVelocity(2.5)
wheels[3].setVelocity(2.5)
robot.step(900 * timestep)

# Повернуть робота.
wheels[0].setVelocity(1.0)
wheels[1].setVelocity(-1.0)
wheels[2].setVelocity(1.0)
wheels[3].setVelocity(-1.0)
robot.step(200 * timestep)

# Двигаться вперёд.
wheels[1].setVelocity(1.0)
wheels[3].setVelocity(1.0)
robot.step(300 * timestep)

# Повернуть робота.
wheels[0].setVelocity(1.0)
wheels[1].setVelocity(-1.0)
wheels[2].setVelocity(1.0)
wheels[3].setVelocity(-1.0)
robot.step(130 * timestep)

# Двигаться вперёд.
wheels[1].setVelocity(1.0)
wheels[3].setVelocity(1.0)
robot.step(310 * timestep)

# Стоп.
for wheel in wheels:
    wheel.setVelocity(0.0)

# Опустить руку.
armMotors[3].setPosition(0)
armMotors[2].setPosition(-0.3)
robot.step(200 * timestep)

armMotors[1].setPosition(-1.0)
robot.step(200 * timestep)

armMotors[3].setPosition(-1.0)
robot.step(200 * timestep)

armMotors[2].setPosition(-0.4)
robot.step(50 * timestep)

# Открыть захват.
finger1.setPosition(fingerMaxPosition)
finger2.setPosition(fingerMaxPosition)
robot.step(50 * timestep)

