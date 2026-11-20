# Md Naim

**AI / Machine Learning Engineer · Generative AI · RAG Systems · LLM Infrastructure**

Faculty of Engineering · Information Technology · Tokyo Polytechnic University, Japan

I build and evaluate AI-enabled software across **Python/FastAPI backends, React/TypeScript applications, retrieval and LLM workflows, multimodal machine learning, and native inference systems**. My portfolio focuses on inspectable implementations, automated tests, reproducible experiments, and honest reporting of engineering trade-offs.

**🚀 Live application:** [https://aqlyra-ai.vercel.app](https://aqlyra-ai.vercel.app)

## Featured engineering projects

These projects are selected for their technical depth and relevance to AI application, ML systems, and infrastructure engineering.

### 1. [Aqlyra — Full-Stack AI Knowledge & RAG Application](https://github.com/naim-munshi/aqlyra-rag-ai)

**Deployed engineering beta · Not enterprise-production certified**

A multilingual AI knowledge application with a separately deployed **Next.js / React / TypeScript frontend** and **Python / FastAPI backend**, Neon PostgreSQL + pgvector, Redis, and an isolated 384-dimensional semantic worker. It includes private document ingestion, hybrid dense and lexical retrieval, Reciprocal Rank Fusion (RRF), evidence-grounded answers, citation validation, streaming chat, personal memory, and web research.

**Measured engineering evidence (10 November 2026):** 1,035 / 1,035 eligible ready Knowledge chunks had matching current 384D semantic vectors. This is index coverage, not answer accuracy. On 60 synthetic multilingual queries, the deployed-weight encoder's offline dense Hit Rate@1 was **70% English / 35% Japanese / 60% Bengali**. These measurements are not live answer-quality or customer-performance claims; Japanese retrieval remains an improvement area.

**Outstanding acceptance gates:** real authenticated multi-user end-to-end testing, representative answer-quality evaluation, multilingual real-time voice testing, and encrypted off-host database/object recovery. Render Free cold starts and provider quotas also affect availability.

**Stack:** Python · FastAPI · TypeScript · Next.js · React · PostgreSQL · pgvector · Redis · Docker · ONNX

**Explore:** [Open Aqlyra](https://aqlyra-ai.vercel.app) · [Repository](https://github.com/naim-munshi/aqlyra-rag-ai) · [Active backend release](https://github.com/naim-munshi/aqlyra-rag-ai/tree/release/core-without-study-abroad-20261027) · [Phase 1 evaluation and acceptance report](https://github.com/naim-munshi/aqlyra-rag-ai/blob/release/core-without-study-abroad-20261027/docs/PORTFOLIO_PHASE1_AUDIT_20261110.md) · [GitHub Actions](https://github.com/naim-munshi/aqlyra-rag-ai/actions)

*Deployment note: the Vercel frontend and Render backend use separate release branches. The protected `main` branch is a historical baseline, not the source of both live deployments. The former scripted `/demo` route has been retired; the link above opens the actual application.*

### 2. [Metriqen — LLM Serving & Performance Engineering](https://github.com/naim-munshi/metriqen-llm-serving-optimization)

**Source-available local research prototype · Portfolio v1.0 not released**

A local LLM serving system that explores the boundary between an inference gateway, model runtime, and operator control plane. It combines a **Go OpenAI-compatible streaming gateway**, local Ollama inference, bounded request admission and cancellation, an optional **FastAPI control plane**, and reproducible performance experiments. The engineering reports document both positive and negative results rather than presenting uncontrolled measurements as production speedups.

**Stack:** Go · Python · FastAPI · Ollama · PostgreSQL · Redis · Docker · GitHub Actions

**Review:** [Engineering case study](https://github.com/naim-munshi/metriqen-llm-serving-optimization/blob/main/docs/PORTFOLIO_CASE_STUDY.md) · [CI](https://github.com/naim-munshi/metriqen-llm-serving-optimization/actions)

### 3. [IhsanVision.AI — Industrial Visual Anomaly Detection](https://github.com/naim-munshi/ihsanvision-ai-industrial-anomaly-detection)

**Applied ML engineering prototype · Not a production-certified inspection system**

An industrial anomaly-detection application built with **PyTorch and Anomalib**, comparing PaDiM and PatchCore for normal-only visual inspection. The project includes a FastAPI inference interface, checkpoint-backed local predictions, anomaly heatmaps, model evaluation, and serving measurements. Measured model results currently cover the **MVTec AD bottle category** under a documented split protocol; they should not be generalized to other product categories or factory conditions.

**Stack:** Python · PyTorch · Anomalib · PaDiM · PatchCore · FastAPI · SQLite · Docker · GitHub Actions

**Review:** [Measured results and evaluation protocol](https://github.com/naim-munshi/ihsanvision-ai-industrial-anomaly-detection/blob/main/docs/evaluation.md) · [Model card](https://github.com/naim-munshi/ihsanvision-ai-industrial-anomaly-detection/blob/main/docs/model-card.md) · [CI](https://github.com/naim-munshi/ihsanvision-ai-industrial-anomaly-detection/actions)

### 4. [Video Scene Search — Multimodal Video Retrieval](https://github.com/naim-munshi/video-scene-search)

**Local single-user prototype · v0.1 engineering checks passed**

A multimodal search prototype for finding relevant moments in video using natural-language queries. It combines **CLIP visual embeddings**, **Whisper speech transcription**, MiniLM text embeddings, FAISS indexes, intent-weighted Reciprocal Rank Fusion, and timestamped playback. The repository also contains a frozen-query and human-review evaluation workflow.

The initial three-video evaluation uses AI-assisted weak relevance labels. Its exploratory retrieval measurements are **not independently human-validated accuracy results**. The project is local-only and does not claim a hosted multi-user service.

**Stack:** Python · CLIP · Whisper · MiniLM · FAISS · Streamlit · FFmpeg

**Review:** [Engineering brief](https://github.com/naim-munshi/video-scene-search/blob/main/docs/RECRUITER_BRIEF.md) · [Human evaluation protocol](https://github.com/naim-munshi/video-scene-search/blob/main/docs/HUMAN_EVALUATION.md) · [CI](https://github.com/naim-munshi/video-scene-search/actions)

### 5. [CortexLite — C/C++ Neural Inference & Vector Search](https://github.com/naim-munshi/cortexlite-ai-engine)

**Educational CPU AI systems and DSA project**

A compact end-to-end inference/search engine: train a small model with PyTorch, export its weights, run inference in **C11**, and perform exact or approximate vector retrieval in **C++17**. It implements custom hash maps, top-K heaps, a neighbor graph, SIMD paths, multithreaded execution, and weight-only INT8 quantization.

**Measured macOS ARM64 toy workload:** 35 observations across five runs per configuration measured **1.69×** four-thread vs one-thread wall throughput, **37.3%** lower stored model-parameter bytes with weight-only INT8, and **95.2% Recall@10** at ef=64 on 1,000 seeded synthetic 32-dimensional vectors. These are small educational benchmarks—not large-model inference, production serving, or general semantic-search results.

**Stack:** C11 · C++17 · Python · PyTorch · CMake / Apple Clang · GitHub Actions

**Review:** [macOS benchmark and limitations](https://github.com/naim-munshi/cortexlite-ai-engine/blob/main/docs/results-macos.md) · [Technical reviewer brief](https://github.com/naim-munshi/cortexlite-ai-engine/blob/main/docs/portfolio-brief.md) · [Native build instructions](https://github.com/naim-munshi/cortexlite-ai-engine#run-it-yourself)

## Core engineering interests

Generative AI and LLM applications · Retrieval quality and grounded answers · Multimodal search · REST APIs and microservices · Model evaluation · Observability and performance · Computer vision · Data structures and algorithms

## Project status

Aqlyra is a deployed public engineering beta, not enterprise-production certified. Metriqen is a local research prototype and its v1.0 portfolio release is not complete. IhsanVision.AI remains an ML engineering prototype with a limited, documented evaluation scope. Video Scene Search is a local multimodal prototype with independent human-label validation still outstanding. CortexLite is complete within its deliberately small educational scope.

Each repository documents what has been implemented, what has actually been tested, and what remains unverified. [Browse all public repositories](https://github.com/naim-munshi?tab=repositories).
