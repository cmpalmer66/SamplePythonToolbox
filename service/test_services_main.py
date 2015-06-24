import unittest
import services_main


class TesServices(unittest.TestCase):
    def test_service_one(self):
        instance = services_main.SampleServices()
        out = instance.service_one_implementation("world")
        self.assertEqual(out, "Hello world")

    def test_service_two(self):
        instance = services_main.SampleServices()
        out = instance.service_two_implementation(5, 10)
        self.assertEqual(out, 15)

    def test_service_three(self):
        instance = services_main.SampleServices()
        out = instance.service_three_implementation("abcdefg")
        self.assertEqual(out, "gfedcba")


if __name__ == '__main__':
    unittest.main()
