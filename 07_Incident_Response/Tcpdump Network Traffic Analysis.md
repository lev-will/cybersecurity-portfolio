# Cybersecurity Incident Report: 

# Network Traffic Analysis

+--------------------------------------------------------+-------------+
| Part 1: Provide a summary of the problem found in the  |             |
| DNS and ICMP                                           |             |
|                                                        |             |
| traffic log.                                           |             |
+========================================================+=============+
| The UDP protocol reveals that: **the request for an IP |             |
| address for the domain did not go through on the DNS   |             |
| server, there was no device listening**.               |             |
|                                                        |             |
| This is based on the results of the network analysis,  |             |
| which show that the ICMP echo reply returned the error |             |
| message: **udp port 53 unreachable**                   |             |
|                                                        |             |
| The port noted in the error message is used for: **DNS |             |
| service**                                              |             |
|                                                        |             |
| The most likely issue is: **problem with DNS service** |             |
+--------------------------------------------------------+-------------+
|                                                        |             |
+--------------------------------------------------------+-------------+

+-----------------------------------------------------------------------+
| Part 2: Explain your analysis of the data and provide at least one    |
| cause of the incident.                                                |
+=======================================================================+
| Time incident occurred: **1:24pm**                                    |
|                                                                       |
| Explain how the IT team became aware of the incident: **Several       |
| customers of clients reported that they were not able to access the   |
| client company website www.yummyrecipesforme.com, and saw the error   |
| "destination port unreachable" after waiting for the page to load**   |
|                                                                       |
| Explain the actions taken by the IT department to investigate the     |
| incident: **visited the website and got the same message. Loaded      |
| network analyzer tcpdump and attempted to visit the website again**.  |
|                                                                       |
| Note key findings of the IT department\'s investigation (i.e.,        |
| details related to the port affected, DNS server, etc.): **in sending |
| udp packets to DNS server, receive ICMP packets in return stating     |
| port 53 is unreachable, the + sign after the query identification     |
| number indicates flags with the udp message, and the 'A' indicates    |
| flag with the dns request for a record**                              |
|                                                                       |
| Note a likely cause of the incident: **DNS service not active**       |
+-----------------------------------------------------------------------+
