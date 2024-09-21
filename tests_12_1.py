import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner_1 = Runner('spartac')
        for i in range(10):
            runner_1.walk()
        try:
            self.assertEqual(runner_1.distance, 50)
            print(f'Функция Runner.walk() проверена на бегуне {runner_1}. Ошибок нет.')
        except:
            print(f'Функция Runner.walk() проверена на бегуне {runner_1}. '
                  f'Обнаружена ошибка: расстояние {runner_1.distance} != 50.')

    def test_run(self):
        runner_2 = Runner('dynamo')
        for i in range(10):
            runner_2.run()
        try:
            self.assertEqual(runner_2.distance, 100)
            print(f'Функция Runner.run() проверена на бегуне {runner_2}. Ошибок нет.')
        except:
            print(f'Функция Runner.run() проверена на бегуне {runner_2}. '
                  f'Обнаружена ошибка: расстояние {runner_2.distance} != 100.')

    def test_challenge(self):
        runner_3 = Runner('zenit_1')
        runner_4 = Runner('zenit_2')
        for i in range(10):
            runner_3.run()
            runner_4.walk()
        try:
            self.assertNotEqual(runner_3.distance, runner_4.distance)
            print(f'Сравнение функций Runner.run() и Runner.walk() проведено на бегунах {runner_3} и {runner_4}.')
            print(f'Ошибка не обнаружена: дистанция {runner_3.distance}, которую пробежал бегун {runner_3},'
                  f'отличается от дистанции {runner_4.distance}, которую прошёл бегун {runner_4}.')
        except:
            print(f'Сравнение функций Runner.run() и Runner.walk() проведено на бегунах {runner_3} и {runner_4}.')
            print(f'Обнаружена ошибка: дистанция {runner_3.distance}, которую пробежал бегун {runner_3},'
                  f'равна дистанции {runner_4.distance}, которую прошёл бегун {runner_4}.')


if __name__ == "__main__":
    unittest.main()
