# Bear Detector – Gradio App (fastai)

This folder contains a **minimal, deployable Gradio application** that serves a trained **fastai image classifier** as an interactive interface.

The app is intentionally simple. Its purpose is to demonstrate a **clean deployment pattern** for fastai models on **Hugging Face Spaces**, not to showcase model performance.

---

## What This App Does

- Loads a trained fastai image classification model (`model_resnet18.pkl`)
- Accepts an input image via a Gradio UI
- Runs inference using fastai
- Returns predicted labels with associated probabilities

The live, running version of this app is hosted on Hugging Face Spaces:

👉 https://huggingface.co/spaces/rgiri2025/bear-detector

---

## What This Folder Contains

- `app.py`  
  The Gradio application entry point. This is the file Hugging Face executes.

- `requirements.txt`  
  Pinned dependencies required to run the app reliably in a hosted environment.

- `README.md`  
  This file. Explains how the app is structured and how to use it.

**Note:**  
The trained model file (`model_resnet18.pkl`) is **not** stored in this GitHub repository.  
It is hosted in the Hugging Face Space and managed via Git LFS/Xet there.

---

## How the App Works (High Level)

1. The model is loaded using `fastai.load_learner(...)`
2. Images uploaded through Gradio are converted to `PILImage`
3. fastai performs inference and returns:
   - predicted label
   - class probabilities
4. Results are displayed via Gradio’s `Label` component

The app forces **CPU inference**, which is appropriate for Hugging Face Spaces and avoids device-related issues.

---

## Running Locally (Optional)

If you want to run this app locally:

1. Create a virtual environment (recommended)
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the model file from the Hugging Face Space and place it in this folder:
   ```
   model_resnet18.pkl
   ```
4. Start the app:
   ```bash
   python app.py
   ```

You should see a local URL (e.g. `http://127.0.0.1:7860`) where you can test the interface.

---

## Deployment Notes (Important)

- Hugging Face Spaces rebuild on **every git push**
- The Python version must match the one used during model export
- Binary artifacts (models, images) should be handled via **Git LFS/Xet** on Hugging Face
- Avoid `pip -U` in hosted environments
- Pin dependencies explicitly

For detailed troubleshooting and lessons learned, see:
- `docs/bear-detector-journey.md`
- `docs/troubleshooting.md`

---

## Why This Exists

This app exists as a **reference implementation**:

> A small, boring, reliable deployment is better than a clever but fragile one.

Use this pattern as a starting point for deploying other fastai models (e.g. medical imaging, tabular classifiers, NLP models).
