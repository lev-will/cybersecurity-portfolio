## PASTA(Process for Attack Simulation and Threat Analysis) worksheet

+------------------+---------------------------------------------------+
| ### **Stages**   | ### **Sneaker company**                           |
+==================+===================================================+
| **I. Define      | Make **2-3 notes** of specific business           |
| business and     | requirements that will be analyzed.               |
| security         |                                                   |
| objectives**     | -   *Will the app process transactions?*          |
|                  |                                                   |
|                  | -   *Does it do a lot of back-end processing?*    |
|                  |                                                   |
|                  | -   *Are there industry regulations that need to  |
|                  |     > be considered?*                             |
|                  |                                                   |
|                  | *App will connect buyers and sellers. Buyers will |
|                  | be able to rate their shopping experience with    |
|                  | sellers. Proper payment handling will be needed   |
|                  | to avoid legal issues, compliance with PCI-DSS.   |
|                  | There is a lot of back-end processing taking      |
|                  | place.*                                           |
+------------------+---------------------------------------------------+
| **II. Define the | List of technologies used by the application:     |
| technical        |                                                   |
| scope**          | -   *Application programming interface (API)*     |
|                  |                                                   |
|                  | -   *Public key infrastructure (PKI)*             |
|                  |                                                   |
|                  | -   *SHA-256*                                     |
|                  |                                                   |
|                  | -   *SQL*                                         |
|                  |                                                   |
|                  | Write **2-3 sentences** (40-60 words) that        |
|                  | describe why you choose to prioritize that        |
|                  | technology over the others.                       |
|                  |                                                   |
|                  | *I would prioritize APIs since it handles a lot   |
|                  | of data between customers, employees, and         |
|                  | partners. Because they have such a large attack   |
|                  | surface they would be most prone to security      |
|                  | vulnerabilities. Since APIs are usually third     |
|                  | parties would have to consider which ones are     |
|                  | being used before proceeding with how best to     |
|                  | address them.*                                    |
+------------------+---------------------------------------------------+
| **III. Decompose | [[Sample data flow                                |
| application**    | diagram]{.und                                     |
|                  | erline}](https://docs.google.com/presentation/d/1 |
|                  | ol7y79popTFfNHM-90ES-H-i1Lpd0YNvPShxBlXozjg/templ |
|                  | ate/preview?resourcekey=0-DZAkf7Vzh2PXsP-j3oXV-g) |
|                  |                                                   |
|                  | The user is going to input data into the app to   |
|                  | search the database for a particular product.     |
+------------------+---------------------------------------------------+
| **IV. Threat     | List **2 types of threats** in the PASTA          |
| analysis**       | worksheet that are risks to the information being |
|                  | handled by the application.                       |
|                  |                                                   |
|                  | -   *What are the internal threats?*              |
|                  |                                                   |
|                  | -   *What are the external threats?*              |
|                  |                                                   |
|                  | *Social engineering tactics on an employee could  |
|                  | be an internal threat.*                           |
|                  |                                                   |
|                  | *SQL injection is an external threat*             |
|                  |                                                   |
|                  | *Session hijacking*                               |
+------------------+---------------------------------------------------+
| **V.             | List **2 vulnerabilities** in the PASTA worksheet |
| Vulnerability    | that could be exploited.                          |
| analysis**       |                                                   |
|                  | -   *Could there be things wrong with the         |
|                  |     > codebase?*                                  |
|                  |                                                   |
|                  | -   *Could there be weaknesses in the database?*  |
|                  |                                                   |
|                  | -   *Could there be flaws in the network?*        |
|                  |                                                   |
|                  | *If there is a lack of input validation, code can |
|                  | be injected into spaces for user input.*          |
|                  |                                                   |
|                  | *A lack of secure session expiration, perhaps     |
|                  | when making a payment.*                           |
+------------------+---------------------------------------------------+
| **VI. Attack     | [[Sample attack tree                              |
| modeling**       | diagram]{.underline}](htt                         |
|                  | ps://docs.google.com/presentation/d/1FmWLyHgmq9XQ |
|                  | oVuMxOym2PHO8IuedCkan4moYnI-EJ0/template/preview? |
|                  | usp=sharing&resourcekey=0-zYPY7AhPJdcClXamlAfOag) |
|                  |                                                   |
|                  | *Shows areas where a user inputs data could be    |
|                  | open to SQL injection or session hijacking.*      |
+------------------+---------------------------------------------------+
| **VII. Risk      | List **4 security controls** that you've learned  |
| analysis and     | about that can reduce risk.                       |
| impact**         |                                                   |
|                  | *Password policies*                               |
|                  |                                                   |
|                  | *Least privilege*                                 |
|                  |                                                   |
|                  | *Hashing and salting*                             |
|                  |                                                   |
|                  | *Code sanitizing*                                 |
+------------------+---------------------------------------------------+
