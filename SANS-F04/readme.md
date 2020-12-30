Sans had a community ctf with a challenge called F04 where you had to brute force the login into a ics panel .
The challenge had ended and for sometime you could still access it, but since it was no longer available I coded a simple python server and client to replicate the challenge.

https://medium.com/@EricaZeli/sans-community-ctf-fuzzing-8a616ad33737

script.py is the client doing the brute forcing

server.py is the server

I have tested the code in linux it works, but in Windows I did get an error about using single quotes ''

An issue I have been meaning to fix is that once the client.py brute forces password to VINT it runs again saying Processing.

No warranty is given for the software and the code is pretty self explanatory and has comments. You are free to copy this specific code sample and do whatever you want with it.
obviously I am not liable for any issues, damage you cause, whatever you do with code sample, and do not condone any illegal activity.

