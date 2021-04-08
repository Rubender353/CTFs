# SANS Cyber FastTrack Sprint 2021 Writeups

# Binaries Challenges

## BE01
This one was simple just extract the folder in Windows. Change chicken.pdf to chicken.zip extension and keep extracting until you get to the flag
Other option is to use binwalk
![image](https://user-images.githubusercontent.com/31175996/114052703-1e173400-9843-11eb-8b2b-0c4f4d527db6.png)

## BE02
It says rot13 is input so maybe there was another way to trigger this with rot13 formated code
I used a bunch of random characters and kept applying it until I got a buffer overflow that showed the flag

![GetImage](https://user-images.githubusercontent.com/31175996/114052972-5f0f4880-9843-11eb-9f1a-c9036fe74882.png)

## BM01 

Running strings didn't work because it's in Russian cyryllic language. In order to show those in strings you probably have to use someother option.
Putting huge amount of input didn't cause crash so most likely its set to accept specific input size. 
I tried objdump and gdb with breaks but it didn't work.
I opened it in IDA and viewed strings and came across hammer123 in russian this worked once you input it in russian 

![GetImage (1)](https://user-images.githubusercontent.com/31175996/114053502-db099080-9843-11eb-800c-d9130b7635ed.png)

# Network Challenges
## NE01
Nmap that address and then nc to the port to get flag 
![GetImage (2)](https://user-images.githubusercontent.com/31175996/114053972-48b5bc80-9844-11eb-8341-d8c25a3c2776.png)
![image](https://user-images.githubusercontent.com/31175996/114054218-81559600-9844-11eb-974a-d36f1ad0036d.png)

## NM01
When you nc to the address it gives you hex I tried random characters and just pasting the hex they give. None worked 
![GetImage (3)](https://user-images.githubusercontent.com/31175996/114054340-a2b68200-9844-11eb-8840-c01de18ed2f5.png)

I then noticed that the connection would just end with no message if I converted the hex to ascii and put that in. I tried various other ways such as echo "" and putting string in "". 

![GetImage (4)](https://user-images.githubusercontent.com/31175996/114054375-ab0ebd00-9844-11eb-9648-c85e778dff8b.png)

Nothing worked so I assumed that the hex probably repeats so I just piped one of the previous hex strings from echo to nc. Kept doing that until I got the correct flag as shown
below 

![GetImage (5)](https://user-images.githubusercontent.com/31175996/114054401-b19d3480-9844-11eb-88a6-c7ad52983766.png)

# Forensics Challenges
## FE01 OST file 
![GetImage (6)](https://user-images.githubusercontent.com/31175996/114055141-56b80d00-9845-11eb-8cbf-879bdd41a295.png)

This is a ost file I tried binwalk –e fe01.ost which did extract emails but a bunch of other zlib files. I tried using –D and –dd to ignore them, but they didn't work. Also couldn't really find any good examples using those options.  

So I found pff-tools run in ubuntu apt-get install pff-tools 

Run pffexport fe01.ost this will extract ost folders and files 

Cd into the folder and open random folders there will be a message folder that holds encrypted zip. I ran grep –r "p/w" and grep –r "password" to find the particular zip file and email message

I was only able to pull up email that has encrypted zip and mentions that they had sent the password earlier 

I tried zip2john but hash was huge so no point in trying to crack it 

I tried searching grep –r "Friday" which pulled up other emails but no password 

I looked through the folders some more and found one that contains calendar invites. Appointment 1 had something that looked like password . I tried it and it worked. 

![GetImage (7)](https://user-images.githubusercontent.com/31175996/114055493-ae567880-9845-11eb-8122-0aaad9bd3866.png)
![GetImage (8)](https://user-images.githubusercontent.com/31175996/114055505-b0b8d280-9845-11eb-965c-b748474e3c58.png)

## FE04 50k-users.txt 
![GetImage (9)](https://user-images.githubusercontent.com/31175996/114055749-e1990780-9845-11eb-87ef-86e97decc997.png)

I used regular expressions with grep I tried the ..x which matches any 2 characters and then x. However this was matching anywhere in the line so I used start anchor ^. Next I used the [] which matches any range, specifically 2-6. I tried doing *Z*S$ and *ZS$ however non worked so I piped it into two other greps. Second to get a Z anywhere in line. Final grep looks for S but matches at the end using $ 

![GetImage (10)](https://user-images.githubusercontent.com/31175996/114055774-e5c52500-9845-11eb-9896-f0efc38a8ab8.png)

## FM03 

It is a vera crypt encrypted volume. I looked at truecrypt2john however it couldn't get the hashes. I also tried pulling the first 512 bytes out since it is a volume using dd but without knowing the encryption algorithm didn't know what to choose in hashcat –m option. 

This can be good practice if anyone wants to try using hashcat to crack this. Problem is we don't know what hash was used so in hashcat under -m option you would, most likely have to choose all the available veracrypt hash types. Of course you now know the right password so you can add it to your wordlist.

Instead I used the top 10k passwords list with veracracker.py Link to veracracker.py https://github.com/NorthernSec/VeraCracker 

It worked as shown below 

![GetImage (11)](https://user-images.githubusercontent.com/31175996/114056375-71d74c80-9846-11eb-8f4b-75c5ca599946.png)
