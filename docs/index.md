# fastai → Hugging Face Deployment Playbook

## Purpose

This repository documents the **end-to-end journey of deploying a fastai model** from a local notebook environment to a live, publicly accessible application on **Hugging Face Spaces** using **Gradio**.

The focus here is *not* on model accuracy or architecture tuning, but on everything that happens **after training**:
- exporting a model
- handling environment and version mismatches
- managing binaries and Git workflows
- adapting to library and API drift
- getting a real deployment running

This repo exists to capture the *practical realities* of ML deployment that are often skipped in tutorials.

---

## Background

The work here builds on concepts from the **fastai course**:

- **Chapter 1**: Training a simple image classifier (e.g., “Is it a bird?”)
- **Chapter 2**: Extending the same workflow to custom datasets

Using those foundations, the classifier was extended to detect:
- Grizzly bears
- Black bears
- Teddy bears

The trained model was then exported and deployed as a live application.

---

## Live Demo

You can try the deployed application here:

👉 **Bear Detector – Hugging Face Space**  
https://huggingface.co/spaces/rgiri2025/bear-detector

---

## Key Learnings Captured in This Repo

This repository documents lessons learned the *hard way*, including:

- Using **Git LFS** to manage large binary artifacts (`model.pkl`, example images)
- Generating and using **Hugging Face Personal Access Tokens (PATs)** for Git authentication
- Why **Python version mismatches** (3.10 vs 3.12) can break fastai model loading
- The importance of pinning dependencies (e.g. `numpy<2`)
- Why blindly running `pip -U` in notebooks is risky
- How **Gradio APIs changed** over time and why older tutorials break
- How to read **Hugging Face Build logs vs Container logs**
- What a minimal, working `app.py` for fastai + Gradio looks like today

---

## About the Tutorials

An older tutorial was used as an initial reference:

- Tanishq’s Gradio + Hugging Face blog (2021):  
  https://www.tanishq.ai/blog/posts/2021-11-16-gradio-huggingface.html

That blog is helpful conceptually, but much of the code no longer works due to:
- library version changes
- deprecated Gradio APIs
- updated Hugging Face deployment requirements

This repository documents the **necessary updates and fixes** to make the workflow work in a modern (2025) environment.

---

## Repository Structure

- `apps/` – deployable application examples (e.g. bear-detector)
- `docs/` – detailed journey logs, troubleshooting, and checklists
- Hugging Face Spaces – hosts the live demo and model artifacts

---

## Why This Exists

This is a **learning artifact**, not just a demo.

The goal is to leave behind a clear, honest record of:
> “What actually breaks when you try to deploy a real ML model — and how to fix it.”

If you are moving from notebooks to real deployments, this repo is for you.