# LocalDrop

`localdrop` is a lightweight tool for **secure and fast data transfer** between devices on the same LAN using the terminal.

---

## 🚀 Features

- 🛡️ Secure messaging
- 🌐 LAN-based fast communication
- 📥 Receive messages using short codes
- 📤 Send messages with auto-generated codes
- 📂 File sharing coming soon!

---

## 📦 Installation

```bash
pip install localdrop
```

---

## ⚙️ Usage

### 1. Initialize the sender server:

```bash
python -m localdrop init
```

This command starts the sender server on your device.

---

### 2. Send a message:

```bash
python -m localdrop send "Hello world!"
```

You will receive a **4-character code**. Example:

```
Your Code is : 7G4K
```

---

### 3. Receive the message from another device:

Any user on the same LAN can run:

```bash
python -m localdrop get 7G4K
```

And the message will be displayed:

```
Hello world!
```

---

## 4. For close the sender server:
```bash
python -m localdrop stop
```

---

## 📁 File Sharing (Coming Soon)

Currently, only text messages are supported. File sharing will be added in an upcoming update.

---

## 🤝 Contribute

Report issues, suggest features, or contribute on GitHub!
