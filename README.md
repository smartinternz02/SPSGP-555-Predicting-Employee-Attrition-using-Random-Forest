<h1><b>Predicting-Employee-Attrition</b></h1>

<h2>Overview</h2>
A common problem in human resources analytics is devising a means to retain the high performing employees as losing them has a negative effect on the company performance as well as their growth.
Apart from the lower productivity from a replacement, the newer employee needs to familiarise themselves with the company operations, the process involved in searching for a new employee, interviewing 
and training (both formal and informal) the newly employed person makes employees’ turnover undesirable. The cost of replacing an employee can vary based on the employee’s skill level; however, the 
cost is usually very high for a highly skilled professional in comparison to an entry-level job. This project presents insights on reasons behind emloyees turnover as well as predictive models on employee turnover.
The model employed include: random forest classifier

<h2>Objective</h2>
Using machine learning to predict employee attrition in Python<br>

<h2>Data Description</h2>
The dataset consists of 25491 obseravtions and 10 variables.<br> Each row in dataset represents an employee; each column contains employee attributes:<br><br>

satisfaction_level (0–1)<br>
last_evaluation (Time since last evaluation in years)<br>
number_projects (Number of projects completed while at work)<br>
average_monthly_hours (Average monthly hours at workplace)<br>
time_spend_company (Time spent at the company in years)<br>
Work_accident (Whether the employee had a workplace accident)<br>
left (Whether the employee left the workplace or not (1 or 0))<br>
promotion_last_5years (Whether the employee was promoted in the last five years)<br>
sales (Department in which they work for)<br>
salary (Relative level of salary)<br>

<h2>Approach</h2>
We perform turnover analysis project by using Python’s Scikit-Learn library. We use Random Forest classifier for employee attrition and measure the accuracy of models that are built.Then we use Flask Frame Work with Machine Learning Model. In this section, we will be building a web application that is integrated into the model we built. A UI is provided for the uses where he has to enter the values for predictions. The enter values are given to the saved model and prediction is showcased on the UI.
To build this flask application we should have basic knowledge of “HTML, CSS, Bootstrap, flask framework and python

<h2>Acknowledgements</h2>
Thanks to Kaggle for providing free access to the dataset
