# Cloud Computing Notes

## On-Premise vs Cloud Computing

### On-Premise Infrastructure

On-premise (on-prem) means an organisation owns and manages its own physical servers, networking equipment, storage devices, and data centres.

### Disadvantages

- High upfront costs (Capital Expenditure - CAPEX)
- Difficult and expensive to scale
- Hardware maintenance is the organisation's responsibility
- Requires physical space
- Requires dedicated IT staff
- Slower deployment of new services
- Hardware eventually becomes obsolete

### Example

A company purchases and maintains its own servers in an office server room.

---

## What is Cloud Computing?

Cloud computing is the delivery of computing services over the internet on-demand.

Instead of purchasing and maintaining physical hardware, businesses rent computing resources from cloud providers when needed.

### Simple Diagram

```text
Data Centre
     │
     ▼
 Internet
     │
     ▼
 User Device
```

### Benefits

- Pay only for what you use (Pay-As-You-Go)
- Scale resources instantly
- Global availability
- Reduced hardware costs
- Faster deployment
- High reliability

### Cloud Provider Responsibilities

The cloud provider owns and manages:

- Physical servers
- Networking equipment
- Storage devices
- Physical security
- Cooling and power systems
- Data centre maintenance

Examples of cloud providers:

- Amazon Web Services (AWS)
- Microsoft Azure
- Google Cloud Platform (GCP)

---

# Cloud Services

Many services we use daily are cloud services:

- Microsoft 365 (Word, Excel, Outlook)
- Google Drive
- Dropbox
- GitHub
- Netflix
- Spotify
- Salesforce

Data is stored remotely and accessed via the internet.

---

# Cloud Deployment Models

## Public Cloud (Multi-Tenant)

Resources are owned and operated by a third-party cloud provider.

Multiple customers share the same underlying infrastructure.

### Advantages

- Lower costs
- Highly scalable
- Easy to deploy

### Examples

- AWS
- Azure
- Google Cloud

Most businesses use public cloud services.

---

## Private Cloud (Single-Tenant)

Infrastructure is dedicated to a single organisation.

Can be hosted internally or by a third-party provider.

### Advantages

- Greater control
- Increased security
- Easier compliance

### Disadvantages

- More expensive
- Requires specialist management

### Examples

- Government departments
- Banks
- Healthcare organisations

---

## Hybrid Cloud

Combines public and private cloud environments.

Sensitive workloads remain private while less critical services use the public cloud.

### Advantages

- Flexibility
- Better security
- Cost savings

### Disadvantages

- Increased complexity
- More difficult management

### Example

The NHS may keep patient records in private infrastructure while using public cloud services for websites or analytics.

---

## Multi-Cloud

Uses services from multiple cloud providers.

### Example

```text
AWS <--> Azure <--> GCP <--> Private Cloud
```

### Advantages

- Avoids vendor lock-in
- Improves resilience
- Allows organisations to use the best service from each provider

### Disadvantages

- Higher complexity
- Increased management overhead
- Requires specialised expertise

Common in large enterprises and financial organisations.

---

# Cloud Service Types

## Infrastructure as a Service (IaaS)

Provides virtualised computing infrastructure over the internet.

The customer manages:

- Operating systems
- Applications
- Data

The provider manages:

- Hardware
- Networking
- Storage

### Examples

- AWS EC2
- Azure Virtual Machines
- Google Compute Engine

### Characteristics

- Most flexibility
- Most responsibility
- Closest to traditional servers

---

## Platform as a Service (PaaS)

Provides a managed environment for developing and deploying applications.

The provider manages:

- Hardware
- Operating systems
- Runtime environments

The customer focuses on:

- Application code
- Business logic

### Examples

- Heroku
- Azure App Service
- Google App Engine

### Benefits

- Faster development
- Less infrastructure management

---

## Software as a Service (SaaS)

Complete software solutions delivered through a browser or application.

### Examples

- Microsoft 365
- Gmail
- Salesforce
- Dropbox

### Characteristics

- Least control
- Least responsibility
- Ready to use immediately

---

## Function as a Service (FaaS)

Also known as **Serverless Computing**.

Code executes only when triggered by an event.

### Examples

- AWS Lambda
- Azure Functions
- Google Cloud Functions

### Common Triggers

- File upload
- HTTP request
- Database change
- Scheduled task

### Benefits

- No server management
- Highly scalable
- Pay only when code executes

---

# Advantages of Cloud Computing

## Cost Savings

Converts:

```text
CAPEX → OPEX
```

Instead of purchasing hardware, organisations pay monthly or based on usage.

---

## Scalability

Resources can increase or decrease automatically based on demand.

Example:

A retailer can scale during Black Friday traffic spikes.

---

## Accessibility

Services can be accessed from anywhere with an internet connection.

---

## Security

Major cloud providers invest billions into:

- Encryption
- Monitoring
- Physical security
- Compliance certifications

---

## Automatic Updates

Providers maintain and update infrastructure automatically.

---

## Global Reach

Applications can be deployed worldwide in minutes.

---

## Faster Innovation

Development teams can quickly:

- Create environments
- Test applications
- Deploy products

without purchasing hardware.

---

# Potential Pitfalls

## Cost Management

Poorly managed cloud resources can lead to unexpected costs.

Many organisations employ Cloud Cost Analysts or FinOps teams.

---

## Internet Dependency

No internet connection means no access to cloud resources.

---

## Security Risks

Misconfigured services can expose sensitive data.

---

## Vendor Lock-In

Moving between cloud providers can be difficult and expensive.

---

## Compliance Requirements

Organisations must comply with:

- GDPR
- ISO 27001
- Industry regulations

---

## Service Outages

Cloud providers occasionally experience outages that may affect customers globally.

---

# The Big Three Cloud Providers

## AWS (Amazon Web Services)

Market leader and largest cloud provider.

### Known For

- Reliability
- Large service catalogue
- Extensive documentation
- Mature ecosystem

### Popular Services

- EC2
- S3
- RDS
- Lambda

---

## Microsoft Azure

Strong integration with Microsoft products.

### Known For

- Active Directory integration
- Microsoft 365 ecosystem
- Enterprise environments
- Azure DevOps

### Popular Services

- Azure Virtual Machines
- Azure SQL Database
- Azure Functions

---

## Google Cloud Platform (GCP)

Strong focus on data and AI.

### Known For

- Machine Learning
- Analytics
- Big Data
- Ease of use

### Popular Services

- BigQuery
- Vertex AI
- Cloud Run

---

# Data Centres

A data centre is a facility containing servers, networking equipment, storage systems, power supplies and cooling systems.

Cloud providers operate data centres around the world.

### AWS Availability Zones

Example:

```text
Ireland Region
 ├─ AZ1
 ├─ AZ2
 └─ AZ3
```

Availability Zones provide redundancy and fault tolerance.

If one zone fails, services can continue running in another.

---

# SSH Key Pairs

SSH (Secure Shell) key pairs provide secure authentication.

## Components

### Public Key

- Shared with the server
- Like a padlock

### Private Key

- Kept secret
- Like the key that unlocks the padlock

## Benefits

- More secure than passwords
- Supports encrypted communication
- Widely used for cloud servers

### Naming Convention Example

```text
charlie-prod-key.pem
charlie-dev-key.pem
```

Always use clear and meaningful names.

---

# Virtual Machines (VMs)

A Virtual Machine is a software-based computer running on a physical server.

### Example

Physical Server:

```text
32 CPU
128 GB RAM
```

Virtual Machines:

```text
VM1 = 2 CPU / 2 GB RAM
VM2 = 4 CPU / 8 GB RAM
VM3 = 8 CPU / 16 GB RAM
```

The physical machine is called the **Host**.

The virtual machines are called **Guests**.

---

# EC2 (Elastic Compute Cloud)

EC2 is AWS's Infrastructure as a Service offering.

Allows users to launch virtual machines in the cloud.

### Features

- Multiple operating systems
- Scalable resources
- Secure networking
- Pay-as-you-go pricing

### Example Instance Type

```text
t3.micro
```

A small, low-cost VM suitable for learning and testing.

---

# Common Linux Commands

Update package lists:

```bash
sudo apt update -y
```

Upgrade installed packages:

```bash
sudo apt upgrade -y
```

> ⚠️ Upgrades can be disruptive on production systems.

Install NGINX:

```bash
sudo apt install nginx -y
```

Check service status:

```bash
sudo systemctl status nginx
```

Exit status screen:

```text
q
```