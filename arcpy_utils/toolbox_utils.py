import arcpy


def int_param_check(param):
    """
    Takes an ArcPy parameter and gets its string value. If it is '', return 0. Otherwise cast
    it to an int. On error, return 0 anyway
    """
    try:
        val = param.valueAsText
        retval = int(val) if val <> '' else 0

        return retval
    except ValueError:
        return 0


def make_parameter(displayName, name, datatype, defaultValue=None,
                   parameterType='Optional', direction='Input'):
    """
    This method prepopulates the paramaeterType
    and direction parameters and leaves the setting a default value for the
    newly created parameter as optional. The displayName, name and datatype are
    the only required inputs.
    """
    # create parameter with a few defaults
    param = arcpy.Parameter(
        displayName=displayName,
        name=name,
        datatype=datatype,
        parameterType=parameterType,
        direction=direction)

    # set new parameter to a default value
    param.value = defaultValue

    # return the complete parameter object
    return param
