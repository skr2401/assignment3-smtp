import socket

from socket import *


def smtp_client(port=1025, mailServer='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    mailServer = ('127.0.0.1', 1025)
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    #smtp = gmail.com(127.0.0.1) and port=1025
        clientSocket.connect(mailServer)
    # mailserver = ('127.0.0.1', 1025)
    #clientSocket.connect((mailserver))
    # Fill in end

        recv = clientSocket.recv(1024)
        recv = recv.decode()
    #print
    print("Message after connection request:" + recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024)
    recv1 = recv1.decode()
    #print
    print("Message after Helo command:" + recv1) 
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFrom = "Mail From:<sender@gmail.com>\r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print
    print("After MAIL From command: " + recv2)
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptTo = "RCPT To: <recipient@example.com>\r\n"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print
    print("After RCPT To command: " + recv3)
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data = "Data\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print
    print("After data command: " + recv4)
    # Fill in end

    # Send message data.
    # Fill in start

    date = date + "\r\n\r\n"
    clientSocket.send(date.encode())
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024)
    #print
    print("Response after sending message body: " + recv5.decode())
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = "QUIT\r\n"
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024)
    #print
    print(recv6.decode())
    # Fill in end

    # Close the socket ********
    clientSocket.close() #*****
    # *************************


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')