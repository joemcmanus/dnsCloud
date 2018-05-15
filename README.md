# dnsCloud
Program to create word clouds of DNS traffic. 

# Install
You will need to install some prereqs. 

 - pip3 install wordcloud
 - pip3 install matplotlib
 - pip3 install pcapy 
 - pip3 install scapy
 
# Use
First you will want to create a list of DNS lookups. To do that run sniff.py INTERFACE OUTFILE 

    dnsCloud joe$ ./pysniff.py  --help 
    usage: pysniff.py [-h] [--pid] interface outfile
    
    DNS Word Cloud Image Generation
    
    positional arguments:
      interface   Network Interface
      outfile     DNS log file
    
    optional arguments:
      -h, --help  show this help message and exit
      --pid       Create a pid file in /var/run/pysniff.pid

To listen on en0 and create a file with DNS lookups called dnslookups.txt run: 

    dnsCloud joe$ sudo ./sniff.py en0 dnslookups.txt

You can then create a word cloud using cloud.py INFILE OUTFILE  .

    dnsCloud joe$ ./cloud.py -h
    usage: cloud.py [-h] [--bgimage BGIMAGE] infile outfile
    
    DNS Word Cloud Image Generation
    
    positional arguments:
      infile             Source file
      outfile            Destination image file
    
    optional arguments:
      -h, --help         show this help message and exit
      --bgimage BGIMAGE  Optional image filei to shape around

To create a wordcloud using the file dnslookups.txt and an image dnslookups.png run: 

    dnsCloud joe$ ./cloud.py dnslookups.txt dnslookups.png
    Source file: dnslookups.txt
    Output file: dnslookups.png

![](https://raw.githubusercontent.com/joemcmanus/dnsCloud/master/wordcloud.png)

