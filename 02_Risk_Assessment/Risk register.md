## Risk register

### **Operational environment:**

The bank is located in a coastal area with low crime rates. Many people
and systems handle the bank\'s data---100 on-premise employees and 20
remote employees. The customer base of the bank includes 2,000
individual accounts and 200 commercial accounts. The bank\'s services
are marketed by a professional sports team and ten local businesses in
the community. There are strict financial regulations that require the
bank to secure their data and funds, like having enough cash available
each day to meet Federal Reserve requirements.

  -----------------------------------------------------------------------------------------------------------
  **Asset**   **Risk(s)**             **Description**          **Likelihood**   **Severity**   **Priority**
  ----------- ----------------------- ------------------------ ---------------- -------------- --------------
  Funds       Business email          *An employee is tricked  3                3              9
              compromise              into sharing                                             
                                      confidential                                             
                                      information.*                                            

              Compromised user        *Customer data is poorly 2                3              6
              database                encrypted.*                                              

              Financial records leak  *A database server of    3                3              9
                                      backed up data is                                        
                                      publicly accessible.*                                    

              Theft                   *The bank\'s safe is     1                3              6
                                      left unlocked.*                                          

              Supply chain disruption *Delivery delays due to  1                1              1
                                      natural disasters.*                                      

  Notes       *The most critical                                                               
              include [social                                                                  
              engineering                                                                      
              threats]{.underline}                                                             
              like business email                                                              
              compromise, [data                                                                
              exposure]{.underline}                                                            
              due to weak encryption                                                           
              or unsecured backups.                                                            
              The likelihood of theft                                                          
              is low since the                                                                 
              physical location of                                                             
              the bank is within an                                                            
              area of low crime                                                                
              traffic. While physical                                                          
              theft is considered                                                              
              less likely, the                                                                 
              presence of sensitive                                                            
              financial assets and                                                             
              regulatory obligations                                                           
              underscores the need                                                             
              for strong security                                                              
              controls and regular                                                             
              audits.*                                                                         
  -----------------------------------------------------------------------------------------------------------

**Asset:** The asset at risk of being harmed, damaged, or stolen.

**Risk(s):** A potential risk to the organization\'s information systems
and data.

**Description:** A vulnerability that might lead to a security incident.

**Likelihood:** Score from 1-3 of the chances of a vulnerability being
exploited. A 1 means there\'s a low likelihood, a 2 means there\'s a
moderate likelihood, and a 3 means there\'s a high likelihood.

**Severity:** Score from 1-3 of the potential damage the threat would
cause to the business. A 1 means a low severity impact, a 2 is a
moderate severity impact, and a 3 is a high severity impact.

**Priority:** How quickly a risk should be addressed to avoid the
potential incident. Use the following formula to calculate the overall
score: **Likelihood x Impact Severity = Risk**

## Sample risk matrix

+-----------------+-----------------+-----------------+-----------------+
|                 | Low             | Moderate        | Catastrophic    |
|                 |                 |                 |                 |
|                 | 1               | 2               | 3               |
+=================+=================+=================+=================+
| Certain         | 3               | 6               | 9               |
|                 |                 |                 |                 |
| 3               |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Likely          | 2               | 4               | 6               |
|                 |                 |                 |                 |
| 2               |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Rare            | 1               | 2               | 3               |
|                 |                 |                 |                 |
| 1               |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
