# IP Manager

[![en](https://img.shields.io/badge/lang-en-red.svg)](/README.md) [![fr](https://img.shields.io/badge/lang-fr-blue.svg)](/README.fr.md)

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](/LICENSE)
[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Repo Size](https://img.shields.io/github/repo-size/thamnis/ip_manager)](https://github.com/thamnis/ip_manager)
[![Issues](https://img.shields.io/github/issues/thamnis/ip_manager)](https://github.com/thamnis/ip_manager/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/thamnis/ip_manager)](https://github.com/thamnis/ip_manager/pulls)
[![Contributors](https://img.shields.io/github/contributors/thamnis/ip_manager)](https://github.com/thamnis/ip_manager/graphs/contributors)
[![Last Commit](https://img.shields.io/github/last-commit/thamnis/ip_manager)](https://github.com/thamnis/ip_manager/commits/main)

## 📌 Overview

**IP Manager** is a Python library that provides advanced operations on IP addresses:

- ✅ **Validation of IP addresses and CIDR**.
- 🔄 **Conversion between binary and decimal notation**.
- 🛠 **Subnet mask calculation**.
- 📍 **Network address range determination**.
- 🚀 **Network optimization for a given number of hosts**.

## 🚀 Installation

Make sure you have **Python 3.x** installed on your machine, then clone the repository:

```bash
git clone https://github.com/thamnis/ip_manager.git
cd ip_manager
```

## 📖 Usage

Example usage of the Ip class:

``` Python
from ip_manager import Ip

# Creating an instance with an IP address

ip_instance = Ip("192.168.1.0/24")

print(f"IP Address: {ip_instance.ip}")
print(f"CIDR: {ip_instance.cidr}")
print(f"Decimal Mask: {ip_instance.mask_dec}")
print(f"Address Range: {ip_instance.ip_range}")
```

Run an example:

``` Bash
python main.py
```

## 🌍 Network Optimization

If you want to optimize your network for a given number of hosts:

``` Python
optimized_network = ip_instance.optimize_network(50)
print(optimized_network)
```

## 🛠 Dependencies

No external dependencies are required. The script works with Python's standard modules.

## 🧪 Unit Tests

A test file [test.py](/test.py) is available to validate the functionalities.

### 🔹 Running tests

``` Bash
python -m unittest test.py
```

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for more details.

## ✨ Author

Developed by [@thamnis](https://www.github.com/thamnis).
