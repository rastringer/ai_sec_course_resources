# LLMs

Now that we have covered the principles, practice and some of the security considerations of machine learning, we move onto the big league of large language models, or LLMs.

LLMs emerged with the runaway popularity of ChatGPT and a host of competing applications and underlying models capable of a variety of language modelling tasks, from classification to sentiment analysis and text generation. We now also have large multi-modal models, capable of interpreting and responding to images, text and sound.

In this module, we will build and understanding of how LLMs are created, before we turn our attention in the next module to their safety and security risks.

### Enter the Transformer

In 2017, researchers published the now iconic "Attention Is All You Need" [paper](https://arxiv.org/pdf/1706.03762). 

Prior to the transfomer architecture, language modelling was limited by constraints inherent in recurrent models such as RNNs (recurrent neural networks) and LSTMs (long short-term memory). These constraints included:
* Processing text sequentially, word by word, which caused bottlenecks and inhibited learning long-range depencencies. This is also called the 'vanishing gradients' problem that manifests over long sequences.
  * For example, the model may not correlate effectively a dog mentioned in the first paragraph and the sound of barking outside in the fifth

Transformers attended to all positions in a sequence through *attention*, or *self-attention*, which allowed for better long-range understanding, more efficient training and better modelling of complex linguistic relationships. The architecture enabled:
* Improved performance on language tasks
* Faster training times due to parallelization
* The foundation for large language models

In the following notebook, we will examine:
* Attention and how it fits into the broader transformer architecture
* How LLMs are trained

### Attention

Here's a quick overview of attention:

In attention, or self-attention, we compute weighted relationships between all positions of a text (or other inputs, such as images) simultaneously. Words are tokenized and each token calculates how relevant each other token in the text is to the current one. We use 'keys', 'queries' and 'values' to accomplish this. For example, when processing the word "woke" in the sentence

"The cat that was sleeping on the mat woke up"

the *query* "woke" compares itself to all *keys* ("the", "cat", "was" etc) and finds a high similarity with "cat" since it is the subject of the verb. It then retrieves the corresponding *value* representation of "cat" to incorporate into the updated representation of "woke".

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Multi-head attention runs multiple attention mechanisms in parallel, allowing the model to compute different types of relationships and representations simultaneously. This information is then combined and processed through feed-forward layers to produce the final output.

Masked, or causal self-attention prevents tokens from looking at future tokens in a sequence. This ensures when generating text, each token can only use information from itself and previous tokens. This is key for autoregressive language models that generate a token at a time during inference. This is specifically designed for and used by models such as GPT et al.
$$\text{MaskedAttention}(Q, K, V, M) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}} + M\right)V$$

### Encoders and Decoders

Encoder-Decoder (examples include original Transformer, T5, BART):

* Encoder processes input sequence
* Decoder generates output sequence
* Used for translation, summarization


Encoder-Only (such as BERT):

* Only encoder stack
* Good for classification, understanding tasks


Decoder-Only (GPT, nanoGPT):

* Only decoder stack
* Autoregressive generation
* Good for text generation, completion

## Safety Considerations

LLMs are powerful and ever-larger models that have digested vast training datasets and that have been extensively 'tuned' (mostly) by human moderators. Their outputs are non-deterministic and their knowledge is vast -- they're a powerful tool which must be evaluated extensively and carefully, before being exposed to users. Some fields of safety research concern:

### Alignment 

* How closely is the model trained and deployed to satisfy the task at hand? How will the model accomplish its tasks? Optimizing for certain metrics may lead to unintended behaviour by the model to satisfy its evaluators and users.

### Harmful content generation
* LLMs have vast knowledge and subtle or even naive manipulations can lead to harmful outputs.

### Bias and discrimination
* Models can amplify prejudices present in training data and in human evaluators tasked with improving the responses of the base model. See *[On the Dangers of Stochastic Parrots](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)* by Bender, Gebru, McMillan-Major and Shmitchell.

### Misinformation and Hallucination
* LLMs can generate false information and present it with confidence.

### Manipulation and deception
* Since machine learning is training a model to complete a task, the model often devises ways of fulfilling its goals that were unimagined by its programmers. [This](https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/) Deepmind paper shows the example of gaming agents using unique behaviour to achieve fulfill their reward functions.

## Security Considerations

LLMs pose a host of security considerations. 

### Prompt injection and jailbreaking
* LLMs can be manipulated by careful prompts and patterns to ignore its safety filters or original instructions, and output restricted data or potentially harmful content. LLMs are also susceptible to *indirect* prompt injection, whereby instructions (for example, a SQL query) are embedded in a textual or visual input to a model, which are then executed.

### Data poisoning
* Since LLMs are trained on swathes of the internet, there is significant scope for strategically placing poisoned content online which then gets pulled into training data. This is also a general quality control problem; should LLMs consider ALL content of equal value?

### Data extraction and memorization
* LLMs can memorize and reproduce sensitive training data. They are also often used in conjunction with an organization's data (having the LLM refer to a database to inform its answers), this is a process known as Retrieval Augmented Generation (RAG) and can lead to sensitive data leaks.

### Adversarial examples
* Similar to attacks we learned about in module 2, attackers can craft specific inputs to change how LLMs behave. See the [llm attacks](https://llm-attacks.org/) paper for more details.

### Pipeline / supply chain vulnerabilities
* As we saw in module 2, security the data pipeline is crucial. This is yet more important for LLMs, whose training cycles, adaption, fine-tuning and deployments that often include access to data, present numerous attack vectors.

### Emergent capabilities
* Not finding a vulnerability or misbehaviour does not mean there aren't any. LLM abilities are still not entirely understood, and their reasoning and behaviour are still the subject of much research. It is difficult to predict and evalutate all risks; ongoing processes are necessary.

### Resources

We will cover transformers and attention in the next notebook. For more exploration, see the 
How Transformer LLMs Work [course](https://www.deeplearning.ai/short-courses/how-transformer-llms-work/) by Jay Alammar and Maarten Grootendorst

For more on AI safety / alignment, see BlueDot Impact's [courses](https://bluedot.org/).
