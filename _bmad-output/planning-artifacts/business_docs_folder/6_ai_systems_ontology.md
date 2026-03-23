# AI Systems Ontology
## Draft v1

Version: Draft v1  
Date: March 2026

---

# 1. Purpose

The ontology defines the core knowledge structure of the AI Systems Platform.

Its purpose is to organize:

- AI systems
- tools
- techniques
- domains
- use cases
- people
- evidence

This ontology supports:

- system documentation
- curriculum design
- expert knowledge capture
- discovery and recommendation
- knowledge graph development

---

# 2. Design Principles

### 2.1 Systems First

The ontology is centered on **AI systems**, not individual tools.

Tools change quickly.  
Systems are more durable.

---

### 2.2 Applied Knowledge First

The ontology prioritizes knowledge that is useful for real work.

The goal is not abstract theory, but practical system design.

---

### 2.3 Multi-Layer Structure

Knowledge should be separated into different layers:

- stable concepts
- dynamic evidence
- relationships

This allows the system to evolve without constantly rewriting the core model.

---

### 2.4 Human + Machine Readable

The ontology should be understandable to:

- operators
- AI Champions
- learners
- software systems

It should support both documents and databases.

---

# 3. Core Entity Types

The ontology contains several core entity types.

---

## 3.1 AI System

The central unit of knowledge.

Definition:

A structured applied AI solution that solves a real problem through one or more coordinated components.

Examples:

- research synthesis system
- marketing content generation system
- lead qualification agent system
- internal knowledge assistant

Key properties:

- name
- description
- problem solved
- system type
- complexity level
- domain
- architecture summary
- author
- maturity level

---

## 3.2 Component

A sub-part of an AI system.

Definition:

A functional building block inside a larger AI system.

Examples:

- retrieval module
- summarization module
- planner agent
- evaluation step
- MCP connector
- memory layer

Key properties:

- name
- description
- role
- input
- output

---

## 3.3 Tool

A software product, API, model, framework, or integration used within a system.

Examples:

- ChatGPT
- Claude
- n8n
- Zapier
- Notion
- Google Sheets
- Python
- MCP server

Key properties:

- name
- category
- vendor
- capabilities
- limitations

---

## 3.4 Technique

A reusable method or design pattern used inside AI systems.

Examples:

- prompt chaining
- retrieval-augmented generation
- tool use
- self-reflection
- structured output
- routing
- evaluation loop

Key properties:

- name
- description
- prerequisites
- typical use case
- limitations

---

## 3.5 Workflow Pattern

A recurring structure for how work progresses through an AI system.

Examples:

- collect → summarize → synthesize
- classify → route → respond
- retrieve → reason → draft
- observe → plan → act → evaluate

Key properties:

- name
- sequence structure
- typical use cases

---

## 3.6 Domain

The professional or industry context in which the system is applied.

Examples:

- research
- marketing
- consulting
- legal
- operations
- education
- product management

Key properties:

- name
- description
- typical tasks
- common constraints

---

## 3.7 Use Case

A specific job-to-be-done that an AI system supports.

Examples:

- generate weekly market intelligence report
- summarize meeting notes into action items
- draft social media content
- qualify inbound leads
- map research papers into categories

Key properties:

- description
- target user
- frequency
- desired output

---

## 3.8 Role

A human role inside the ecosystem.

Examples:

- Member
- AI Power User
- AI Champion
- Operator
- Founder

Key properties:

- responsibilities
- capabilities
- contribution type

---

## 3.9 Knowledge Asset

A consumable knowledge object derived from systems and expert insight.

Examples:

- guide
- lecture
- workshop
- case study
- architecture breakdown
- system walkthrough

Key properties:

- type
- source
- audience
- related system

---

## 3.10 Evidence

A concrete piece of support showing that something works or matters.

Examples:

- real-world case study
- benchmark result
- workflow screenshot
- user feedback
- implementation result
- before/after comparison

Key properties:

- source
- date
- credibility
- summary

---

# 4. Relationship Types

The ontology is powered by relationships between entities.

---

## 4.1 AI System Relationships

AI System  
- uses → Tool  
- applies → Technique  
- follows → Workflow Pattern  
- solves → Use Case  
- belongs to → Domain  
- contains → Component  
- created by → Role / Champion  
- documented as → Knowledge Asset  
- supported by → Evidence  
- related to → AI System

---

## 4.2 Technique Relationships

Technique  
- used in → AI System  
- requires → Technique  
- alternative to → Technique  
- suitable for → Use Case

---

## 4.3 Tool Relationships

Tool  
- enables → Component  
- used in → AI System  
- commonly paired with → Tool  
- limited by → Constraint

---

## 4.4 Domain Relationships

Domain  
- contains → Use Case  
- commonly uses → AI System  
- constrained by → Constraint

---

## 4.5 Knowledge Asset Relationships

Knowledge Asset  
- explains → AI System  
- derived from → Champion Insight  
- targeted at → Role  
- supported by → Evidence

---

# 5. Knowledge Layers

The ontology should be implemented as three conceptual layers.

---

## 5.1 Concept Layer

Stable concepts that do not change often.

Includes:

- AI System
- Tool
- Technique
- Domain
- Use Case
- Role
- Component

This is the structural backbone.

---

## 5.2 Evidence Layer

Dynamic evidence that changes over time.

Includes:

- case studies
- benchmarks
- examples
- screenshots
- field notes
- user outcomes

This layer allows freshness.

---

## 5.3 Relationship Layer

The semantic connections between concepts and evidence.

Examples:

- system uses tool
- technique supports use case
- evidence validates system

This layer powers search and recommendation.

---

# 6. Canonical AI System Representation

Each AI System should map into the ontology using a standard structure.

Minimum required fields:

- system name
- short description
- problem solved
- domain
- use case
- tools used
- techniques applied
- workflow pattern
- components
- complexity level
- evidence
- related knowledge assets

This creates consistency across the platform.

---

# 7. Example Ontology Instance

Example:

AI System  
Research Synthesis System

solves → weekly research summarization  
belongs to → research  
uses → Claude  
uses → Notion  
applies → summarization  
applies → structured extraction  
follows → collect → summarize → synthesize  
contains → source collection module  
contains → synthesis module  
documented as → workshop guide  
supported by → case study from consulting workflow

---

# 8. Curriculum Mapping

The ontology should also support education design.

Example curriculum path:

Tools  
↓  
Techniques  
↓  
Patterns  
↓  
AI Systems  
↓  
Domain Applications

This allows the platform to design structured learning paths.

---

# 9. Discovery and Recommendation

The ontology should support discovery features such as:

- systems by domain
- systems by complexity
- systems by tool
- systems by technique
- related systems
- next systems to learn

This turns the ontology into a navigation engine.

---

# 10. Champion Knowledge Capture

Champion knowledge should be captured using the ontology.

Interview structure:

- what problem does this system solve?
- what tools are used?
- what techniques are applied?
- what pattern does it follow?
- what evidence shows it works?
- what related systems does it connect to?

This ensures expert knowledge becomes structured.

---

# 11. Future Extensions

Potential future ontology extensions include:

- constraints
- evaluation metrics
- failure modes
- maturity stages
- pricing / monetization metadata
- implementation difficulty
- audience suitability

These can be added later without redesigning the entire ontology.

---

# 12. Strategic Value

This ontology becomes the knowledge engine of the platform.

It enables:

- consistent documentation
- better education design
- structured expert publishing
- knowledge graph development
- future search, recommendation, and marketplace features

The ontology is not just a taxonomy.

It is the structural model of how the platform understands **applied AI systems**.