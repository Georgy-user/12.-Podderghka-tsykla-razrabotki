import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        runner_1 = Runner('spartac')
        for i in range(10):
            runner_1.walk()
        try:
            self.assertEqual(runner_1.distance, 50)
        except:
            print(f'Функция Runner.walk() проверена на бегуне {runner_1}. '
                  f'Обнаружена ошибка: расстояние {runner_1.distance} != 50.')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        runner_2 = Runner('dynamo')
        for i in range(10):
            runner_2.run()
        try:
            self.assertEqual(runner_2.distance, 100)
        except:
            print(f'Функция Runner.run() проверена на бегуне {runner_2}. '
                  f'Обнаружена ошибка: расстояние {runner_2.distance} != 100.')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        runner_3 = Runner('zenit_1')
        runner_4 = Runner('zenit_2')
        for i in range(10):
            runner_3.run()
            runner_4.walk()
        try:
            self.assertNotEqual(runner_3.distance, runner_4.distance)
        except:
            print(f'Сравнение функций Runner.run() и Runner.walk() проведено на бегунах {runner_3} и {runner_4}.')
            print(f'Обнаружена ошибка: дистанция {runner_3.distance}, которую пробежал бегун {runner_3},'
                  f'равна дистанции {runner_4.distance}, которую прошёл бегун {runner_4}.')


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def setUp(self):
        self.runner_1 = Runner('Usein', 10)
        self.runner_2 = Runner('Andrei', 9)
        self.runner_3 = Runner('Nik', 3)

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results.keys():
            print(cls.all_results[key])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_Tour_1(self):
        self.Tour_1 = Tournament(90, self.runner_1, self.runner_3)

        """
        Далее используется словарь tour_result, в котором содержится информация о конкретном забеге 
        (об объекте класса Tournament). Ключами словаря являются занятые в забеге места.
        Значения словаря tour_result - имена бегунов.
        """
        tour_result = self.Tour_1.start()
        max_key = max(tour_result.keys())
        TournamentTest.all_results[1] = tour_result
        try:
            self.assertTrue(tour_result[max_key] == 'Nik', True)
            print(f'Класс Tournament протестирован на забеге 1. '
                  f'Ошибок не обнаружено: бегун {self.runner_3}, имеющий меньшую скорость, '
                  f'пробежал медленнее бегунов(-а), имеющих(-его) большую скорость.')
        except:
            print(f'Класс Tournament протестирован на забеге 1. '
                  f'Обнаружена ошибка: бегун {self.runner_3}, имеющий меньшую скорость, '
                  f'пробежал быстрее бегунов(-а), имеющих(-его) большую скорость.')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_Tour_2(self):
        self.Tour_2 = Tournament(90, self.runner_2, self.runner_3)
        tour_result = self.Tour_2.start()
        max_key = max(tour_result.keys())
        TournamentTest.all_results[2] = tour_result
        try:
            self.assertTrue(tour_result[max_key] == 'Nik', True)
            print(f'Класс Tournament протестирован на забеге 2. '
                  f'Ошибок не обнаружено: бегун {self.runner_3}, имеющий меньшую скорость, '
                  f'пробежал медленнее бегунов(-а), имеющих(-его) большую скорость.')
        except:
            print(f'Класс Tournament протестирован на забеге 2. '
                  f'Обнаружена ошибка: бегун {self.runner_3}, имеющий меньшую скорость, '
                  f'пробежал быстрее бегунов(-а), имеющих(-его) большую скорость.')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_Tour_3(self):
        self.Tour_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        tour_result = self.Tour_3.start()
        max_key = max(tour_result.keys())
        TournamentTest.all_results[3] = tour_result
        try:
            self.assertTrue(tour_result[max_key] == 'Nik', True)
            print(f'Класс Tournament протестирован на забеге 3. '
                  f'Ошибок не обнаружено: бегун {self.runner_3}, имеющий меньшую скорость, '
                  f'пробежал медленнее бегунов(-а), имеющих(-его) большую скорость.')
        except:
            print(f'Класс Tournament протестирован на забеге 3. '
                  f'Обнаружена ошибка: бегун {self.runner_3}, имеющий меньшую скорость, '
                  f'пробежал быстрее бегунов(-а), имеющих(-его) большую скорость.')


if __name__ == "__main__":
    unittest.main()
