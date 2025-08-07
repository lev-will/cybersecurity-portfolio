# Security incident report

  -----------------------------------------------------------------------
  **Section 1: Identify the network protocol involved in   
  the incident**                                           
  -------------------------------------------------------- --------------
  DNS, HTTP, TCP                                           

                                                           
  -----------------------------------------------------------------------

+-----------------------------------------------------------------------+
| **Section 2: Document the incident**                                  |
+=======================================================================+
| A customer contacted the support team to report suspicious behavior   |
| after visiting the yummyrecipesforme.com website. They stated they    |
| were prompted to download a file in order to access free recipes.     |
| After running the file, their computer became noticeably slower, and  |
| the website address in the browser changed unexpectedly.              |
|                                                                       |
| To investigate, we created a sandbox environment to safely interact   |
| with the website without risking impact to the production network.    |
| While monitoring traffic using tcpdump, we observed the following:    |
|                                                                       |
| A DNS query is sent to resolve *yummyrecipesforme.com.*               |
|                                                                       |
| A TCP three-way handshake follows, then an HTTP GET request is made.  |
|                                                                       |
| The browser prompts the user to download a suspicious *.exe* file.    |
|                                                                       |
| After execution, a second DNS query is made for                       |
| *greatrecipesforme.com.*                                              |
|                                                                       |
| The system then initiates a second TCP/HTTP connection to the new     |
| domain, indicating redirection by malware.                            |
|                                                                       |
| This suggests that the **original website's source code was altered** |
| to trigger a malicious download and redirect users to an external,    |
| potentially compromised site.                                         |
|                                                                       |
| Upon further review, the analyst attempted to access the website's    |
| admin panel but found login credentials no longer worked. This        |
| suggests that administrative access may have been compromised. While  |
| the exact method of access is not confirmed, the lack of account      |
| lockout or two-factor authentication indicates that a **brute force   |
| attack is a likely possibility**, especially if default credentials   |
| were still in place                                                   |
+-----------------------------------------------------------------------+

  -----------------------------------------------------------------------
  **Section 3: Recommend one remediation for brute force attacks**
  -----------------------------------------------------------------------
  Implement account lockout and rate-limiting controls for the
  administrative login. After a certain number of failed login attempts,
  temporarily block access to the account and alert security personnel.
  Additionally, enforce the use of strong, non-default passwords and
  enable multi-factor authentication (MFA) on all administrator accounts.

  -----------------------------------------------------------------------
