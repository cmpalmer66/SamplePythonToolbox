import settings


class SampleServices(object):
    """
    Demo/test skeleton for toolbox service organization
    """

    def __init__(self):
        reload(settings)

    def service_one_implementation(self, str_param):
        """
        Returns the string parameter sent to it, concatenated with a string from the settings
        """

        return "{0} {1}".format(settings.setting_string, str_param)

    def service_two_implementation(self, param1, param2):
        """
        Adds the two integer parameters
        """
        try:
            total = param1 + param2

            return total

        except:
            return 0

    def service_three_implementation(self, str_param):
        """
        reverses the string parameter
        """

        return str_param[::-1]
