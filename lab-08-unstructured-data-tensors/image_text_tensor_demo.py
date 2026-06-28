"""Unstructured data representation demo.

The example avoids external downloads and large pretrained models. It shows the
representation step that normally happens before model inference in Lab 8-style
workflows: images and text become numerical arrays.

Run:
    python image_text_tensor_demo.py
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class TextVector:
    vocabulary: list[str]
    counts: list[int]


def synthetic_image() -> np.ndarray:
    """Create a tiny grayscale image with a bright diagonal pattern."""
    image = np.zeros((8, 8), dtype=np.uint8)
    for idx in range(8):
        image[idx, idx] = 255
        if idx + 1 < 8:
            image[idx, idx + 1] = 120
    return image


def image_features(image: np.ndarray) -> dict[str, float]:
    tensor = image.astype("float32") / 255.0
    return {
        "height": float(tensor.shape[0]),
        "width": float(tensor.shape[1]),
        "mean_intensity": float(tensor.mean()),
        "max_intensity": float(tensor.max()),
        "nonzero_pixel_ratio": float(np.count_nonzero(tensor) / tensor.size),
    }


def tokenize(text: str) -> list[str]:
    cleaned = "".join(ch.lower() if ch.isalnum() else " " for ch in text)
    return [token for token in cleaned.split() if token]


def vectorize_text(texts: list[str]) -> list[TextVector]:
    vocabulary = sorted({token for text in texts for token in tokenize(text)})
    vectors = []
    for text in texts:
        counts = Counter(tokenize(text))
        vectors.append(TextVector(vocabulary=vocabulary, counts=[counts[token] for token in vocabulary]))
    return vectors


def main() -> None:
    image = synthetic_image()
    tensor = image.astype("float32") / 255.0
    print("Synthetic grayscale image:")
    print(image)
    print("\nNormalized tensor:")
    print(np.round(tensor, 2))
    print("\nImage features:")
    print(image_features(image))

    texts = [
        "fraud alert transaction amount high",
        "normal transaction approved",
        "customer message requests transaction review",
    ]
    vectors = vectorize_text(texts)
    print("\nText vectors:")
    for text, vector in zip(texts, vectors):
        print({"text": text, "vocabulary": vector.vocabulary, "counts": vector.counts})


if __name__ == "__main__":
    main()
