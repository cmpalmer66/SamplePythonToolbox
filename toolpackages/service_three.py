import service.services_main
import arcpy_utils.toolbox_utils as utils


class ServiceThree(object):
    """
    Demo Service Three
    """

    def __init__(self):
        """
        Define the tool class attributes, including your tool parameters.
        """
        self.label = 'ServiceThree'
        self.canRunInBackground = False

        self.parameters = [
            # Create your parameters here using the parameter function.
            # Make sure you leave the enclosing brackets and separate your
            # parameters using commas.
            utils.make_parameter('First Parameter', 'str_param', 'GPString'),
            utils.make_parameter('Output', 'output', 'GPString',
                                 parameterType='Derived', direction='Output')
        ]

    def getParameterInfo(self):
        """
        Return your parameter list defined in the __init__ method for the tool.
        If you want to set any additional properties, such as filters, for your
        parameters, do this here. Just reference them using their index in the
        parameter list"""

        # self.param[0].filter.list = ['Option1', 'Option2', 'Option3']
        # self.param[1].filter.list = ['xml'] # only xml files for DEFile

        return self.parameters

    def isLicensed(self):
        """
        Set whether tool is licensed to execute and replace this text with a
        good explanation of what you are doing here.
        """
        return True

    def updateParameters(self, parameters):
        """
        Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed.
        """
        return

    def updateMessages(self, parameters):
        """
        Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation.
        """
        return

    def execute(self, parameters, messages):
        """
        Reference the business logic captured in your object defined
        separately in the module, preferably above.
        """
        try:

            instance = service.services_main.SampleServices()  # create object instance
            str_param = parameters[0].valueAsText

            out = instance.service_three_implementation(str_param)

            parameters[1].value = out

        except Exception, ErrorDesc:
            sErr = "ERROR:\n" + str(ErrorDesc)
            messages.addErrorMessage(sErr)

        return
