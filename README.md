Cyber Threat Data Integration Platform (CTIP)
Overview
The Cyber Threat Data Integration Platform (CTIP) is a distributed, event-driven cybersecurity backend platform designed to ingest, normalize, enrich, correlate, automate, and analyze security telemetry from multiple enterprise sources such as:

Endpoint Detection & Response (EDR)
Cloud Security Platforms
CI/CD Security Pipelines
The platform demonstrates modern backend engineering concepts including:
Microservices architecture
Event-driven processing with Kafka
Threat normalization pipelines
Security analytics
Distributed system resiliency
Docker-based orchestration
CI/CD with GitHub Actions
This project is designed to align with real-world cybersecurity engineering and platform integration roles.
Architecture
                         ┌──────────────────────┐
                         │  EDR / Cloud / CICD │
                         │      Security Logs   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                      ┌──────────────────────────┐
                      │   Ingestion Service      │
                      │   FastAPI + Kafka Prod   │
                      └──────────┬───────────────┘
                                 │
                                 ▼
                     Kafka Topic: raw-security-events
                                 │
                                 ▼
                      ┌──────────────────────────┐
                      │ Normalization Service    │
                      │ Kafka Consumer           │
                      └──────────┬───────────────┘
                                 │
                                 ▼
                      ┌──────────────────────────┐
                      │ Enrichment Service       │
                      └──────────┬───────────────┘
                                 │
                                 ▼
                      ┌──────────────────────────┐
                      │ Automation Service       │
                      └──────────┬───────────────┘
                                 │
                                 ▼
                      ┌──────────────────────────┐
                      │ Correlation Service      │
                      └──────────┬───────────────┘
                                 │
                                 ▼
                      ┌──────────────────────────┐
                      │ Analytics Service        │
                      │ PostgreSQL Reporting     │
                      └──────────────────────────┘
Features
Security Data Integration
EDR log ingestion
Cloud security event ingestion
CI/CD security finding ingestion
Threat Data Processing
Threat normalization
Severity mapping
Asset standardization
Event deduplication
Event fingerprinting using SHA-256 hashes
Event Streaming
Kafka producer/consumer architecture
Asynchronous event processing
Event-driven microservices
Security Automation
Automated remediation workflow generation
Critical severity event handling
Threat Correlation
Multi-event attack correlation
Risk aggregation logic
Analytics
PostgreSQL-based reporting
Threat statistics APIs
Risk summary generation
DevOps
Dockerized services
Multi-container orchestration
GitHub Actions CI pipeline
Technology Stack
Category	Technology
Language	Python 3.11
Backend Framework	FastAPI
Event Streaming	Apache Kafka
Databases	MongoDB, PostgreSQL
Containerization	Docker
Orchestration	Docker Compose
CI/CD	GitHub Actions
Messaging	Kafka Producer/Consumer
API Docs	Swagger/OpenAPI
Project Structure
CyberThreatDataIntegrationPlatform/
│
├── ingestion-service/
├── normalization-service/
├── enrichment-service/
├── automation-service/
├── correlation-service/
├── analytics-service/
│
├── docker-compose.yml
├── .gitignore
├── README.md
│
└── .github/
    └── workflows/
        └── ci.yml
Microservices
1. Ingestion Service
Responsibilities
Accept raw security logs
Store raw events in MongoDB
Publish events to Kafka
Port
8001
Example Sources
CrowdStrike
SentinelOne
AWS Security Hub
GitHub Actions Security
2. Normalization Service
Responsibilities
Consume Kafka events
Normalize heterogeneous security schemas
Deduplicate events
Generate event fingerprints
Port
8002
Example Normalized Fields
{
  "source": "edr",
  "asset": "finance-server-01",
  "event_type": "ransomware",
  "severity": "critical"
}
3. Enrichment Service
Responsibilities
Add contextual intelligence
Add enrichment metadata
Simulate threat intelligence enrichment
Port
8003
4. Automation Service
Responsibilities
Generate remediation workflows
Trigger automated response recommendations
Port
8004
5. Correlation Service
Responsibilities
Correlate multi-source events
Identify attack patterns
Aggregate threat indicators
Port
8005
6. Analytics Service
Responsibilities
Store analytical summaries
Provide reporting APIs
Generate risk dashboards data
Port
8006
Kafka Streaming Flow
Raw Security Event
        ↓
Ingestion Service
        ↓
Kafka Topic
(raw-security-events)
        ↓
Normalization Consumer
        ↓
Normalized Security Events
Setup Instructions
Prerequisites
Install the following:
Python 3.11+
Docker
Docker Compose
Git
Postman or curl
Clone Repository
git clone <YOUR_GITHUB_REPO_URL>

cd CyberThreatDataIntegrationPlatform
Start Platform
docker-compose up --build
This starts:
MongoDB
PostgreSQL
Zookeeper
Kafka
All FastAPI microservices
Verify Running Containers
docker ps
Expected services:
ingestion-service
normalization-service
enrichment-service
automation-service
correlation-service
analytics-service
kafka
zookeeper
ctip-mongo
ctip-postgres
API Documentation
Service	URL
Ingestion	http://localhost:8001/docs
Normalization	http://localhost:8002/docs
Enrichment	http://localhost:8003/docs
Automation	http://localhost:8004/docs
Correlation	http://localhost:8005/docs
Analytics	http://localhost:8006/docs
Example Workflow
1. Ingest Security Event
Endpoint
POST http://localhost:8001/ingest
Payload
{
  "source": "edr",
  "payload": {
    "host": "finance-server-01",
    "ip": "10.10.1.25",
    "threat": "ransomware",
    "severity": "critical",
    "detected_by": "CrowdStrike"
  }
}
Response
{
  "status": "success",
  "message": "edr log ingested and streamed to Kafka"
}
2. Verify Automatic Normalization
Endpoint
GET http://localhost:8002/normalize/normalized
Example Response
{
  "count": 1,
  "data": [
    {
      "source": "edr",
      "asset": "finance-server-01",
      "event_type": "ransomware",
      "severity": "critical",
      "event_hash": "6fadf16935bd025f..."
    }
  ]
}
Example Security Sources
EDR Example
{
  "source": "edr",
  "payload": {
    "host": "prod-db-01",
    "ip": "10.1.1.10",
    "threat": "ransomware",
    "severity": "critical",
    "detected_by": "CrowdStrike"
  }
}
Cloud Example
{
  "source": "cloud",
  "payload": {
    "instance_id": "aws-prod-app-01",
    "event_type": "unauthorized_access",
    "severity_level": 9,
    "region": "ap-south-1"
  }
}
CI/CD Example
{
  "source": "cicd",
  "payload": {
    "pipeline": "release-prod",
    "issue": "dependency_vulnerability",
    "priority": "critical",
    "repository": "auth-service",
    "branch": "release-v2"
  }
}
Event Deduplication
The platform generates SHA-256 fingerprints for events.
This enables:
duplicate detection
idempotent processing
consistent event identity
Example:
{
  "event_hash": "97fb7aaed8d44f426aa221bae4c57430..."
}
CI/CD Pipeline
GitHub Actions automatically:
Builds Docker containers
Starts services
Verifies APIs
Validates microservice availability
Workflow file:
.github/workflows/ci.yml
Running GitHub Actions
Push code to GitHub:
git add .

git commit -m "Initial CTIP platform"

git push origin main
Then monitor:
GitHub → Actions
Key Engineering Concepts Demonstrated
Backend Engineering
FastAPI microservices
REST APIs
distributed services
Cybersecurity Engineering
threat ingestion
exposure management
threat analytics
event correlation
Distributed Systems
Kafka streaming
producer/consumer architecture
async processing
retry handling
Data Engineering
schema normalization
enrichment pipelines
event fingerprinting
DevOps
Docker
container orchestration
GitHub Actions CI/CD
Future Enhancements
Potential improvements:
Kafka chaining between all services
Redis caching
Kubernetes deployment
Grafana dashboards
Prometheus monitoring
Real threat intelligence feeds
Role-based authentication
WebSocket streaming
SIEM integrations
Learning Outcomes
This project demonstrates practical experience with:
cybersecurity platform engineering
scalable backend systems
distributed event processing
security data normalization
enterprise integration patterns
containerized microservices

Developed as a hands-on cybersecurity engineering and distributed systems learning project using Python, FastAPI, Kafka, MongoDB, PostgreSQL, Docker, and GitHub Actions.