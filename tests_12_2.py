import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self, delta_t):
        self.distance += delta_t * self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:

    tour_number = 0 # Счётчик забегов (тестов).

    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)
        Tournament.tour_number += 1

    def start(self):
        finishers = {}
        speed_multipl = 1
        for participant in self.participants:
            speed_multipl *= participant.speed

        delta_t = self.full_distance / speed_multipl
        """delta_t - гарантированный приведённый интервал времени, позволяющий корректно отследить 
        движение бегунов по дистанции. Этот параметр передаётся функции Runner.run."""

        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run(delta_t)
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
                    
        return finishers
       


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Usein', 10)
        self.runner_2 = Runner('Andrei', 9)
        self.runner_3 = Runner('Nik', 3)

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results.keys():
            print(cls.all_results[key])


    def test_Tour_1(self):
        self.Tour_1 = Tournament(90, self.runner_1, self.runner_3)

        """Проверка коррректности ввода данных бегунов (тестирование прекращается, если один и тот же бегун
        стартовал дважды."""
        data_cor = True
        for i in range(len(self.Tour_1.participants) - 1):
            for j in range(i + 1, len(self.Tour_1.participants)):
                if self.Tour_1.participants[i] == self.Tour_1.participants[j]:
                    data_cor = False
                    break

        if data_cor:

            """
            Далее используется словарь tour_result, в котором содержится информация о конкретном забеге 
            (об объекте класса Tournament). Ключами словаря являются занятые в забеге места.
            Значения словаря tour_result - имена бегунов.
            """
            tour_result = self.Tour_1.start()
            max_key = max(tour_result.keys())
            TournamentTest.all_results[Tournament.tour_number] = tour_result
            try:
                self.assertTrue(tour_result[max_key] == 'Nik', True)
                print(f'Класс Tournament протестирован на забеге {Tournament.tour_number}. '
                      f'Ошибок не обнаружено: бегун {self.runner_3}, имеющий меньшую скорость, '
                      f'пробежал медленнее бегунов(-а), имеющих(-его) большую скорость.')
            except:
                print(f'Класс Tournament протестирован на забеге {Tournament.tour_number}. '
                      f'Обнаружена ошибка: бегун {self.runner_3}, имеющий меньшую скорость, '
                      f'пробежал быстрее бегунов(-а), имеющих(-его) большую скорость.')

        else:
            print(f'Данные для тестирования класса Tournament введены некорректно: в забеге {Tournament.tour_number} '
                  f'один и тот же бегун стартовал дважды. Тестирование не проводилось.')


    def test_Tour_2(self):
        self.Tour_2 = Tournament(90, self.runner_2, self.runner_3)

        """Проверка коррректности ввода данных бегунов (тестирование прекращается, если один и тот же бегун
        стартовал дважды."""
        data_cor = True
        for i in range(len(self.Tour_2.participants) - 1):
            for j in range(i+1, len(self.Tour_2.participants)):
                if self.Tour_2.participants[i] == self.Tour_2.participants[j]:
                    data_cor = False
                    break

        if data_cor:
            """
            Далее используется словарь tour_result, в котором содержится информация о конкретном забеге 
            (об объекте класса Tournament). Ключами словаря являются занятые в забеге места.
            Значения словаря tour_result - имена бегунов.
            """
            tour_result = self.Tour_2.start()
            max_key = max(tour_result.keys())
            TournamentTest.all_results[Tournament.tour_number] = tour_result
            try:
                self.assertTrue(tour_result[max_key] == 'Nik', True)
                print(f'Класс Tournament протестирован на забеге {Tournament.tour_number}. '
                      f'Ошибок не обнаружено: бегун {self.runner_3}, имеющий меньшую скорость, '
                      f'пробежал медленнее бегунов(-а), имеющих(-его) большую скорость.')
            except:
                print(f'Класс Tournament протестирован на забеге {Tournament.tour_number}. '
                      f'Обнаружена ошибка: бегун {self.runner_3}, имеющий меньшую скорость, '
                      f'пробежал быстрее бегунов(-а), имеющих(-его) большую скорость.')

        else:
            print(f'Данные для тестирования класса Tournament введены некорректно: в забеге {Tournament.tour_number} '
                  f'один и тот же бегун стартовал дважды. Тестирование не проводилось.')


    def test_Tour_3(self):
        self.Tour_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)

        """Проверка коррректности ввода данных бегунов (тестирование прекращается, если один и тот же бегун
        стартовал дважды."""
        data_cor = True
        for i in range(len(self.Tour_3.participants) - 1):
            for j in range(i + 1, len(self.Tour_3.participants)):
                if self.Tour_3.participants[i] == self.Tour_3.participants[j]:
                    data_cor = False
                    break

        if data_cor:

            """
            Далее используется словарь tour_result, в котором содержится информация о конкретном забеге 
            (об объекте класса Tournament). Ключами словаря являются занятые в забеге места.
            Значения словаря tour_result - имена бегунов.
            """
            tour_result = self.Tour_3.start()
            max_key = max(tour_result.keys())
            TournamentTest.all_results[Tournament.tour_number] = tour_result
            try:
                self.assertTrue(tour_result[max_key] == 'Nik', True)
                print(f'Класс Tournament протестирован на забеге {Tournament.tour_number}. '
                      f'Ошибок не обнаружено: бегун {self.runner_3}, имеющий меньшую скорость, '
                      f'пробежал медленнее бегунов(-а), имеющих(-его) большую скорость.')
            except:
                print(f'Класс Tournament протестирован на забеге {Tournament.tour_number}. '
                      f'Обнаружена ошибка: бегун {self.runner_3}, имеющий меньшую скорость, '
                      f'пробежал быстрее бегунов(-а), имеющих(-его) большую скорость.')


        else:
            print(f'Данные для тестирования класса Tournament введены некорректно: в забеге {Tournament.tour_number} '
                  f'один и тот же бегун стартовал дважды. Тестирование не проводилось.')


    """Логическая ошибка в методе start класса Tournament состоит в следующем. 
    Бегуны (как потоки) запускаются (стартуют) не одновременно, а в порядке очерёдности их перечисления 
    при создании объекта класса.
    Поэтому если после равного количества запусков функции run для более быстрого и более медленного бегунов: 
    1) дистанция меньше произведения скорости более медленного бегуна на количество запусков, 
    2) более медленный бегун запускается раньше более быстрого, 
    то более медленный бегун финиширует раньше более быстрого.
    
    Общее решение состоит в определении промежутка времени для итераций подсчёта длины пробега. Этот промежуток времени
    должен быть < отношения дистанции забега к произведению скоростей всех бегунов."""

    """Вторая недоработка: метод не учитывает, что скорости бегунов могут быть равны, тогда места делятся 
    между бегунами с равными скоростями."""


    def test_Tour_4(self):
        self.Tour_4 = Tournament(2, self.runner_3, self.runner_1, self.runner_2)
        """"Это тестирование на корректность кода для дистанции, меньшей, чем минимальная скорость 
        (без учёта единиц измерения)."""

        """Проверка коррректности ввода данных бегунов (тестирование прекращается, если один и тот же бегун
        стартовал дважды."""
        data_cor = True
        for i in range(len(self.Tour_4.participants) - 1):
            for j in range(i + 1, len(self.Tour_4.participants)):
                if self.Tour_4.participants[i] == self.Tour_4.participants[j]:
                    data_cor = False
                    break

        if data_cor:

            """
            Далее используется словарь tour_result, в котором содержится информация о конкретном забеге
            (об объекте класса Tournament). Ключами словаря являются занятые в забеге места.
            Значения словаря tour_result - имена бегунов.
            """
            tour_result = self.Tour_4.start()
            max_key = max(tour_result.keys())
            TournamentTest.all_results[Tournament.tour_number] = tour_result
            try:
                self.assertTrue(tour_result[max_key] == 'Nik', True)
                print(f'Класс Tournament протестирован на забеге {Tournament.tour_number}. '
                      f'Ошибок не обнаружено: бегун {self.runner_3}, имеющий меньшую скорость, '
                      f'пробежал медленнее других бегунов, имеющих большую скорость.')
            except:
                print(f'Класс Tournament протестирован на забеге {Tournament.tour_number}. '
                      f'Обнаружена ошибка: бегун {self.runner_3}, имеющий меньшую скорость, '
                      f'пробежал быстрее бегунов(-а), имеющих(-его) большую скорость.')

        else:
            print(f'Данные для тестирования класса Tournament введены некорректно: в забеге {Tournament.tour_number} '
                  f'один и тот же бегун стартовал дважды. Тестирование не проводилось.')

    def test_Tour_5(self):
        self.Tour_5 = Tournament(2, self.runner_2, self.runner_3, self.runner_1)
        """Тест проверяет соответствие скоростей бегунов и занятых ими мест в забеге."""

        dict_participants_and_speed = {} #Это словарь, его ключи - скорости, а значения - имена бегунов.
        for participant in self.Tour_5.participants:
            dict_participants_and_speed[participant.speed] = participant.name
        sort_dict_p_and_s = sorted(dict_participants_and_speed.items(), reverse=True)

        # Отсортированный в порядке убывания скорости список бегунов.
        speed_sorted_list = []
        for i, j in sort_dict_p_and_s:
            speed_sorted_list.append(j)

        """Проверка коррректности ввода данных бегунов (тестирование прекращается, если один и тот же бегун
        стартовал дважды."""
        data_cor = True
        for i in range(len(self.Tour_5.participants) - 1):
            for j in range(i + 1, len(self.Tour_5.participants)):
                if self.Tour_5.participants[i] == self.Tour_5.participants[j]:
                    data_cor = False
                    break

        if data_cor:

            """
            Далее используется словарь tour_result, в котором содержится информация о конкретном забеге
            (об объекте класса Tournament). Ключами словаря являются занятые в забеге места.
            Значения словаря tour_result - имена бегунов.
            """
            tour_result = self.Tour_5.start()
            TournamentTest.all_results[Tournament.tour_number] = tour_result

            # Отсортированный в соответствии с занятым местом список бегунов.
            ordered_tour_result = list(tour_result.values())
            try:
                self.assertEqual(ordered_tour_result, speed_sorted_list)
                print(f'Класс Tournament протестирован на забеге {Tournament.tour_number}. '
                      f'Ошибок не обнаружено: распределение бегунов по местам соответствует '
                      f'их распределению по скоростям.')
            except:
                print(f'Класс Tournament протестирован на забеге {Tournament.tour_number}. '
                      f'Онаружена ошибка: распределение бегунов по местам не соответствует '
                      f'их распределению по скоростям.')



if __name__ == "__main__":
    unittest.main()
