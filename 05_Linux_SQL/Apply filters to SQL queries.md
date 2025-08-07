# Apply filters to SQL queries

## Project description

I recently discovered some potential security issues that involve login
attempts and employee machines. So, I am going to examine the
organization's data in their employees and log_in_attempts tables. I
will use SQL filters to retrieve records from different datasets and
investigate the potential security issues.

## Retrieve after hours failed login attempts

SELECT \*

FROM log_in_attempts

WHERE login_time \> '18:00:00' AND success = 0;

Here, I am filtering for all records where there were failed login
attempts after 6:00pm. I use the AND operator to indicate that both
conditions have to be met. The success column contains a boolean where 1
is true and 0 is false.

## Retrieve login attempts on specific dates

SELECT \*

FROM log_in_attempts

WHERE login_date = '2022-05-08' OR login_date = '2022-05-09';

I am filtering for all records where there was an attempt to login on
May 8, 2022 or May 9, 2022. I use the OR operator to show that either
condition can be met, in this way I'm able to see the login attempts
from both days.

## Retrieve login attempts outside of Mexico

SELECT \*

FROM log_in_attempts

WHERE NOT country LIKE 'MEX%';

Here, I filtered for records showing login attempts not originating in
Mexico. I used the NOT operator to negate the country and then I used
the LIKE keyword to specify any country beginning with MEX, by typing
'MEX%' since in the table it can display 'MEX' or 'MEXICO'.

## Retrieve employees in Marketing

SELECT \*

FROM employees

WHERE department = 'Marketing' AND office LIKE 'East%';

Filtered for records from the employees table to show employees from the
Marketing department and who has an office in the East building. Again I
had to use the LIKE keyword and % sign to filter any records from the
office column beginning with East, since the values can be like East-170
or East-139.

## Retrieve employees in Finance or Sales

SELECT \*

FROM employees

WHERE department = 'Finance' OR department = 'Sales';

This filters for all employees who are in the Finance department or the
Sales department. Although both conditions are based on the same column,
I must write out both full conditions, therefore I typed department as
the column in both conditions.

## Retrieve all employees not in IT

SELECT \*

FROM employees

WHERE NOT department = 'Information Technology';

This filters for all employees who are not in the IT department. I use
the NOT operator to negate columns containing Information Technology.

## Summary

In this project, I used SQL to investigate a potential security issue by
filtering login attempts and employee data. I applied *AND, OR, NOT,*
and *LIKE* to identify failed logins, activity on key dates, and access
from outside Mexico. These queries also supported targeted security
updates for specific departments and locations.
