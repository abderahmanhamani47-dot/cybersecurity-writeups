# Root-Me - TCP / Base64 / zlib

## Challenge

This challenge requires connecting to a TCP server and processing messages that are encoded with Base64 and compressed using zlib. The objective is to recover the original message and send it back to the server within a limited time.

## Objective

Automate the entire process using Python by:

1. Connecting to the TCP server.
2. Receiving the encoded message.
3. Decoding the Base64 data.
4. Decompressing the zlib-compressed content.
5. Sending the original message back to the server.
6. Repeating the process until the challenge is completed.

## Concepts Learned

- TCP sockets
- Network communication
- Python socket programming
- Base64 decoding
- zlib decompression
- Automation
- String manipulation
- Error handling

## Technologies Used

- Python 3
- socket
- base64
- zlib

## Python Libraries

### socket
Used to establish a TCP connection and communicate with the remote server.

### base64
Used to decode Base64-encoded data received from the server.

### zlib
Used to decompress the decoded data and recover the original message.


## Workflow

```text
TCP Server
    |
    v
Receive encoded data
    |
    v
Base64 decode
    |
    v
zlib decompress
    |
    v
Recover original message
    |
    v
Send response
    |
    v
Repeat until challenge completion
