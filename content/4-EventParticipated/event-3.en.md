---
title: "4.3. Event Recap: FCAJ Community Day (June 27, 2026)"
weight: 3
---

## Event Recap: Personal Learnings from FCAJ Community Day on June 27, 2026

Hello everyone,

Today I am sitting down again to type out a quick recap of the **FCAJ Community Day** tech event that took place this past June. This event painted a comprehensive picture of how enterprises apply AI in reality, from infrastructure operations to human resource management.

Below are 5 lessons and 5 real-world experiences from the speakers that brought me new perspectives on the Agentic AI era.

---

### 1. Deep Response Engine: Shifting from 'Alert' to 'Action'
*Speaker: Steve Tran*

![Steve Tran](/FCAJ%20June%2027%20assets/Steve%20Tran.jpg)

**Core Content:**
Mr. Steve pointed out the 'complexity wall' that modern cloud systems are facing. Instead of relying on alert-driven systems that keep ops teams constantly 'on fire', the solution is to shift to an Action-driven system. With the Deep Response Engine, AI not only reports errors but also automatically conducts investigations and proposes mitigation plans, reducing incident response time from hours to mere minutes.

> **Personal Experience:**
> I realized that startups often get stuck building 'BC ideas' without 'Customer Champions'. The biggest lesson is to tie solutions to actual enterprise problems (like F88, FPT), where every minute of downtime equals money lost.

---

### 2. Voice Agents: When AI Speaks Human
*Speakers: Trung, Kiet Tran, and Nghi Danh Hoang Hieu*

![Trung Vu](/FCAJ%20June%2027%20assets/Trung%20Vu.jpg)

**Core Content:**
Moving from traditional IVRs and Chatbots, we have entered the era of AI Voice Agents. Mr. Trung emphasized the challenge of the Vietnamese language being a 'low resource language'. Instead of using full speech-to-speech models (which are often unstable), the solution is a 3-step architecture: `Speech-to-Text -> LLM (logic processing) -> Text-to-Speech (voice generation)`. Especially when building for banks, strict adherence to Audit logs, Versioning, and Knowledge bases is essential to prevent the AI from hallucinating.

---

### 3. AWS DevOps Agent: The Operations Assistant That Never Sleeps
*Speakers: Ms. Bao & Mr. Nguyen*

![Bao and Nguyen](/FCAJ%20June%2027%20assets/Ms%20Bao%20and%20mr%20Nguyen.jpg)

**Core Content:**
This was my favorite part due to its high applicability for DevOps engineers. The system uses the concept of an Agent Space to learn the topology of the infrastructure. When an incident occurs (e.g., an ECS task failure), the agent automatically traces the root cause and provides a mitigation plan, leaving the operator only to approve it (Human-in-the-loop).

> **Personal Experience:**
> A prerequisite is that the system must have strong Observability (clear logs, metrics, and alarms). If you lack baseline data, AI is just 'a blind man examining an elephant', generating information without specific context. The cited 77% reduction in MTTR at a university is a very convincing figure.

---

### 4. Amazon Quick Suite: Redefining HR Productivity
*Speakers: Mr. Truong & Ms. Minh Anh*

![Truong Tran](/FCAJ%20June%2027%20assets/Truong%20tran.jpg)

**Core Content:**
The combination of Amazon Quick and HR workflows. More than just a chatbot tool, Quick helps automate CV screening (OCR), cross-referencing with JDs, and scoring candidates based on technical/soft skill scales. It transforms HR from 'administrative workers' to 'human resource strategists' by freeing them from repetitive tasks.

---

### 5. Building Secure MCP Connections
*Speakers: Toan Nguyen & Mr. Nghi*

![Toan Nguyen](/FCAJ%20June%2027%20assets/Toan%20Nguyen.jpg)

**Core Content:**
The Model Context Protocol (MCP) acts as a bridge for AI to 'expand' into the world (Jira, Zalo, Gmail, AWS). However, the security risks are massive. The speakers demonstrated how to set up VPC Private Connectivity, use ALBs, and implement TLS encryption to ensure the MCP server remains safely in a Private Subnet, preventing sensitive data from being publicly exposed to the Internet.

> **Personal Experience:**
> This technique reminded me that new technologies always bring new security risks. Never prioritize the convenience of AI at the expense of exposing sensitive endpoints to the public.

---

## Conclusion

![Conclusion](/FCAJ%20June%2027%20assets/conclusion.jpg)

After the event, I drew a core realization: **AI Agents will not replace humans, but humans who use AI Agents will replace those who don't.**

My takeaway is that we must start establishing robust Observability infrastructure, ensure all MCP connections reside within a secure VPC, and most importantly, design AI processing workflows so that humans always retain the final control (Human-in-the-loop).

It's not just about building tools, but designing an automated and secure operational ecosystem.
