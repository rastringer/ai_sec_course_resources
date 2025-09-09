# Module 3

In this module, we will consider the notion of AI safety and how it relates to security. 

We can distinguish between technical vulnerabilities and intentional malicious attacks. Typically, technical vulnerabilities such as hallucinations, scheming or misunderstandings can be due to model's development and shortcommings of our ability to evaluate with care how the model is likely to behave. Technical vulnerabilities can be harmful to users, and can also provide fertile ground for intentional malicious attacks. 

For example, an LLM which isn't sufficiently cautious about personally identifiable information may be suceptible to data theft or other extraction attacks. AI safety and security are fields with strong interplay.

### AI safety research

AI safety, or alignment, is a burgeoning field of research and there are plentiful resources to develop an understanding of the field. Some resources worth consuming for an overview include:

* Intro to AI Safety ([talk](https://www.youtube.com/watch?v=pYXy-A4siMw&t=16s))
* How we could stumble into AI catastrophe ([article](https://www.cold-takes.com/how-we-could-stumble-into-ai-catastrophe/)) by Holden Karnofsky

For those interested in an extensive exploration of AI Alignment, I suggest Blue Dot Impact's [course](https://bluedot.org/courses/alignment). In our modules, we will consider the practical steps we can implement in our projects and deployments without an exhaustive coverage of the research field.

### Evaluations

Evaluations are crucial for large model-powered applications, especially in the pre-deployment phase. Since our models are extremely powerful and non-deterministic, it is far harder to predict their behaviour than in traditional programs that follow hard-coded logic. A rough evaluation process may include:

#### Evaluation on competency and accuracy for the task

Organizations get subject matter experts together to create evaluation datasets of questions and gold-standard answers to assess model performance. 

#### Safety evaluations

To evaluate beyond performance and check for potentially damaging behaviour, we need to think imaginatively to stress test the model and see how it responds. The most dangerous behaviour may be one we haven't thought to screen for. 

### Common research directions for evaluations

* Power-seeking and resource acquisition - assess whether systems try to acquire computational resources or have broader tendencies to seek influence, control, or self-preservation that could lead to problematic behavior.
* Deception and manipulation - Testing whether AI systems engage in dishonest behavior, hide their true capabilities, or manipulate humans to achieve their goals.
* Goal misgeneralization - Evaluating whether systems pursue their training objectives in unintended ways when deployed in new contexts, potentially causing harm while technically following their instructions.
* Situational awareness - Assessing whether AI systems understand they are AI systems, their training process, and their deployment context - which could influence how they behave strategically.
* Alignment robustness - Testing whether helpful, harmless behavior persists under pressure, adversarial inputs, or when systems have more capability or autonomy.
* Coordination and scheming - Evaluating whether multiple AI systems might coordinate in problematic ways, or whether single systems engage in long-term planning that could be harmful.
* Capability overhang - Measuring gaps between what systems can do versus what we can reliably control or understand about their behavior.
* Truthfulness and calibration - Testing whether systems provide accurate information and properly express uncertainty about their knowledge.


## Further discussion of AI safety / alignment etc

[AI tools used by English councils downplay women's health issues, study finds](https://uk.finance.yahoo.com/news/ai-tools-used-english-councils-050042574.html) 
