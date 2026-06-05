# chat_with_ai() goes here
from openai import OpenAI
from utils.logger import log_interaction

def chat_with_ai(openai_client, prompt, context_text=""):
    try:
        messages = [
            {"role": "system", "content": "You are NEXORA, a helpful and intelligent AI assistant."}
        ]

        if context_text:
            messages.append(
                {"role": "system", "content": f"Context: {context_text[:1500]}"}
            )

        messages.append({"role": "user", "content": prompt})

        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            max_tokens=800,
            temperature=0.7,
        )

        ans = response.choices[0].message.content.strip()
        log_interaction("chat", prompt, ans)
        return ans

    except Exception as e:
        err = f"OpenAI request failed: {e}"
        log_interaction("chat_error", prompt, err)
        return err
