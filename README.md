# 🩺 AI Medical Chatbot

> An intelligent, responsive medical assistant built with **Gradio**, **LangChain**, and **RAG (Retrieval-Augmented Generation)** — featuring a beautiful, modern UI inspired by healthcare themes.

---

## 🌟 Overview

The **AI Medical Chatbot** helps users with **symptom guidance**, **medicine lookup**, **first aid advice**, and **stock availability** queries.
It uses **Retrieval-Augmented Generation (RAG)** to provide context-aware, reliable medical answers while maintaining an elegant and modern conversational interface.

This chatbot seamlessly blends **intelligence** with **aesthetic design**, ensuring a pleasant, informative user experience.

---

## 🎨 UI Design Highlights

✨ **Modern Gradient UI** – Inspired by [Dribbble AI chatbot designs](https://dribbble.com/shots/25640525-Mobile-AI-Chatbot), featuring soft pink gradients (`#FFE5EC → #FB6F92`).
🧠 **Context Awareness** – Displays the retrieved medical database context before giving the AI response.
💬 **Animated Chat Flow** – Smooth transitions, emojis, and hover effects for an engaging chat experience.
🌙 **Warm, Approachable Design** – Friendly palette that remains professional, with no stark white backgrounds.

### 🎨 Color Palette Used

```
#FFE5EC | #FFC2D1 | #FFB3C6 | #FF8FAB | #FB6F92
```

---

## ⚙️ Key Features

* 🧠 **RAG-based Question Answering** for accurate and contextual responses
* 💬 **Interactive Gradio Interface** with modern animations and gradient backgrounds
* 🩹 **First Aid and Medicine Guidance**
* 📦 **Medicine Stock & Dosage Information**
* 🔒 **Safe and Informative Responses** (non-diagnostic medical guidance)
* 🎨 **Fully Customizable Theme** powered by CSS and Coolors Palette

---

## 🏗️ Project Structure

```
📂 AI-Medical-Chatbot/
│
├── app.py                        # Core backend logic – RAG chain and embeddings  
├── gradio_medical_chatbot.py     # Gradio UI with animations and CSS  
├── requirements.txt              # Dependencies list  
├── data/                         # Medical dataset (CSV or JSON)  
└── README.md                     # Project documentation (this file)  
```

---

## 📥 Datasets Used

1. **Medicine Dataset** – from Kaggle: [Medicine Dataset – Kaggle](https://www.kaggle.com/datasets/ujjwalaggarwal402/medicine-dataset)
   A comprehensive synthetic dataset of medicines containing 50,000 unique entries. ([Kaggle][1])

2. **Your custom medical database** – stored in `data/`, used for retrieval context in the RAG chain.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/ai-medical-chatbot.git  
cd ai-medical-chatbot
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Chatbot

```bash
python gradio_medical_chatbot.py
```

Your chatbot will launch locally (or use `share=True` for a public link).

---

## 🧩 Technologies Used

| Component      | Technology                       |
| -------------- | -------------------------------- |
| 🧠 LLM Backend | LangChain + Ollama / OpenAI      |
| 💬 Frontend    | Gradio (custom CSS + animations) |
| 🗂️ Database   | Chroma Vector Store              |
| ⚡ Embeddings   | OllamaEmbeddings                 |
| 🧰 Language    | Python 3.10+                     |

---

## 💬 Example Interaction

```
🧠 Context (medical database summary):
Medicine Name: Burnol
Generic Name: Aminacrine Hydrochloride
Use Case: Treatment of minor burns and cuts
Dosage Form: Ointment
Stock: 18

💬 Question:
What should I do for a mild burn?

✅ Helpful Answer:
Clean the area gently with cool water, apply Burnol or any soothing burn ointment,
and cover it with sterile gauze. If the burn covers a large area or blisters form,
consult a healthcare professional.
```

---

## 📸 UI Preview

*(Insert screenshot here, e.g. `assets/ui_preview.png`)*

🔗 **Live Demo:** [https://your-gradio-link.gradio.live](https://your-gradio-link.gradio.live)

---

## 📜 Disclaimer

> This chatbot is intended for **educational and informational purposes only**.
> It does **not** provide a medical diagnosis or replace professional medical advice.
> Always consult a licensed healthcare provider for medical concerns.

---

## 🤝 Contributors

* 👩‍💻 **Sahithi,Tanmayi** — Developer & Designer
* 🤖 **AI Assistant** — Backend & UI Design Support

---

## ❤️ Acknowledgements

* [Gradio](https://gradio.app/)
* [LangChain](https://www.langchain.com/)
* [Coolors Palette Generator](https://coolors.co/)
* [Dribbble UI Inspiration](https://dribbble.com/shots/25640525-Mobile-AI-Chatbot)
* [Medicine Dataset on Kaggle](https://www.kaggle.com/datasets/ujjwalaggarwal402/medicine-dataset)

---
> 🩷 “Empowering healthcare awareness through AI — beautifully and responsibly.”
---

