# AudioMCQ: Audio Multiple-Choice Question Dataset

**Official repository for the paper "Measuring Audio's Impact on Correctness: Audio-Contribution-Aware Post-Training of Large Audio Language Models"**

<div align="center">

[![arXiv](https://img.shields.io/badge/arXiv-2509.21060-b31b1b.svg)](https://arxiv.org/abs/2509.21060)
[![Dataset](https://img.shields.io/badge/🤗%20Dataset-AudioMCQ-yellow)](https://huggingface.co/datasets/inclusionAI/AudioMCQ)
[![DCASE 2025](https://img.shields.io/badge/DCASE%202025-1st%20Place-gold.svg)](https://dcase.community/challenge2025/task-audio-question-answering-results)

</div>

## Quick Links

- **Dataset**: [https://huggingface.co/datasets/inclusionAI/AudioMCQ](https://huggingface.co/datasets/inclusionAI/AudioMCQ)
- **Paper**: [https://arxiv.org/abs/2509.21060](https://arxiv.org/abs/2509.21060)
- **DCASE 2025 Challenge**: [1st Place Results](https://dcase.community/challenge2025/task-audio-question-answering-results)

## Overview

AudioMCQ is a comprehensive audio multiple-choice question dataset with **571k samples** designed for post-training Large Audio Language Models (LALMs). The dataset features dual chain-of-thought annotations and audio-contribution filtering, achieving state-of-the-art results in audio understanding tasks.

### Key Highlights

- **571k high-quality samples** across sound, music, speech, and temporal domains
- **Dual CoT annotations**: Structured and unstructured reasoning paths
- **Audio-Contribution filtering**: Weak (54.8%) and strong (45.2%) splits
- **DCASE 2025 Challenge**: 1st place winner
- **Pre-trained models available**: Weak-to-Strong and Mixed-to-Strong paradigms

## Dataset Access

**For complete dataset information, statistics, data format, and download instructions, please visit:**

### [Hugging Face Dataset Repository](https://huggingface.co/datasets/inclusionAI/AudioMCQ)

The Hugging Face repository contains:
- Full dataset documentation
- Detailed statistics and examples
- Data format specifications
- Download links for audio files
- Usage instructions
- Model checkpoints

## Model Checkpoints

We provide trained model checkpoints for two post-training paradigms:

| Training Paradigm | Hugging Face Link |
| :--- | :--- |
| **Weak-to-Strong** | [inclusionAI/AudioMCQ-Weak-To-Strong](https://huggingface.co/inclusionAI/AudioMCQ-Weak-To-Strong) |
| **Mixed-to-Strong** | [inclusionAI/AudioMCQ-Mixed-To-Strong](https://huggingface.co/inclusionAI/AudioMCQ-Mixed-To-Strong) |

## Training Scripts

All training code used for this project can be found in the `/training_scripts` directory.

## News

- **[2025.09]** Paper published on arXiv
- **[2025.09]** AudioMCQ dataset released with 571k samples
- **[2025.07]** Achieved 1st place in DCASE 2025 Audio-Question-Answering challenge

## Contact

- **Haolin He**: [harlandzzc@link.cuhk.edu.hk](mailto:harlandzzc@link.cuhk.edu.hk)

## Citation

If you find AudioMCQ useful in your research, please cite:
```bibtex
@article{he2025audiomcq,
  title={Measuring Audio's Impact on Correctness: Audio-Contribution-Aware Post-Training of Large Audio Language Models},
  author={He, Haolin and others},
  journal={arXiv preprint arXiv:2509.21060},
  year={2025}
}
```

## Acknowledgements

We thank the organizers of DCASE 2025 and the research community for their valuable feedback and support.

## Related Resources

- [Qwen2.5-Omni](https://github.com/QwenLM/Qwen2.5-Omni)
- [DCASE 2025 Challenge](http://dcase.community/challenge2025/)
- [R1-AQA Evaluation Format](https://github.com/xiaomi-research/r1-aqa)