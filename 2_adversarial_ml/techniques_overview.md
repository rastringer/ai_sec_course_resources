# Adversarial ML

Attacking ML models, data pipelines and deployments is a vast, exciting and unique field. We will explore some ways in which ML systems can be vulnerable before looking at how to approach red teaming and security for AI. While adversarial ML examples and results certainly eye-catching, we should bear in mind that the entire system in which AI is deployed should be evaluated for security. Both traditional offensive security methods (gaining unwarranted access to and priviledges in a system) and ML-specific attacks should be considered when evaluating the security of AI applications.

## Attacking Models

* Evasion: Since models are typically non-deterministic, there is scope for what are broadly called 'evasion attacks'. This means we feed modified inputs at inference time to fool deployed models. We will cover some examples of this attack vector shortly. This image may look familiar to anyone interested in adversarial ML:

<img src="https://github.com/rastringer/ai_sec_course_resources/blob/main/2_adversarial_ml/images/panda_gibbon.png?raw=true" width="600" alt="Panda-Gibbon Image">

Image from *[Explaining and Harnessing Adversarial Examples](https://arxiv.org/pdf/1412.6572)*, by Goodfellow, Shlens & Szegedy.

* Extraction: attackers can steal proprietary models through strategically quering deployments with specific, iterative inputs to elicit the weights, decision boundaries and other tendencies of the model. This can mean theft of intellectual property, and also allows attackers to use the stolen model to craft further attacks.

## Attacking Data Pipelines

As we have seen, data is the nourishment upon which AI models feast, and its quality affects theirs. 

* Poisoning attacks: corrupting data (eg by mislabeled examples) can affect model behaviour. Even changing a few data samples can propagate through the network and have an outsized affect on model outputs.

* Proprietary data theft: a general security issue rather than specifically ML-related. However, the theft of high-quality, unique and private datasets could represent significant intellectual property loss.

## Membership Inference

Determining whether specific data points were used in training can yield privacy concerns. 

## Unique technical challenges

Adversarial ML presents some compelling challenges:

* Transferability: several studies have shown a high degree of transferance, which means that an attack working on one model stands a good chance of working on another.

    * This has several implications: proprietary models may be vulnerable to attacks developed using open source model. This also means that when defending ML models, generating and training on adversarial examples using surrogate models can help approximate and defend against attacks. More on adversarial training and mitigations soon.
      
* Robustness-accuracy tradeoff: some defence mechanisms can reduce model performance on clean inputs. Whereas traditional security focuses on finding and patching vulnerabilities, it can be costly to make models more robust, and affect model expressivity.  

### White box, black box attacks

We can broadly separate adversarial attacks into two types: white box and black box, or permissioned and unpermissioned. White box means we have access to the model weights; in a black box scenario, we don't have direct access to the model but can elicit its predictions from an API or another exposure.

### Readings

I recommend skimming through these papers to get an understanding of the landscape and some of the more colourful attack demonstrations. Some have github repos worth taking a look at also.


[Universal adversarial pertubations](https://arxiv.org/pdf/1610.08401)

[Making an Invisibility Cloak: Real World Adversarial Attacks on Object Detectors](https://arxiv.org/pdf/1910.14667)

[Universal and transferable adversarial attacks on aligned language models](https://llm-attacks.org/)

[Adversarial Toolkit](https://github.com/Trusted-AI/adversarial-robustness-toolbox/tree/main/notebooks)

[Adversarial Examples in Modern Machine Learning: A Review](https://arxiv.org/pdf/1911.05268)