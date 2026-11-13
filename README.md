# Image_to_video_Pika-H3-Flex
                        

# 🐱 Image-to-Video Generation with Hugging Face

This project demonstrates how to use the **Hugging Face Inference Client** to turn an image into a video using an AI model.

In this example, a picture of a cat is used as the starting image, and the AI is instructed to make the cat dance.

## 🚀 Requirements

Before running the code, make sure you have:

- Python 3.8 or newer
- A Hugging Face account
- A Hugging Face API token
- An input image named `cat.png`

---

## 📦 Install Dependencies

Install the Hugging Face Hub library:

```bash
pip install -U huggingface_hub
```

---

## 🔑 Set Up Your Hugging Face Token

You need a Hugging Face access token to use the API.

Create a token from your Hugging Face account and set it as an environment variable named `HF_TOKEN`.

### Windows PowerShell

```powershell
$env:HF_TOKEN="your_huggingface_token_here"
```

### Windows Command Prompt

```cmd
set HF_TOKEN=your_huggingface_token_here
```

### macOS/Linux

```bash
export HF_TOKEN="your_huggingface_token_here"
```

> ⚠️ **Important:** Never upload your Hugging Face token directly to GitHub.

---

## 📁 Project Structure

Your project folder should look like this:

```text
your-project/
│
├── app.py
├── cat.png
└── README.md
```

- `app.py` contains the Python code.
- `cat.png` is the image you want to animate.
- `README.md` contains the project instructions.

---

## 💻 Python Code

Create a file called `app.py` and add the following code:

```python
import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="wavespeed",
    api_key=os.environ["HF_TOKEN"],
)

with open("cat.png", "rb") as image_file:
    input_image = image_file.read()

video = client.image_to_video(
    input_image,
    prompt="The cat starts to dance",
    model="Pika-Labs/Pika-H3-Flex",
)
```

---

## ▶️ Run the Program

Make sure your Hugging Face token is set and your `cat.png` image is in the same folder as your Python script.

Then run:

```bash
python app.py
```

The program will:

1. Connect to the Hugging Face Inference API.
2. Use the `wavespeed` provider.
3. Load the `cat.png` image.
4. Send the image to the AI model.
5. Use the prompt:

```text
The cat starts to dance
```

6. Generate a video based on the image and prompt.

---

## 🎨 Changing the Animation

You can change the prompt to create different animations.

For example:

```python
prompt="The cat starts running through a beautiful forest"
```

Or:

```python
prompt="The cat is flying through space"
```

Or:

```python
prompt="The cat slowly turns into a superhero"
```

The prompt tells the AI how you want the image to move and animate.

---

## 🖼️ Using Your Own Image

To use a different image, replace:

```text
cat.png
```

with your own image.

For example:

```python
with open("my_image.png", "rb") as image_file:
    input_image = image_file.read()
```

Make sure the image file is located in the same directory as your Python script.

---

## 🔒 Security

Do not put your Hugging Face API token directly in your Python code.

❌ Avoid this:

```python
api_key="hf_your_secret_token"
```

✅ Use an environment variable instead:

```python
api_key=os.environ["HF_TOKEN"]
```

This helps keep your API token private and prevents accidentally uploading it to GitHub.

---

## 📚 Summary

This project uses:

- **Hugging Face Hub**
- **InferenceClient**
- **WaveSpeed**
- **Pika Labs image-to-video model**

The workflow is simple:

```text
Image
  ↓
AI Prompt
  ↓
Image-to-Video Model
  ↓
Generated Video
```

---

## 📝 License

This project is provided for educational and experimental purposes.

Always check the model and provider documentation for usage requirements, limitations, and licensing information.

Happy building! 🚀
