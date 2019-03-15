# Python AWS Lambda Skeleton

## Directory Structure
This is a structure for a python AWS Lambda solution.
In this structure the AWS Lambda which make the solution are directories in the root of the project's solution (i.e. `aws_lambda/`), and inside it we can find the following structure:
* main/
* test/
* lambda.py

### 'main/' directory
The **main/** directory contains the Lambda Handler class, i.e. *LambdaHandler.py*, any helper class and the modules used by these classes.

### 'test/' directory
The **test/** directory contains all the tests for the lambda handler and the helper classes of this AWS Lambda solution, i.e. `LambdaHelper_test.py`

### 'lambda.py' script
This is the entry point for the AWS Lambda function.
When configuring the AWS Lambda function the 'Handler' should be  `lambda.handler`. This script imports the lambda handler class, i.e. `from main.LambdaHandler import LambdaHandler`.

## Considerations During Development and Preparing Deployment
* If during the development of the lambda or the tests there is the need of installing 3rd party modules, these modules should be installed inside the **modules/** subdirectory of **main/** or **test/** directories. And then they should be imported from the package **modules**, i.e:
**Install `requests` the module in *modules/*:**
```
$ pip install requests -t aws_lambda/main/modules
```
**Import `requests` in *LambdaHandler.py*:**
```
from modules.requests import request
```
* To prepare the zip file, we just need to zip the `lambda.py` and the `modules/` directory keeping the relative structure.

## Running The Tests
In order to run the tests we just need to run the following command from the root of the project:
```
$ python -m unittest discover -p '*_test.py'
```
This will run the tests for all the solution. Of course we can build the tests using any other testing tool, like `nose` and in that case we need to run them a bit different, depending on the tool used.