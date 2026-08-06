# Project Charter

**Project Name:** Port Land Management System (PLMS)

**Document Version:** 1.0 (Baseline Approved)

**Project Owner:** Client Organization (Port Authority)

**Prepared By:** Sujith VS

**Date:** July 2026

---

# 1. Project Overview

The Port Land Management System (PLMS) is an AI-powered enterprise platform designed to assist Port Authority employees and authorized tenants in managing land lease information, organizational documents, and approval workflows.

The system combines Retrieval-Augmented Generation (RAG) with structured database querying (Text-to-SQL) to provide secure, contextual, and source-backed answers from both unstructured documents and structured PostgreSQL databases. In addition to intelligent search, the platform supports document drafting, document analysis, multi-stage approval workflows, audit logging, and role-based access control.

The project aims to modernize existing manual processes by enabling faster information retrieval, improving operational efficiency, and enhancing compliance with organizational policies.

---

# 2. Business Need

Port Authorities maintain a large collection of lease agreements, government policies, legal documents, circulars, maps, and operational records. These documents exist in multiple formats, including PDFs, scanned documents, Word files, images, and text files.

Employees currently spend significant time searching across multiple repositories to locate relevant information required for decision-making, document preparation, policy verification, and lease administration.

Operational data such as tenant information, lease records, billing details, payment history, and contract information are stored separately within structured databases, making it difficult to retrieve both document-based and database-backed information through a single interface.

An intelligent system capable of securely retrieving information from both document repositories and structured databases will significantly improve productivity, reduce manual effort, improve decision-making, and strengthen regulatory compliance.

---

# 3. Project Purpose

The purpose of this project is to design and develop a secure, enterprise-grade AI assistant that enables authorized users to retrieve, analyze, and generate information from organizational knowledge sources while supporting human approval workflows and maintaining complete auditability.

---

# 4. Project Objectives

The project aims to:

* Reduce the average time required to locate information across organizational documents by at least **50%**.
* Enable conversational search across structured and unstructured organizational data through a unified interface.
* Provide source-cited AI-generated responses to improve trust and reduce factual ambiguity.
* Assist employees in drafting official documents, office memorandums, reports, and notices.
* Support secure information retrieval through Role-Based Access Control (RBAC) and tenant-level data isolation.
* Implement a multi-tier approval workflow (`DO → NO → HOD`).
* Maintain complete and tamper-resistant audit records for critical system activities.
* Improve overall operational efficiency and knowledge accessibility.

---

# 5. Expected Deliverables

The project will deliver:

* AI-powered conversational assistant interface.
* Secure authentication and authorization module (RBAC + Tenant Isolation).
* Document ingestion and indexing pipeline.
* OCR processing pipeline for scanned documents and land maps.
* Hybrid document retrieval engine (Vector Search + Full-Text Keyword Search).
* Natural language Text-to-SQL structured database query engine.
* Official document drafting, editing, and diff-analysis engine.
* Multi-stage approval workflow (`DO → NO → HOD` ticket lifecycle).
* Tenant self-service portal with Row-Level Security (RLS).
* Administrative dashboard for system usage and monitoring.
* Audit logging and compliance module.
* Containerized deployment package (Docker / On-Premise artifacts).
* Complete technical documentation, API specifications, and admin guides.

---

# 6. Stakeholders

| Stakeholder | Role | Responsibilities |
| --- | --- | --- |
| Client Organization | Project Sponsor | Project funding, strategic direction, final acceptance |
| Estate Department | Primary Business User | Workflow validation and user acceptance |
| Legal Department | Policy Validation | Verification of legal clauses and compliance |
| Finance Department | Business Data Owner | Billing and lease data verification |
| Information Technology Department | System Administration | Infrastructure, GPU resources, and system maintenance |
| Data Entry Operators (DO) | Operational Users | Document preparation and workflow initiation |
| Nodal Officers (NO) | Review Authority | Review, refinement, and workflow approval |
| Head of Department (HOD) | Final Approval Authority | Final approval and document authorization |
| Tenants | External Users | Access to tenant-specific information and services |

---

# 7. Project Scope

## In Scope

* AI-assisted document retrieval and source citation.
* Conversational knowledge assistant (Text-to-SQL + Vector RAG).
* Structured and unstructured data retrieval.
* OCR processing of scanned documents and maps.
* Document comparison, summarization, and clause extraction.
* Official document drafting and interactive editing.
* Hierarchical approval workflow (`DO → NO → HOD`).
* Role-Based Access Control (RBAC).
* Tenant-level data isolation (Row-Level Security).
* Metadata-based search and filtering.
* Audit logging and activity lineage tracking.
* Administrative reporting dashboard.

## Out of Scope

* Enterprise financial accounting systems.
* Active GIS mapping software and dynamic CAD applications.
* Human resource management.
* Payroll management.
* Physical asset and port machinery maintenance systems.
* Physical document scanning and manual digitizing services.

---

# 8. Success Criteria

The project will be considered successful when it achieves the following measurable outcomes during User Acceptance Testing (UAT):

* **Search Time Reduction:** Reduce average document search time by **50% or more**.
* **Citation Accuracy:** Generate source-cited responses with **greater than 95% citation precision**.
* **Text-to-SQL Accuracy:** Achieve **greater than 90% execution accuracy** for AI-generated SQL queries on validated database schemas.
* **Security & Isolation:** Zero instances of unauthorized cross-tenant information access during security audits.
* **Audit Trail Completeness:** Maintain a 100% complete audit history for all workflow actions and queries.
* **Performance SLAs:** Deliver document chunk retrieval within **3 seconds** and complete AI-assisted responses within **8 seconds** under normal production workloads.
* **User Adoption:** Demonstrate improved user satisfaction and productivity during operational sign-off.

---

# 9. Assumptions

The project assumes that:

* Organizational documents are available in digital format or will be provided in legible scanned formats.
* A centralized **PostgreSQL database with pgvector extension** will serve as the primary engine for relational data and vector storage.
* Local, private AI inference execution (e.g., via Ollama using `Qwen 2.5` family models) will be used to adhere to government data privacy regulations.
* Suitable OCR technology (e.g., PaddleOCR / Tesseract) will be integrated for processing scanned documents.
* The organization will provision the necessary computing infrastructure (including dedicated GPU hardware) for secure on-premise execution.
* Authorized users will authenticate using organizational accounts and existing credentials.

---

# 10. Constraints

The project is subject to the following constraints:

* Strict government data security and privacy regulations prohibiting cloud LLM data transfers.
* Availability and VRAM capacity of GPU hardware resources for local AI inference.
* High variability in the scan quality of historical documents affecting OCR precision.
* Continuous updates to government land lease policies requiring modular system design.
* Integration constraints with legacy enterprise software.
* Adherence to defined project schedules, infrastructure budgets, and resource limits.

---

# 11. Risks and Mitigation Strategies

| Risk | Severity | Mitigation Strategy |
| --- | --- | --- |
| **AI-generated factual inaccuracies** | High | **Human-in-the-Loop (HITL):** Strict workflow requirement that all AI-generated drafts require NO/HOD manual review and authorization before execution. |
| **Unauthorized information access** | Critical | Enforce strict RBAC, database Row-Level Security (RLS), and pre-retrieval identity filtering. |
| **Poor OCR quality on legacy documents** | Medium | Automated image pre-processing (deskew, binarize) and manual operator validation prompts for low-confidence text extracts. |
| **GPU infrastructure limitations** | Medium | Utilize model quantization (4-bit / 8-bit GGUF via Ollama), semantic response caching, and asynchronous job queues. |
| **Regulatory or policy changes** | Medium | Maintain modular policy indexing and dynamic metadata tagging for rapid re-indexing. |

---

# 12. Project Success Statement

The project will be considered successful when authorized users can securely retrieve accurate information from organizational documents and structured databases through a unified conversational interface while maintaining regulatory compliance, complete auditability, and strict role-based access control.

---

# 13. Project Constraints Triangle

The successful delivery of PLMS depends on maintaining an appropriate balance between the following project dimensions:

* **Scope** — Deliver the agreed functional capabilities without uncontrolled expansion.
* **Time** — Complete the project within the approved schedule.
* **Cost** — Utilize organizational infrastructure and resources efficiently.
* **Quality** — Ensure security, reliability, usability, and regulatory compliance are not compromised.

Any significant change to one dimension may require corresponding adjustments to the others.

---

# 14. High-Level Project Phases

```text
Phase 1 : Project Initiation & Chartering                (Weeks 1–2)
Phase 2 : Requirements Gathering & Analysis             (Weeks 3–4)
Phase 3 : System Architecture & DB Design (PostgreSQL)   (Weeks 5–7)
Phase 4 : Core Backend & Ollama LLM Integration          (Weeks 8–10)
Phase 5 : AI Dual RAG Pipeline (pgvector + Text-to-SQL)  (Weeks 11–14)
Phase 6 : Approval Workflow & UI Development            (Weeks 15–18)
Phase 7 : Security Auditing, OCR Tuning & UAT           (Weeks 19–21)
Phase 8 : On-Premise Deployment, Training & Handover     (Weeks 22–23)