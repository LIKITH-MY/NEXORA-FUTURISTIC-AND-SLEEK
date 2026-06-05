# generate_image() goes here
from io import BytesIO
import requests
from PIL import Image
from utils.logger import log_interaction

def generate_image(openai_client, prompt):

    try:
        response = openai_client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            n=1,
            size="512x512"
        )

        image_url = response.data[0].url

        r = requests.get(image_url, timeout=20)

        img = Image.open(BytesIO(r.content))

        log_interaction("image_generation", prompt, image_url)

        return img, None

    except Exception as e:
        log_interaction("image_generation_error", prompt, str(e))
        return None, str(e)
