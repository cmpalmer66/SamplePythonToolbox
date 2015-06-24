# SamplePythonToolbox
Sample project for testing ArcGIS Python Toolbox file structures

This project defines a single ArcGIS Python Toolbox called "Toolbox" with three tools, 
ServiceOne, ServiceTwo, and ServiceThree.

The Toolbox is defined in toolbox.pyt and each tool is defined in toolpackages/service_*.py, but the 
actual implementation code is in service/services_main.py.

These have been tested in ArcMap and ArcCatalog and should be able to be executed, added to the ArcToolbox, or published
on ArcGIS Server (although the dependent directories will have to be copied to the deployment location - more about
that if anyone is interested or has better ideas on deploying them).

## Unit Testing
There are also two levels of unit testing. 

test_services_main.py has unit tests for the individual service
implementations, independent of the toolbox configuration (and in this case independent of arcpy itself since 
these demo services just manipulate and send back their parameters).

test_toolbox.py has units tests for the Toolbox implementation. Each test loads the Toolbox (should be organized better 
setup and teardown procedures - feel free) and executes one of the tools and tests the output. If this set of unit tests
passes, it should be good to go in ArcMap, ArcCatalog, or ArcGIS Server.
