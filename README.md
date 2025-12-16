# fastai → Hugging Face Deployment

This repository is a hands-on, end-to-end deployment playbook showing how to take a trained fastai model from a local notebook and deploy it as a live, public application on Hugging Face Spaces using Gradio.

This is not a “happy path” tutorial.

It documents the real work that happens after training:
- exporting models correctly
- handling Python and library version mismatches
- managing Git, Git LFS, and Hugging Face Spaces
- debugging opaque runtime errors
- turning a working demo into something reproducible and shareable

---

## Live Demo

Bear Detector App (Hugging Face Spaces)  
https://huggingface.co/spaces/rgiri2025/bear-detector

Documentation Site (GitHub Pages)  
https://codekunoichi.github.io/fastai-hf-deployment/

---

## What This Repo Is (and Isn’t)

This repo is:
- A practical deployment walkthrough
- A learning artifact created while studying the fast.ai course
- A reference for future projects and for teaching others

This repo is not:
- A model accuracy benchmark
- A fastai internals deep dive
- A polished framework or template

---

## Repository Structure

.
├── apps/
│   └── bear-detector/
│       ├── app.py
│       ├── requirements.txt
│       └── README.md
│
├── docs/
│   ├── index.md
│   ├── bear-detector-journey.md
│   ├── troubleshooting.md
│   └── hf-spaces-checklist.md
│
├── mkdocs.yml
├── requirements-docs.txt
└── .github/workflows/
    └── publish-mkdocs.yml

---

## Background

This work builds on concepts from the fast.ai Practical Deep Learning for Coders course:
- Training a simple image classifier
- Extending the workflow to a custom dataset
- Exporting a trained learner

The example classifier distinguishes between:
- Grizzly bear
- Black bear
- Teddy bear

The emphasis here is not the model, but everything that breaks after training.

---

## Why This Exists

Most ML tutorials stop right when things get interesting.

This repo exists to capture:
- confusion
- mistakes
- fixes
- and the muscle memory required to deploy ML systems in the real world

It is written for:
- learners transitioning from notebooks to production
- engineers new to ML deployment
- students learning how to document their thinking, not just their code

---

## How to Use This Repo

- Follow the Bear Detector Journey to see the full arc
- Use the HF Spaces Checklist before deploying your own app
- Refer to Troubleshooting when something breaks
- Fork and adapt this structure for your own fastai to Hugging Face projects

---

## What’s Next

This repo may grow to include:
- additional deployment examples
- versioning strategies
- notes on safer model loading
- guidance for students publishing their first serious repositories


