import unittest

from mutwo.events import basic


class SimultaneousEventTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sequence = basic.SimultaneousEvent(
            [basic.SimpleEvent(1), basic.SimpleEvent(2), basic.SimpleEvent(3)]
        )

    def test_get_duration(self):
        self.assertEqual(self.sequence.duration, 3)

    def test_set_duration(self):
        self.sequence.duration = 1.5
        self.assertEqual(self.sequence[0], 0.5)
        self.assertEqual(self.sequence[1], 1)
        self.assertEqual(self.sequence[2], 1.5)


if __name__ == "__main__":
    unittest.main()