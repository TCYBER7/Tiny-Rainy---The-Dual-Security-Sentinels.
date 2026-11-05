# 🌧️ Tiny & Rainy — The Dual Security Sentinels

> **Automated Active Defense & Deception Engine Built in Pure Python**

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Dependencies](https://img.shields.io/badge/dependencies-Zero%20(Pure%20Python)-orange.svg)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)

---

## ⚡ Overview

**Tiny & Rainy** is a lightweight, multi-threaded security framework designed to protect server infrastructure through active deception, honeypots, and real-time IP banishment. 

Built with **zero external dependencies**, it runs straight out of the box on any Linux environment using Python's standard library.

---

## 🛡️ Meet The Sentinels

* 🚪 **Tiny (The Front-Door Shield):** Guards active network ports, captures unauthorized scan attempts, and deploys deceptive honey-portals to confuse attackers.
* 🚪 **Rainy (The Back-Door Guard):** Monitors back-channel activity, directory traps, and triggers automated IP banishment against brute-force attempts.

---

## ✨ Key Features

* 🚀 **Zero-Dependency Engine:** No `pip install` required. Clean, audit-friendly, and lightweight.
* 🔄 **Multi-Threaded Architecture:** Sentinels monitor concurrently in the background without locking your main process.
* 📦 **Dual-Package Bundle:**
  * **Production Script:** Fully integrated for live Linux server environments (with `iptables` active blocking).
  * **Safe Demo Script:** Designed for secure, rootless testing on Windows, macOS, or Android (Termux).

---

## 💻 Quick Start

### 1. Run Safe Demo (Cross-Platform)
```bash
python3 TinyAndRainy_Demo.py
