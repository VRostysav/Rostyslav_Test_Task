# Rostyslav_Test_Task

In this project, where the next scenarios was automated:

1. Visit https://useinsider.com/ and check Insider home page is opened or not
2. Select the “Company” menu in the navigation bar, select “Careers” and check Career
   page, its Locations, Teams and Life at Insider blocks are open or not
3. Go to https://useinsider.com/careers/quality-assurance/, click “See all QA
   jobs”, filter jobs by Location - Istanbul, Turkey and department - Quality
  Assurance, check the presence of the jobs list
4. Check that all jobs’ Position contains “Quality Assurance”, Department
contains “Quality Assurance”, Location contains “Istanbul, Turkey
5. Click the “View Role” button and check that this action redirects us to Lever
Application form page

### Prerequisites
In this section, you will find all the necessary steps which should be done before running the application:

1. Download Python to your machine (3.10 preferably)
2. Add Python to environment variables
3. Download any IDE of your choice
4. Clone the repo
   ```sh git clone https://github.com/VRostysav/Rostyslav_Test_Task ```
5. Install requirements from the requirements.txt file
   
### How to start the test execution
1. In the IDE terminal run the command to run all tests ```pytest -m -v ```
2. In case you don't want to see a warning in the console run the next command  ```pytest -m -v:no:warnings```
3. IF you want to run some specific test case run the command with the appropriate Pytest mark ```pytest -m tcid```.
   All Pytest marks can be found in  ```Test ``` directory in the project

