import gradio as gr
from fastai.vision.all import *
import sys

print("Python:", sys.version)

learn = load_learner("model_resnet18.pkl", cpu=True)
labels = learn.dls.vocab

def predict(img):
    img = PILImage.create(img)
    pred, pred_idx, probs = learn.predict(img)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}

gr.Interface(
    fn=predict,
    inputs=gr.Image(type="filepath"),
    outputs=gr.Label(num_top_classes=3),
    title="Bear Detector Classifier",
    description="fastai bear classifier demo",
    examples=["grizzly.jpg"],
).launch()