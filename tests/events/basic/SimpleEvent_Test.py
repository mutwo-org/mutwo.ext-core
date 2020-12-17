import unittest

from mutwo.events import basic


class SimpleEventTest(unittest.TestCase):
    def test_get_assigned_parameter(self):
        duration = 10
        self.assertEqual(
            basic.SimpleEvent(duration).get_parameter("duration"), duration
        )

    def test_get_not_assigned_parameter(self):
        self.assertEqual(basic.SimpleEvent(1).get_parameter("anyParameter"), None)

    def test_set_assigned_parameter_by_object(self):
        simple_event = basic.SimpleEvent(1)
        new_duration = 10
        simple_event.set_parameter("duration", new_duration)
        self.assertEqual(simple_event.duration, new_duration)

    def test_set_assigned_parameter_by_function(self):
        old_duration = 1
        simple_event = basic.SimpleEvent(old_duration)
        simple_event.set_parameter("duration", lambda old_duration: old_duration * 2)
        self.assertEqual(simple_event.duration, old_duration * 2)

    def test_set_not_assigned_parameter(self):
        simple_event = basic.SimpleEvent(1)
        new_unknown_parameter = 10
        new_unknown_parameter_name = "new"
        simple_event.set_parameter("new", new_unknown_parameter)
        self.assertEqual(
            simple_event.get_parameter(new_unknown_parameter_name),
            new_unknown_parameter,
        )


if __name__ == "__main__":
    unittest.main()
