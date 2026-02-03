# BMW Build AI

A lightweight, **100% local** AI advisor for building and modding 80s BMW M3 (E30 era), 328, and 330 models (E46 chassis) — focusing on modifications that balance performance (handling, power, braking) with aesthetics (style, stance, interior).

Suggests balanced mods, parts lists, build plans, and generates simple text-based schematics (e.g., wiring diagrams, suspension layouts via ASCII or Graphviz DOT code).

Powered by **Ollama** (local LLMs) + **Gradio** (chat UI).  
No API keys, no cloud, fully offline & private.

> "Balance the art of speed and style." — Your AI Mechanic

## Features

- Model-specific advice: 80s M3 (E30), 328/330 (E46)
- Balanced mods: e.g., coilovers for stance + handling, wheels for looks + grip, intakes/exhausts for power + sound
- Schematics: Outputs text-based diagrams (ASCII art) or DOT code for Graphviz (renderable locally)
- Build plans: Step-by-step guides, budgets, compatibility checks
- Strict theme: BMW mods only — redirects off-topic
- Educational: Safety tips, common pitfalls, historical context

## Quick Start

### Prerequisites

1. Install [**Ollama**](https://ollama.com)
2. Pull a model:
   ```bash
   ollama pull llama3.2:3b     # fast & small (~2 GB)
   # Better for detailed advice: ollama pull llama3.1:8b
