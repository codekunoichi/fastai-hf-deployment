# Troubleshooting Guide (fastai → Hugging Face Deployment)

This document captures common failure modes encountered when moving from a local fastai notebook to a deployed application on Hugging Face Spaces, along with their root causes and fixes.

Each item follows a **symptom → cause → fix** pattern.

---

1. **Space stuck on “Building” or “Pushing image”**
   - **Cause:** Large dependency layers (torch, gradio), Hugging Face infra lag, or cached Docker layers
   - **Fix:** Be patient and refresh; slim down `requirements.txt`; push a small commit to retrigger the build; scan the *Build* logs for early `ERROR` lines

2. **Build logs show success, but Space UI still says “Building”**
   - **Cause:** UI lag while the container is transitioning to runtime
   - **Fix:** Check *Container* logs for `===== Application Startup =====`; refresh the Space page

3. **Error: `TypeError: code expected at most 16 arguments, got 18`**
   - **Cause:** Python version mismatch (model exported on Python 3.12, Space running Python 3.10)
   - **Fix:** Set `python_version: 3.12` explicitly in the Space `README.md`, or re-export the model using the deployment Python version

4. **Error: `AttributeError: module 'gradio' has no attribute 'inputs'`**
   - **Cause:** Outdated tutorial code using deprecated Gradio APIs (`gr.inputs.*`, `gr.outputs.*`)
   - **Fix:** Update to modern Gradio components, e.g. `gr.Image()` and `gr.Label()`

5. **Crash on Kaggle/Colab: “module compiled using NumPy 1.x cannot run in NumPy 2.x”**
   - **Cause:** NumPy 2.x installed while compiled dependencies expect NumPy 1.x
   - **Fix:** Pin NumPy explicitly (`numpy<2`), avoid `pip -U`, and restart the kernel after installation

6. **pip warning: “dependency resolver does not currently take into account…”**
   - **Cause:** Mixing environment-pinned packages with forced upgrades
   - **Fix:** Remove `-U`; pin versions explicitly; install dependencies once at the top of the notebook; restart kernel

7. **Git push to Hugging Face fails authentication**
   - **Cause:** Hugging Face no longer supports password-based Git authentication
   - **Fix:** Use a Hugging Face Personal Access Token (PAT) as the Git password; store it via the system credential helper

8. **Push rejected: “contains binary files” / “offending files: model.pkl, .jpg”**
   - **Cause:** Large binary files pushed without Git LFS/Xet tracking
   - **Fix:** Track binaries with Git LFS (`*.pkl`, `*.jpg`); commit `.gitattributes`; re-add files; migrate history if already committed

9. **`FileNotFoundError` when calling `load_learner()` locally**
   - **Cause:** Incorrect working directory or undefined path variable
   - **Fix:** Use relative paths (`load_learner("model.pkl")`) or confirm working directory with `os.getcwd()` / `Path.cwd()`

10. **Incorrect probability display (prediction correct, probability shows 0.0000)**
    - **Cause:** Incorrect indexing into `probs` assuming a fixed class order
    - **Fix:** Map probabilities to labels explicitly using `learn.dls.vocab` or index via `pred_idx`

---

If you encounter a new failure mode, add it here with the same **symptom → cause → fix** structure so this document continues to evolve as a practical deployment reference.
