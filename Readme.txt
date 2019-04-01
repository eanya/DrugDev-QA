
Notes:Postman API Test
-- The Postman API test run with a 100% pass rate, i.e the Login Success and Login Error scripts.
   Please see the collections and environment folder included.
-- Import the collection.json and the environment.json files into postman to run the project or
-- Use newman, navigate to the postman folder and use this command - newman run ./collections/collection.json -e ./environment/environment.json
Updated:01.04.2019

Notes:Python BDD
-- You can port this project anywhere and run it, the code will find the project root by itself.
-- When you import the project in Pycharm IDE, select to run the TestRunner.py file to run this project.
   You can also use the TestRunner.py file in command line to run the project.
-- The Behave BDD test run with a 100% pass rate when ran on Chrome browser,but not for Firefox and Edge.
-- I have set up a crossbrowser test option for chrome and firefox which demonstrates this.
-- I have added more negative tests using Behave Scenerio Outline and Examples applying a low level approach to the feature file, this
   could easily be converted to a high level none technical feature file for non technical stakeholders.
