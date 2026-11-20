# Md Naim

**AI / Machine Learning Engineer — Generative AI Applications, Full-Stack AI Systems & Model Serving**

Faculty of Engineering · Information Technology · Tokyo Polytechnic University, Japan

I develop and evaluate AI-enabled applications across **Python/FastAPI backends, React/TypeScript frontends, retrieval and LLM workflows, and native inference systems**. My repositories emphasize implementation, automated tests, reproducible measurements and clearly stated engineering limitations.

## Featured engineering projects

These repositories are ordered by relevance to **full-stack AI application engineering and LLM-enabled services**. Each links to inspectable source code and validation evidence.

### 1. [Aqlyra — Full-Stack AI Knowledge & RAG Application](https://github.com/naim-munshi/aqlyra-rag-ai)

**Public engineering beta; not enterprise-production certified.** Built a full-stack AI knowledge application with a separately deployed **Next.js / React / TypeScript frontend** and **Python / FastAPI backend**, **Neon PostgreSQL + pgvector**, Redis and an isolated 384-dimensional multilingual semantic worker. The application includes private document ingestion, dense and lexical retrieval, Reciprocal Rank Fusion (RRF), evidence-grounded answers, citation validation, streaming conversations, memory and web research.

**Measured engineering evidence (10 November 2026):** 1,035 / 1,035 eligible ready chunks had current 384D semantic vectors indexed. The deployed compact multilingual encoder's offline Hit Rate@1 on 60 synthetic queries was **70% English / 35% Japanese / 60% Bengali**. These are index-coverage and offline retrieval measurements—not live answer accuracy, customer quality or an availability SLA. Japanese retrieval remains an improvement area.

**Outstanding release gates:** real authenticated multi-user end-to-end acceptance, multilingual voice acceptance, representative independent answer-quality evaluation, and verified encrypted off-host database/object recovery. The public `/demo` route is a clearly labelled scripted preview; it does not perform live inference.

**Stack:** Python · FastAPI · TypeScript · Next.js · React · PostgreSQL · pgvector · Redis · Docker · ONNX

**Explore:** [Live application](https://aqlyra-ai.vercel.app) · [Scripted demo](https://aqlyra-ai.vercel.app/demo) · [Active backend release README](https://github.com/naim-munshi/aqlyra-rag-ai/blob/release/core-without-study-abroad-20261027/README.md) · [Phase 1 evaluation and acceptance report](https://github.com/naim-munshi/aqlyra-rag-ai/blob/release/core-without-study-abroad-20261027/docs/PORTFOLIO_PHASE1_AUDIT_20261110.md) · [GitHub Actions](https://github.com/naim-munshi/aqlyra-rag-ai/actions)

*Repository note: Aqlyra's protected `main` branch is a historical baseline, not the deployed backend release. The current backend source and its status evidence are linked above.*

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

*Project status: Aqlyra is a public engineering beta, not enterprise-production certified; Metriqen and IhsanVision remain engineering prototypes; CortexLite v1.0 is complete within its deliberately small educational scope. Each repository documents what has been tested and what remains open.*
