# Security risk assessment report 

+--------------------------------------------------------+-------------+
| **Part 1: Select up to three hardening tools and       |             |
| methods to implement**                                 |             |
+========================================================+=============+
| **Implement Password Policies and Privileged Access    |             |
| Management (PAM):**                                    |             |
|                                                        |             |
| -   Enforce strong, unique passwords and prohibit      |             |
|     > password sharing.                                |             |
|                                                        |             |
| -   Rotate administrative credentials and prevent the  |             |
|     > use of default passwords.                        |             |
|                                                        |             |
| -   Store passwords in a secure password manager.      |             |
|                                                        |             |
| **Configure Firewall Rules and Traffic Filtering:**    |             |
|                                                        |             |
| -   Set up inbound and outbound traffic rules to       |             |
|     > restrict unnecessary access.                     |             |
|                                                        |             |
| -   Use application-layer firewalls to monitor and     |             |
|     > block suspicious activity.                       |             |
|                                                        |             |
| -   Regularly audit firewall logs and configurations.  |             |
|                                                        |             |
| **Enable Multi-Factor Authentication (MFA):**          |             |
|                                                        |             |
| -   Require MFA for all user accounts, especially for  |             |
|     > administrative access and sensitive systems.     |             |
|                                                        |             |
| -   Use app-based or hardware token MFA over SMS-based |             |
|     > for better security.                             |             |
|                                                        |             |
| -   Integrate MFA with the organization\'s identity    |             |
|     > provider or SSO platform.                        |             |
+--------------------------------------------------------+-------------+
|                                                        |             |
+--------------------------------------------------------+-------------+

+-----------------------------------------------------------------------+
| **Part 2: Explain your recommendations**                              |
+=======================================================================+
| By enforcing password policies and using a secure password management |
| solution, each user will have a unique login. This makes it easier to |
| audit access and prevent internal misuse or external compromise.      |
|                                                                       |
| Default passwords are widely known and targeted by attackers. Using   |
| Privileged Access Management tools, the organization can rotate       |
| high-risk passwords regularly and enforce strong password complexity  |
| for administrative accounts. This will significantly reduce the       |
| likelihood of brute force and credential stuffing attacks.            |
|                                                                       |
| By configuring firewall rules, the organization can restrict access   |
| based on IP address, protocol, and application. This helps prevent    |
| unauthorized access, contain breaches, and detect early signs of      |
| attack.                                                               |
|                                                                       |
| MFA adds a second layer of security, preventing unauthorized users    |
| from accessing accounts even if passwords are compromised. This is    |
| especially important for admin accounts and customer data systems.    |
|                                                                       |
| These network hardening practices should be incorporated into the     |
| organization's security policy and enforced consistently. For         |
| example, firewall audits should occur at least once per month, and    |
| password policies must be reviewed quarterly. If these practices are  |
| ignored, the organization may remain vulnerable to similar breaches,  |
| resulting in repeated loss of customer trust, data exfiltration, or   |
| non-compliance penalties.                                             |
+-----------------------------------------------------------------------+
