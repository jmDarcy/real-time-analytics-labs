# Unstructured Data Notes

## Core Idea

Unstructured data must be represented numerically before analytics or machine learning can use it.

Examples:

- image -> pixels -> tensor -> embedding or class probabilities,
- text -> tokens -> vector -> embedding or class probabilities,
- audio -> waveform -> spectrogram -> tensor.

## Real-Time Analytics Pipeline

```text
raw event
-> decode media or text
-> convert to tensor/vector
-> model inference
-> business decision
-> persist result for audit
```

## Images

An image can be represented as:

- grayscale tensor with shape `(height, width)`,
- RGB tensor with shape `(height, width, channels)`,
- batch tensor with shape `(batch, height, width, channels)` or framework-specific variants.

The tensor values are often normalized, for example from integer pixel values `0..255` to floating-point values `0..1`.

## Text

Text has to be tokenized. A minimal representation can count words, but modern models usually use subword tokenizers and embeddings.

Simple representation:

```text
"fraud detected in transaction"
-> ["fraud", "detected", "in", "transaction"]
-> vector of token counts
```

Modern representation:

```text
text
-> tokenizer
-> token IDs
-> pretrained language model
-> embedding or predicted label
```

## Pretrained Models

Pretrained models are useful because images and text usually require large datasets to learn useful representations. In a lab setting, they can be discussed as a model-serving component even when the runnable example avoids external downloads.

In production, the key questions are latency, throughput, model size, monitoring, and whether inference should run synchronously in the request path or asynchronously in a streaming pipeline.
