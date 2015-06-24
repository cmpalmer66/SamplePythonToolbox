from toolpackages.service_one import ServiceOne
from toolpackages.service_two import ServiceTwo
from toolpackages.service_three import ServiceThree


class Toolbox(object):
    def __init__(self):
        '''
        Define the toolbox properties here. Do not change the name of this
        class. ArcGIS locates this class by name. It will not be able to find
        the toolbox and your toolbox will not work if you modify this.
        '''
        self.label = 'Toolbox'
        self.alias = 'SAMPLE'

        # List of tool classes associated with this toolbox
        self.tools = [
            ServiceOne,
            ServiceTwo,
            ServiceThree
        ]
