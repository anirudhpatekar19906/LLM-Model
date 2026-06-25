# LLM Model - Custom GPT Implementation

This project is a from-scratch implementation of a Generative Pre-trained Transformer (GPT) language model using PyTorch. The model is designed to learn from and generate text based on educational content about neural networks and deep learning.

## 🚀 Features

- **Transformer Architecture**: Implements a full GPT-style transformer including:
  - **Multi-head Causal Self-Attention**: Optimized using PyTorch's `scaled_dot_product_attention` with fused QKV projections.
  - **Feed-Forward Network (FFN)**: Features GELU activation and residual connections.
  - **Pre-Layer Normalization**: Uses Pre-LN blocks for improved training stability.
  - **Causal Masking**: Ensures the model only attends to previous tokens during training.
- **Custom Dataset**: Includes a scraping utility (`dataset.py`) to collect text from the "Neural Networks and Deep Learning" book by Michael Nielsen.
- **Text Generation**: Supports flexible text generation with:
  - **Temperature Control**: Adjusts the randomness of the output.
  - **Top-k Sampling**: Limits the vocabulary to the top $k$ most likely tokens to improve coherence.
- **Weight Tying**: Implements weight tying between the token embedding table and the final linear head.

## 📂 Project Structure

- `model_brain.py`: The core implementation of the `GPTLanguageModel` and its components (Attention, Block, FeedForward).
- `dataset.py`: A utility script to scrape the training data into `full_book.txt`.
- `requirements.txt`: List of required Python packages for the project.
- `bigram.ipynb`, `gpt_model.ipynb`, `New_Model.ipynb`: Jupyter notebooks used for model experimentation, training, and evaluation.
- `vocab.txt`: Stores the vocabulary used for tokenization.
- `full_book.txt`: The raw text dataset used for training.

## 🛠️ Getting Started

### Prerequisites
- Python 3.10+
- PyTorch

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd "LLM Model"
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Data Collection
Run the scraping script to generate the training dataset:
```bash
python dataset.py
```
This will create `full_book.txt` containing the text from all chapters of the target book.

### Model Training & Usage
Open the provided Jupyter notebooks (`gpt_model.ipynb` or `New_Model.ipynb`) to train the model and generate text.

## ⚙️ Hyperparameters

The current model configuration in `model_brain.py` uses the following settings:

| Hyperparameter | Value | Description |
| :--- | :--- | :--- |
| `n_embd` | 384 | Dimensionality of token and position embeddings |
| `n_head` | 4 | Number of attention heads |
| `n_layer` | 6 | Number of transformer blocks |
| `block_size` | 128 | Maximum sequence length (context window) |
| `dropout` | 0.3 | Dropout rate for regularization |

## 👤 Author
**Anirudhpatekar**  
GitHub: [@anirudhpatekar19906](https://github.com/anirudhpatekar19906)

## 📜 License
This project is developed for educational purposes. it is open for anyone to use, modify, and build upon freely.
