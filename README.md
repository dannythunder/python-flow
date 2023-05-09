# python-flow

This python library enables for you to develop methods for Flow on your own computer / environment.

## Requirements <br>

### Install on Mac (using brew)
```brew install python3``` <br>

### Install on Linux (Debian)
```sudo apt install python3 -y```

### Install on Windows
[Python3 for Windows](https://www.python.org/downloads/windows/)

### Other OS:es and/or ways
[Python3 download](https://www.python.org/downloads/)

## Installation of the library
```pip3 install git+https://github.com/natgruppen/python-flow.git```

## Environment variables
.env file with

### Required
```FLOW_AUTHORIZATION=Basic {{FLOW_API_TOKEN}}``` <br> Your http api token
```FLOW_URL=https://flow.kurbit.se``` <br> Base url to Flow, no trailing /

### Optional
```FLOW_SECURE_REQUEST=True / False``` Allows for making request to unsecure ssl servers (i.e test servers might be using self signed cert)

## Need to know
When developing outside Flow, you have to use httpOpen instead of rpcOpen (same goes for all of the method types). <br>
So when you post your finished code back to Flow, you have to replace all http*** to rpc***.

## Usage
Se script in [Example files](Examples/)
