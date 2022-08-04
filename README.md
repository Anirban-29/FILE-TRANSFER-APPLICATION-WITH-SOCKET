# FILE-TRANSFER-APPLICATION-WITH-SOCKET
THIS IS A PROJECT WORKING WITH SOCKET FOR SECURE FILE TRANSFER
FILE TRANSFER APPLICATION USING SOCKET PROGRAMMING IN PYTHON
The objective of this project is to create a system to facilitate duplex communication between all the nodes in a small Local Area Network (LAN) using Socket Programming. To establish the communication between the client and server, we make use of TCP protocol using socket programming in Python.



TCP is a standard protocol which defines how to establish and maintain a network connection via which application programs can exchange data. TCP works with the Internet Protocol (IP), which defines how computers send packets of data to each other. TCP is a connection-oriented protocol, which means a connection is established and maintained until the application programs at each end have finished exchanging messages. It determines how to break application data into packets that networks can deliver, send packets to and accept the packets from the network layer, manages flow control and because it is meant to provide error-free data transmission handles retransmission of dropped or garbled packet as well as acknowledgment of all the packets which arrive.


HOW TO RUN

It is a simple to use gui.The sender and receiver both have to run the FILETRANSFER.py file.The sender has to click on the SEND button and using the BROWSE button select the file he or she wants to send if the upload was successful a message will show "LOADING COMPLETED" if not an error will display ,then as soon as the send button is pressed the application will wait for incoming connections.
The receiver has to click on the receive button and enter the required fields like the sender's id(ip address) and the file name with which the file will be saved rememeber to mention the proper extension in case of mis-match of the extension the file may get corrupted.And after filling the required details they need to only press the receive button.A message will be displayed when the file transfer is completed in the both receiver and sender end.Using this application anyone can send a file upto 2gb size of any extension.
