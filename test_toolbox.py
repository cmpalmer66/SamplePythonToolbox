import os
import unittest
import arcpy


class TestToolbox(unittest.TestCase):
    def test_service_one(self):
        path = os.path.dirname(os.path.realpath(__file__))
        arcpy.ImportToolbox(path + r'\toolbox.pyt')

        result = arcpy.ServiceOne_SAMPLE("Hello")
        self.assertEqual("Hello Hello", result.getOutput(0))

    def test_service_two(self):
        path = os.path.dirname(os.path.realpath(__file__))
        arcpy.ImportToolbox(path + r'\toolbox.pyt')

        result = arcpy.ServiceTwo_SAMPLE(5, 10)
        self.assertEqual(15, int(result.getOutput(0)))

    def test_service_three(self):
        path = os.path.dirname(os.path.realpath(__file__))
        arcpy.ImportToolbox(path + r'\toolbox.pyt')

        result = arcpy.ServiceThree_SAMPLE("Hello")
        self.assertEqual("olleH", result.getOutput(0))


if __name__ == '__main__':
    unittest.main()
