# Md Naim

**AI / Machine Learning Engineer — Generative AI Applications, Full-Stack AI Systems & Model Serving**

Faculty of Engineering · Information Technology · Tokyo Polytechnic University, Japan

I develop and evaluate AI-enabled applications across **Python/FastAPI backends, React/TypeScript frontends, retrieval and LLM workflows, and native inference systems**. My repositories focus on implementation, automated tests, reproducible measurements and explicit limitations rather than unsupported production claims.

## Featured engineering projects

These repositories are ordered by relevance to **full-stack AI application engineering and LLM-enabled services**. Each links to inspectable source code and its actual validation evidence.

### 1. [Aqlyra — Full-Stack AI & Retrieval-Augmented Generation](https://github.com/naim-munshi/aqlyra-rag-ai)

**Closest match to full-stack Generative AI engineering.** Developed a pre-production AI knowledge application with **Next.js / React / TypeScript**, **Python / FastAPI**, **PostgreSQL + pgvector**, hybrid dense/lexical retrieval, citation validation, grounding checks, document ingestion and streaming conversations. Includes user-scoped access control, Docker-based deployment configurations, automated tests and pre-deployment CI; public HTTPS launch and provider-backed end-to-end acceptance are not yet confirmed.

**Stack:** Python · FastAPI · TypeScript · Next.js · React · PostgreSQL · pgvector · Docker  
**Review:** [Architecture and limitations](https://github.com/naim-munshi/aqlyra-rag-ai#how-the-system-is-structured) · [CI workflows](https://github.com/naim-munshi/aqlyra-rag-ai/actions)

### 2. [Metriqen — LLM Serving & Performance Engineering](https://github.com/naim-munshi/metriqen-llm-serving-optimization)

**LLM infrastructure and operational reliability.** Built a local open-weight LLM inference prototype using a **Go streaming/API gateway**, Ollama, bounded request admission, a **Python/FastAPI** control plane and reproducible load/quality evaluation. Benchmarks include throughput, time-to-first-token and latency measurements, with workload and host limitations documented. The portfolio release and production deployment are **not** claimed complete.

**Stack:** Go · Python · FastAPI · Ollama · PostgreSQL · Docker · GitHub Actions  
**Review:** [Engineering case study](https://github.com/naim-munshi/metriqen-llm-serving-optimization/blob/main/docs/PORTFOLIO_CASE_STUDY.md) · [CI](https://github.com/naim-munshi/metriqen-llm-serving-optimization/actions)

### 3. [IhsanVision.AI — Industrial Visual Anomaly Detection](https://github.com/naim-munshi/ihsanvision-ai-industrial-anomaly-detection)

**Applied machine learning and model evaluation.** Implemented **PyTorch / Anomalib** anomaly-detection experiments using PaDiM and PatchCore, with documented MVTec AD *bottle* results, local checkpoint-backed inference, FastAPI interfaces, automated tests and model-serving measurements. Additional category evaluation and final release acceptance remain in progress.

**Stack:** Python · PyTorch · Anomalib · FastAPI · Docker · GitHub Actions  
**Review:** [Observed model evaluation](https://github.com/naim-munshi/ihsanvision-ai-industrial-anomaly-detection#measured-model-performance--mvtec-ad-bottle) · [Evaluation protocol](https://github.com/naim-munshi/ihsanvision-ai-industrial-anomaly-detection/blob/main/docs/evaluation.md)

### 4. [CortexLite — C/C++ Neural Inference & Vector Search](https://github.com/naim-munshi/cortexlite-ai-engine)

**Algorithms and low-level AI execution.** Completed an educational **C11/C++17** inference/search engine with PyTorch weight export, custom hash maps and top-K heaps, exact/graph cosine retrieval, SIMD and weight-only INT8. The 35-run macOS ARM64 toy workload measured **1.69× four-thread vs one-thread wall throughput**, **37.3% lower model parameter storage** and **95.2% Recall@10** for seeded synthetic vector retrieval (ef=64). These are **not** large-model or production service benchmarks.

**Stack:** C11 · C++17 · Python · PyTorch · CMake / Apple Clang · GitHub Actions  
**Review:** [macOS benchmark and limitations](https://github.com/naim-munshi/cortexlite-ai-engine/blob/main/docs/results-macos.md) · [Native build instructions](https://github.com/naim-munshi/cortexlite-ai-engine#run-it-yourself)

## Core engineering interests

Generative AI and LLM applications · Retrieval quality and grounded answers · REST APIs and microservices · Model evaluation · Observability and performance · Computer vision · Data structures and algorithms

*Status matters: Aqlyra is pre-production; Metriqen and IhsanVision remain engineering prototypes; CortexLite v1.0 is complete within its deliberately small educational scope. Repository documentation identifies what has been tested and what is still planned.*
