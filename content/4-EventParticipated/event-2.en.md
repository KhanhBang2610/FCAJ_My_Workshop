---
title: "4.2. Event Recap: FCAJ Community Day"
weight: 2
---

## Event Recap: Personal Learnings from FCAJ Community Day on May 23, 2026

Hello everyone,

Today I wanted to sit down and type out a quick recap of the **FCAJ Community Day** tech event that took place on May 23.

Below are 6 lessons and 6 real-world experiences from the speakers that provided me with new perspectives—not only on technology but also on how to handle work correctly to achieve the best performance.

---

### 1. The Uncontrollability of LLMs: Temp = 0 Cannot Stop AI from "Flipping"
*Speaker: Duc Dao (Solution Architect)*

**Core Content:**
Mr. Duc Dao's talk gave me a different perspective. For a long time, when coding AI integration flows, I always assumed that setting the `temperature = 0` parameter meant the system would return a 100% perfectly formatted JSON every single time. But the truth is: LLMs can still output different results! The root cause lies in floating-point errors on GPU architectures and the batching optimization mechanisms of providers.

> **Personal Experience:**
> Hearing about the hardware-level GPU cause really changed my understanding. AI is ultimately about probability, not linear mathematical functions. Instead of trying to force it into a rigid machine, Mr. Duc's advice is to use `temperature = 0.1` to avoid vocabulary repetition, combine it with JSON mode, and most importantly: **Design backend systems that accept output variability**. Clearly, anticipating errors and implementing robust Exception Handling is crucial.

---

### 2. Stop Being an "Internet Garbage Collector"
*Speaker: Tinh Truong (Platform Engineer)*

![Tinh Truong](/FCAJ%20May%2023%20assets/Tinh%20Truong.jpg)

**Core Content:**
Mr. Tinh Truong exposed a harsh truth: When an AI model gives a "nonsensical" answer, it's usually not because the AI is bad, but because we provided the wrong context. Many people are stuck in "Internet Puller" syndrome—shoving a chaotic, redundant mess of information in the AI's face or giving vague, unconstrained requests. His proposed solution is to build a **"Second AI Brain"** using a standard flow: `Store -> Retrieve -> Generate -> Learn`.

> **Personal Experience:**
> Honestly, I felt called out! How many times have I copied an entire, massive document file, thrown it into AI Agent tools like Cursor or Trae, and then gotten frustrated when it didn't code the way I wanted? This sharing helped me redefine how to build RAG (Retrieval-Augmented Generation) systems. The quality of a Vector DB depends entirely on how we clean and chunk the data in the "Store" step, not on how many billion parameters the model has.

---

### 3. 36 hours, one product
*Speaker: Team VIB*

![Team VIB](/FCAJ%20May%2023%20assets/Team%20VIB.jpg)

**Core Content:**
Team VIB shared the journey of the UTMorpho project development team at LotusHacks, the largest hackathon in Vietnam. They shared the process of transforming a raw idea into a real product in just 36 high-pressure hours, while emphasizing lessons on endurance and teamwork.

As the winning team in the AWS Track division, they shared significant milestones—from defining the problem to pivotal failures. Finally, they shared the future directions to integrate the product into actual workflows and continue spreading the spirit of learning through open-source platforms.

---

### 4. CloudFront is Not Just a CDN, it’s an Application Protection and Optimization Platform
*Speaker: Nguyen Tuan Thinh (DevOps Engineer)*

![Nguyen Tuan Thinh](/FCAJ%20May%2023%20assets/Thinh%20Nguyen.jpg)

**Core Content:**
CDNs are often viewed merely as auxiliary infrastructure, but Mr. Thinh proved the opposite. Besides the power of over 700 global PoPs that reduce latency, CloudFront has the ability to stop DDoS attacks right at the Edge instead of waiting 3-4 minutes like before.

Especially with the Flat-rate pricing update (launched November 18, 2025), monthly bills become predictable. Coupled with caching and data compression, file sizes can be reduced by up to 82%.
Furthermore, it provides reliability by automatically routing traffic to a Secondary Origin when the primary one fails, as well as serving stale content from cache when the Origin times out, ensuring an uninterrupted user experience.

> **Personal Experience:**
> I realized that sometimes, exhaustively optimizing code doesn't save as many EC2 or ALB resources as configuring the external network layer correctly. Reducing static payload bandwidth by 82% means never having to fear a skyrocketing AWS bill due to traffic spikes.

---

### 5. Delegating Boredom to Amazon Quick Suite
*Speaker: Pham Hai Anh*

![Pham Hai Anh](/FCAJ%20May%2023%20assets/Hai%20Anh.jpg)

**Core Content:**
Under the Automation theme, Mr. Hai Anh introduced Amazon Quick Suite (Agentic AI). This tool connects directly to over 40 different data sources, automating thousands of tasks across third-party applications. From scheduling meetings to auto-drafting emails and creating accurate Minutes of Meeting (MoM), its standout features include:
- **Data & Knowledge:** Uses company data via Spaces/datasets, combines world knowledge, supports user-uploaded files, connects to databases/data warehouses, and integrates 40+ Data connectors.
- **Actions:** Capable of executing thousands of actions in third-party apps, providing embeddable UIs and APIs.
- **Responsible AI:** Ensures compliance, access control, and data security using Guardrails and strict Governance.
- **BI & Automation:** Provides Dashboards, Scenarios, Insights. Supports automated flows for departments like Sales, Marketing, HR, and Support.

> **Personal Experience:**
> As someone who strongly dislikes writing reports or aggregating logs after every project phase, having an "AI agent" handle all these routine tasks truly optimizes my performance. It allows me to fully focus my brainpower on thinking about data flows rather than getting stuck in administrative chores.

---

### 6. Enterprise-Grade Multi-Agent System
*Speaker: Vy Lam*

![Vy Lam](/FCAJ%20May%2023%20assets/Vy%20Lam.jpg)

**Core Problem:** 
Ms. Vy analyzed how traditional credit scoring models are unsuitable for the reality of startups (which require long-term financial histories and collateral, while startups have novel models and unstructured data).

**Multi-Agent Paradigm:** 
Building a "Virtual Credit Committee" with specialized agents (Finance, Market, Team, Risk, Compliance) to conduct multidimensional analysis instead of relying on a single model.

**ROI:** 
Transitioning to a multi-agent system significantly optimizes operational workflows, reducing costs and processing times.

---

## Conclusion

![Conclusion](/FCAJ%20May%2023%20assets/Conclusion.jpg)

After attending these sessions, the biggest takeaway I received was a "Reset" in perspective. No more absolute reliance on machines, and no more mindlessly cramming data. 

From these experiences, my key takeaway is that I definitely need to review my systems, check CloudFront compression configurations, fine-tune the Temperature parameters, and redesign entire AI processing workflows to accept variability. 

**It's no longer just about writing code that runs; it's about designing systems robust enough to meet enterprise requirements.**
