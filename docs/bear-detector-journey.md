# Bear Detector Deployment Journey (My Brain Tattoo 🧠)

This document captures the *real* end-to-end journey of taking a trained fastai model and deploying it as a live application on Hugging Face Spaces using Gradio.

This is intentionally written as a **battle log** — not a polished tutorial — so future‑me (and others) can remember *what actually broke, why it broke, and how it was fixed*.

---

## 1. Goal

The goal of this repository is to document the **post–model‑training journey**:

- What it takes to move from a trained fastai model (`learn.export`)
- To a deployed, publicly accessible application
- With a stable API/UI for inference
- Using **Hugging Face Spaces + Gradio**

This work is part of a broader effort to deeply understand **practical deep learning**, not just model training.

For example:
- You can train a bird detector or bear classifier in a notebook
- But how do you *actually* deploy it so someone else can use it?
- What breaks when you leave the notebook world?

This repo answers those questions.

---

## 2. What Worked Locally

- The model was trained locally on macOS using **Python 3.12**
- fastai training and inference worked as expected
- `learn.export("model.pkl")` completed successfully
- A local Gradio app (`app.py`) ran without issues on `localhost:7860`

At this stage, everything *appeared* correct — which is often misleading.

---

## 3. What Broke on Kaggle (NumPy 2.x + `pip -U`)

The first failure happened when the notebook was imported into Kaggle.

### What went wrong
- The first notebook cell used `pip -U`
- This upgraded NumPy to **2.x**
- fastai (and compiled dependencies) were built against NumPy 1.x
- Result: cryptic runtime errors

### Key realization
**Blind upgrades (`pip -U`) are dangerous in ML environments.**

### Fix
Pin versions explicitly:

```bash
!pip -q install "numpy<2" "fastai==2.8.5" "ddgs"
```

Once versions were pinned, the notebook worked again.

---

## 4. What Broke on Hugging Face (Python 3.10 vs 3.12 Pickle)

The next major failure happened during deployment to Hugging Face Spaces.

### What went wrong
- Hugging Face Spaces default to **Python 3.10**
- The model was exported using **Python 3.12**
- `model.pkl` is a pickle that embeds Python code objects
- Resulting error:
  ```
  TypeError: code expected at most 16 arguments, got 18
  ```

### Root cause
Pickled models are **not portable across Python minor versions**.

### Fix
Explicitly set the Python version in the Space `README.md`:

```yaml
python_version: 3.12
```

After this change, the model loaded correctly.

---

## 5. What Broke in Gradio (API Drift)

The tutorial being followed used **deprecated Gradio APIs**.

### What broke
- `gr.inputs.Image`
- `gr.outputs.Label`

These APIs no longer exist in modern Gradio.

### Fix
Update to the new API:

```python
gr.Image(type="filepath")
gr.Label(num_top_classes=3)
```

This is a reminder that **deployment tutorials age quickly**.

---

## 6. Git Gymnastics on Hugging Face (Auth + Large Files)

Several Git-related issues surfaced during deployment.

### Authentication
- Hugging Face no longer allows password-based Git auth
- A **Personal Access Token (PAT)** is required

### Binary files
- `.pkl` and `.jpg` files are considered binaries
- Direct pushes are rejected

### Fix
Use Git LFS:

```bash
git lfs install
git lfs track "*.pkl"
git lfs track "*.jpg"
git add .gitattributes
git commit -m "Track model and assets with git-lfs"
```

This creates lightweight pointers instead of pushing raw binaries.

---

## 7. Final Working Configuration (Key Snippets)

### Space `README.md`
```yaml
sdk: gradio
python_version: 3.12
```

### Model loading (CPU-safe)
```python
learn = load_learner("model_resnet18.pkl", cpu=True)
```

### Gradio launch
```python
gr.Interface(...).launch()
```

(No `share=True` needed on Hugging Face.)

---

## 8. Repeatable Deployment Checklist

- [ ] Pin NumPy (`numpy<2`)
- [ ] Pin fastai and Gradio versions
- [ ] Avoid `pip -U` in notebooks
- [ ] Export model using the same Python version as deployment
- [ ] Set `python_version` explicitly in HF Space README
- [ ] Update Gradio APIs to current syntax
- [ ] Use PAT for Hugging Face Git auth
- [ ] Track binaries with Git LFS
- [ ] Check **Build logs** before **Container logs**
- [ ] Add startup prints when debugging deployments

---

## Final Reflection

This journey reinforced a key lesson:

> **“Works locally” does not mean “ready for deployment.”**

Deployment is where assumptions surface, and where real engineering begins.

## Who This Is For

- fastai learners moving beyond notebooks
- anyone deploying pickled ML models
- engineers new to Hugging Face Spaces