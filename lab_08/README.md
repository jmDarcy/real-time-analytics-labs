# Lab 08: Unstructured Data, Tensors, Images, Text, and Pretrained Models

This lab extends the course sequence with the RTA2026 Lab 8 theme: unstructured data and how it becomes usable for modelling. The examples focus on images, text, tensors, and the role of pretrained models.

Reference course material:

<https://sebkaz-teaching.github.io/RTA2026/>

## Learning Goals

- Explain why images and text are not directly tabular.
- Convert a small synthetic image into a tensor-like numerical array.
- Convert text into simple numerical features.
- Understand where pretrained models fit in real-time analytics pipelines.
- Keep inference examples lightweight and reproducible without external downloads.

## Files

| File | Purpose |
| --- | --- |
| `unstructured_data_notes.md` | Conceptual notes aligned with the Lab 8 topic. |
| `image_text_tensor_demo.py` | Self-contained image/text representation demo using NumPy and standard Python. |

## Suggested Run

From this folder:

```bash
python image_text_tensor_demo.py
```

The script prints:

- a synthetic grayscale image matrix,
- normalized tensor values,
- simple image features,
- token counts and text-vector features.

## Discussion Prompt

Real-time analytics with unstructured data usually has an additional representation step. A camera frame, document, or customer message must be transformed into vectors before a model or business rule can act on it.
