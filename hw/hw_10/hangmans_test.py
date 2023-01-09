import unittest
from hangman import Bank
from hangman import Processes
from hangman import Player


class Hangmantest(unittest.TestCase):

    def test_word_choose(self):
        word_bank = Bank()
        word_bank.current_topic = 'colours'
        word_bank.topics = {'colours': ['Red']}
        word_bank.pick_word()
        self.assertEqual(word_bank.current_word, 'Red')

    def test_topic_choose(self):
        word_bank = Bank()
        word_bank.topic_names = ['Colours']
        word_bank.pick_topic()
        self.assertEqual(word_bank.current_topic, 'Colours')

    def test_choose_word_from_url(self):
        word_bank = Bank()
        word_bank.get_word()
        self.assertNotEqual(word_bank.current_word, None)

    def test_list_khali(self):
        word_bank = Bank()
        word_bank.current_topic = 'colours'
        word_bank.topics = {'colours': ['Red']}
        word_bank.pick_word()
        self.assertNotEqual(word_bank.current_word, None)

    def test_lives(self):
        word_bank = Bank()
        word_bank.current_topic = 'colours'
        word_bank.topics = {'colours': ['Red']}
        word_bank.pick_word()
        player = Player(word_bank)
        self.assertEqual(player.lives, 3*len(word_bank.current_word))

    def test_word_isinstance_class(self):
        word_bank = Bank()
        word_bank.current_topic = 'colours'
        word_bank.topics = {'colours': ['Red']}
        word_bank.pick_word()
        self.assertIsInstance(word_bank, Bank)

    def test_letter_right_position(self):
        word_bank = Bank()
        word_bank.current_topic = 'colours'
        word_bank.topics = {'colours': ['red']}
        word_bank.pick_word()
        player = Player(word_bank)
        player.answer = 'R'
        Processes.check_answer_update_lives(word_bank, player)
        self.assertEqual(word_bank.current_word_display, ['r', '_', '_'])

    def test_2letters_right_position(self):
        word_bank = Bank()
        word_bank.current_topic = 'colours'
        word_bank.topics = {'colours': ['red']}
        word_bank.pick_word()
        player = Player(word_bank)
        player.answer = 'R'
        Processes.check_answer_update_lives(word_bank, player)
        player.answer = 'd'
        Processes.check_answer_update_lives(word_bank, player)
        self.assertEqual(word_bank.current_word_display, ['r', '_', 'd'])

    def test_missed_word(self):
        word_bank = Bank()
        word_bank.current_topic = 'colours'
        word_bank.topics = {'colours': ['Red']}
        word_bank.pick_word()
        player = Player(word_bank)
        player.answer = 'x'
        Processes.check_answer_update_lives(word_bank, player)
        self.assertEqual(player.lives, (3 * len(word_bank.current_word)) - 1)
        self.assertNotEqual(word_bank.letters_already_guessed, None)

    def test_already_guessed(self):
        word_bank = Bank()
        word_bank.current_topic = 'colours'
        word_bank.topics = {'colours': ['Red']}
        word_bank.pick_word()
        player = Player(word_bank)
        player.answer = 'x'
        Processes.check_answer_update_lives(word_bank, player)
        player.answer = 'x'
        a = Processes.check_answer_update_lives(word_bank, player)
        self.assertEqual(a, '\nLetter already guessed.')
        self.assertEqual(player.lives, (3 * len(word_bank.current_word)) - 1)

    def test_wrong_input(self):
        word_bank = Bank()
        word_bank.current_topic = 'colours'
        word_bank.topics = {'colours': ['Red']}
        word_bank.pick_word()
        player = Player(word_bank)
        player.answer = '1'
        Processes.validate_user_input(player)
        self.assertEqual(Processes.validate_user_input(player), '\nPlease guess a single alphabet')

    def test_right_input(self):
        word_bank = Bank()
        word_bank.current_topic = 'colours'
        word_bank.topics = {'colours': ['Red']}
        word_bank.pick_word()
        player = Player(word_bank)
        player.answer = 'w'
        Processes.validate_user_input(player)
        self.assertEqual(Processes.validate_user_input(player), True)

    def test_lowercase_word(self):
        word_bank = Bank()
        word_bank.current_topic = 'colours'
        word_bank.topics = {'colours': ['red']}
        word_bank.pick_word()
        player = Player(word_bank)
        player.answer = 'R'
        Processes.check_answer_update_lives(word_bank, player)
        self.assertEqual(word_bank.current_word_display, ['r', '_', '_'])

    def test_win(self):
        word_bank = Bank()
        word_bank.current_topic = 'colours'
        word_bank.topics = {'colours': ['red']}
        word_bank.pick_word()
        player = Player(word_bank)
        player.answer = 'R'
        Processes.check_answer_update_lives(word_bank, player)
        player.answer = 'e'
        Processes.check_answer_update_lives(word_bank, player)
        player.answer = 'D'
        Processes.check_answer_update_lives(word_bank, player)
        word_bank.check_solve()
        self.assertEqual(word_bank.not_solved, False)

    def test_lose(self):
        word_bank = Bank()
        word_bank.current_topic = 'colours'
        word_bank.topics = {'colours': ['red']}
        word_bank.pick_word()
        player = Player(word_bank)
        player.answer = 'R'
        Processes.check_answer_update_lives(word_bank, player)
        player.answer = 'e'
        Processes.check_answer_update_lives(word_bank, player)
        player.answer = 'h'
        Processes.check_answer_update_lives(word_bank, player)
        player.answer = 'f'
        Processes.check_answer_update_lives(word_bank, player)
        player.answer = 'l'
        Processes.check_answer_update_lives(word_bank, player)
        player.answer = 'p'
        Processes.check_answer_update_lives(word_bank, player)
        player.answer = 'q'
        Processes.check_answer_update_lives(word_bank, player)
        player.answer = 's'
        Processes.check_answer_update_lives(word_bank, player)
        player.answer = 'n'
        Processes.check_answer_update_lives(word_bank, player)
        player.answer = 'z'
        Processes.check_answer_update_lives(word_bank, player)
        player.answer = 'v'
        Processes.check_answer_update_lives(word_bank, player)
        word_bank.check_solve()
        self.assertEqual(player.lives, 0)
        self.assertEqual(word_bank.not_solved, True)


if __name__ == '__main__':
    unittest.main()
