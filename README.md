# Md Naim

**AI engineering student | LLM systems, inference serving and applied computer vision**

Faculty of Engineering · Information Technology · Tokyo Polytechnic University, Japan

I build and test software around language models and machine learning: backend services, retrieval systems, inference APIs and reproducible evaluation. My projects prioritize measurable behavior, clear limitations and engineering documentation.

## Selected engineering projects

### [CortexLite — Native C/C++ AI Inference & Vector Search](https://github.com/naim-munshi/cortexlite-ai-engine)

**Completed educational v1.0.** Built an inspectable CPU-only pipeline combining **C11 neural-network inference** with **C++17 custom hash tables, top-K heaps and exact/graph similarity search**. Includes PyTorch training/export, FP32 and weight-only INT8 execution, SSE2/ARM NEON kernels, and reproducible macOS/Linux CI tests. On an actual macOS ARM64 benchmark, four-thread execution measured **1.69× wall throughput** over scalar single-thread execution on a small synthetic workload; the [35-run raw evidence and limitations](https://github.com/naim-munshi/cortexlite-ai-engine/blob/main/docs/results-macos.md) are public.

**Technologies:** C11 · C++17 · Python · PyTorch · CMake/Clang · GitHub Actions

### [Metriqen — LLM Serving & Benchmarking](https://github.com/naim-munshi/metriqen-llm-serving-optimization)

Local open-weight LLM inference prototype with a Go streaming gateway, bounded FIFO request admission, Python performance benchmarks and evidence-based evaluation. Includes a [developer-operated local case study](https://github.com/naim-munshi/metriqen-llm-serving-optimization/blob/main/docs/benchmarks/experiments/2026-10-13-ollama-parallelism.md), with results explicitly labeled descriptive rather than causal.

**Technologies:** Go · Python · Ollama · FastAPI · GitHub Actions

### [Aqlyra RAG AI](https://github.com/naim-munshi/aqlyra-rag-ai)

RAG-oriented system for hybrid retrieval, grounding, citation validation and retrieval evaluation.

**Technologies:** Python · FastAPI · PostgreSQL · pgvector · Docker

## Engineering interests

LLM inference infrastructure · RAG and retrieval quality · AI evaluation · backend systems · reproducible machine learning experiments

Project READMEs distinguish implemented components, limitations, and planned work. CortexLite v1.0 is complete within its educational scope; other systems continue to evolve.
