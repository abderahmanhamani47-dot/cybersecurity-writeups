# Root-Me - TCP / Base64 / zlib

## Challenge

This challenge requires connecting to a TCP server, decoding Base64-encoded data, decompressing it using zlib, and sending the original message back to the server within a limited time.

## Objective

The goal is to recover the original message from a Base64-encoded and zlib-compressed string and automatically send the correct response to the server.

## Concepts Learned

- TCP sockets
- Python socket programming
- Base64 decoding
- zlib decompression
- String manipulation
- Loops and automation
- Error handling
- Time-constrained communication

## Approach

1. Connect to the Root-Me TCP server.
2. Receive the server response.
3. Extract the encoded string from the message.
4. Decode the string using Base64.
5. Decompress the resulting data using zlib.
6. Send the original message back to the server.
7. Repeat the process until the challenge is completed.
8. Detect the final success message and stop the script.

## Tools

- Python
- `socket`
- `base64`
- `zlib`

## Result

The challenge was successfully completed by automating the complete decoding and response process with Python.
