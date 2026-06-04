# MongoDB Setup on AWS EC2 (Ubuntu 24.04)

## Overview

This guide covers installing MongoDB 8.0 on an AWS EC2 Ubuntu instance, configuring remote access, and connecting using MongoDB Compass.

---

# 1. Update the Server

Refresh package information and install required tools.

```bash
sudo apt update
sudo apt install gnupg curl -y
```

**Purpose**

- Updates Ubuntu package lists.
- Installs tools required to download and verify MongoDB packages.

---

# 2. Add MongoDB GPG Key

Download MongoDB's official signing key.

```bash
curl -fsSL https://pgp.mongodb.com/server-8.0.asc | \
sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg \
--dearmor
```

**Purpose**

Ubuntu uses this key to verify that MongoDB packages come from a trusted source.

---

# 3. Add the MongoDB Repository

Add the MongoDB 8.0 repository for Ubuntu 24.04 (Noble).

```bash
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list
```

**Purpose**

Allows Ubuntu to download MongoDB packages directly from MongoDB's official repository.

---

# 4. Install MongoDB

Update package information and install MongoDB.

```bash
sudo apt update
sudo apt install -y mongodb-org
```

**Purpose**

Installs:

- MongoDB Server
- MongoDB Shell (`mongosh`)
- MongoDB Database Tools

---

# 5. Start MongoDB

Start the MongoDB service.

```bash
sudo systemctl start mongod
```

**Purpose**

Launches the MongoDB database server.

---

# 6. Enable MongoDB on Startup

```bash
sudo systemctl enable mongod
```

**Purpose**

Ensures MongoDB automatically starts whenever the EC2 instance reboots.

---

# 7. Verify MongoDB Status

Check that MongoDB is running.

```bash
sudo systemctl status mongod
```

Expected output:

```text
Active: active (running)
```

Press:

```text
q
```

to exit the status screen.

---

# 8. Verify MongoDB Functionality

Open the MongoDB shell.

```bash
mongosh
```

Show available databases:

```javascript
show dbs
```

Create a test database:

```javascript
use testdb
```

Insert a document:

```javascript
db.users.insertOne({
  name: "Charlie",
  role: "Data Engineer"
})
```

Verify the document exists:

```javascript
db.users.find()
```

Exit MongoDB Shell:

```javascript
exit
```

---

# 9. Useful Service Commands

Stop MongoDB:

```bash
sudo systemctl stop mongod
```

Restart MongoDB:

```bash
sudo systemctl restart mongod
```

Check Status:

```bash
sudo systemctl status mongod
```

---

# 10. Configure Remote Access

Open the MongoDB configuration file.

```bash
sudo nano /etc/mongod.conf
```

Locate:

```yaml
bindIp: 127.0.0.1
```

Change to:

```yaml
bindIp: 0.0.0.0
```

**Purpose**

- `127.0.0.1` only accepts connections from the EC2 instance itself.
- `0.0.0.0` allows remote connections from MongoDB Compass.

Save the file:

```text
Ctrl + O
Enter
Ctrl + X
```

Restart MongoDB:

```bash
sudo systemctl restart mongod
```

---

# 11. Configure AWS Security Group

Navigate to:

```text
EC2 → Security Groups → Inbound Rules
```

Add the following rule:

```text
Type: Custom TCP
Port Range: 27017
Source: My IP
```

Example existing rules:

```text
SSH          22
HTTP         80
MongoDB      27017
```

**Purpose**

Allows MongoDB Compass to connect to the EC2 MongoDB instance.

---

# 12. Connect Using MongoDB Compass

Open MongoDB Compass.

Create a new connection using:

```text
mongodb://<EC2-PUBLIC-IP>:27017
```

Example:

```text
mongodb://<YOUR-EC2-PUBLIC-IP>:27017
```

Click:

```text
Save & Connect
```

---

# 13. Verify Successful Connection

Successful connection should display the default MongoDB databases:

```text
admin
config
local
```

You can now:

- Create databases
- Create collections
- Insert documents
- Import JSON files
- Manage MongoDB remotely through Compass

---

# Architecture Overview

```text
MongoDB Compass (Mac)
            │
            ▼
AWS Security Group (Port 27017)
            │
            ▼
EC2 Ubuntu Instance
            │
            ▼
MongoDB Server (mongod)
```

This setup allows MongoDB Compass to connect securely to MongoDB running on AWS EC2.