#  Sniff Sniff Whoopsie

Our employee just deployed a network sniffer tools and I think you might find something interesting in the captured files!

* A port scanning activity is detected in the system. Is it true or false positive? Please do screenshot any kind of proofs including all the port numbers involved and report the open ports.
* A PHP CVE Exploitation is detected by our SIEM. Is it true or false positive? Please do screenshot any kind of proofs.
* We accidentally exposed some ports due to Firewall misconfiguration. Can you tell me which port that responsible to open up a connection for file transfers?
* What does the attacker download from the file transfer port related?
* Any chance the attacker download an internal file which should not be public? Our developer is pretty clumsy that he puts some kind of confidential hint in the website.
* Please answer this question if the previous ones is true. What was the content of the protected file ONLY IF the attacker steal/download the file? Is the password pretty strong?
* There's one FLAG indicating the password disclosure on one of the authenticated ports. Can you find it? [BONUS]