Time: 1-2 hrs

Choose one:

Explore either our nanoGPT or try the HuggingFace Transformers [library](https://huggingface.co/docs/transformers/en/index) with the Tiny Stories [dataset](https://huggingface.co/datasets/roneneldan/TinyStories). Either train the nanoGPT on the dataset and evaluate the quality of its generation, or use HuggingFace to load a small model (eg GPT-2) and fine tune it on the dataset. There are also [evaluation prompts](https://huggingface.co/datasets/roneneldan/TinyStories/blob/main/Evaluation%20prompts.yaml) provided for testing models trained on Tiny Stories.

Evaluations: which AI safety topics seemed interesting to you? Try to implement an evaluation using the Inspect AI library with either OpenAI or Anthtropic API or Ollama models. Some suggestions:
* Truthfulness and hallucination detection (find or create a dataset of verifiable facts)
* Harmful content generation and refusal training: how consistent is the model at refusing to generate dangerous or hateful text?
* Sycophancy and truth-seeking: is the model telling us what we want to read, rather than that which is true?