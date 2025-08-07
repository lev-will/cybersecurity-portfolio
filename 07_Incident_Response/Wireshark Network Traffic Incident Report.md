# Cybersecurity Incident Report

+--------------------------------------------------------+-------------+
| **Section 1: Identify the type of attack that may have |             |
| caused this**                                          |             |
|                                                        |             |
| **network interruption**                               |             |
+========================================================+=============+
| One potential explanation for the website's connection |             |
| timeout error message is a Denial of Service (DoS)     |             |
| attack. Specifically, the logs suggest a SYN flood---a |             |
| type of DoS attack---due to a consistent stream of SYN |             |
| packets originating from a suspicious IP address       |             |
| outside the expected employee IP range.                |             |
|                                                        |             |
| The Wireshark logs indicate a gradual increase in SYN  |             |
| requests sent repeatedly from the same IP address.     |             |
| Over time, these requests overwhelm the server, which  |             |
| eventually stops responding altogether.                |             |
+--------------------------------------------------------+-------------+
|                                                        |             |
+--------------------------------------------------------+-------------+

+-----------------------------------------------------------------------+
| **Section 2: Explain how the attack is causing the website to         |
| malfunction**                                                         |
+=======================================================================+
| When website visitors try to establish a connection with the web      |
| server, a three-way handshake occurs using the TCP protocol. Explain  |
| the three steps of the handshake:                                     |
|                                                                       |
| **1. The visitor's device sends a SYN packet to the server to request |
| a connection.\                                                        |
| **                                                                    |
|                                                                       |
| **2. The server responds with a SYN-ACK packet, acknowledging the     |
| request and reserving resources for the connection.\                  |
| **                                                                    |
|                                                                       |
| **3. The visitor sends back an ACK packet to complete the handshake   |
| and establish the session.**                                          |
|                                                                       |
| Explain what happens when a malicious actor sends a large number of   |
| SYN packets all at once: **In a SYN flood attack, a malicious actor   |
| sends a large volume of SYN packets without completing the handshake. |
| These half-open connections consume server resources, eventually      |
| exhausting the server's ability to respond to legitimate users.**     |
|                                                                       |
| **The logs show that the attacker's IP address initially completes a  |
| successful handshake, but then begins flooding the server with        |
| additional SYN packets. As the server becomes overwhelmed by the      |
| volume of SYN packets and cannot complete the TCP handshakes, it      |
| eventually exhausts its available resources. Without the ability to   |
| open new connections, even legitimate users receive no response. This |
| lack of server acknowledgment causes web browsers to display a        |
| "connection timeout" error, as they fail to establish communication   |
| with the site within the expected timeframe.**                        |
+-----------------------------------------------------------------------+
