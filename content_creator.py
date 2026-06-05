# CONTENT_CATEGORIES and content generation logic
from utils.logger import log_interaction

CONTENT_CATEGORIES = {

    "Technology": {
        "icon": "💻",
        "description":
        "Tech articles, coding, AI & innovation"
    },

    "Business": {
        "icon": "💼",
        "description":
        "Marketing, strategy, entrepreneurship"
    },

    "Health & Wellness": {
        "icon": "🏥",
        "description":
        "Fitness, nutrition, mental health"
    },

    "Education": {
        "icon": "📚",
        "description":
        "Learning materials, courses"
    },

    "Entertainment": {
        "icon": "🎬",
        "description":
        "Stories, scripts, creative content"
    },

    "Travel": {
        "icon": "✈️",
        "description":
        "Guides, itineraries"
    },

    "Food & Recipes": {
        "icon": "🍳",
        "description":
        "Recipes and cooking"
    },

    "Finance": {
        "icon": "💰",
        "description":
        "Investment and budgeting"
    }
}


def generate_content_from_template(
        openai_client,
        template,
        user_input
):

    try:

        prompt = template.replace(
            "[TOPIC]",
            user_input
        )

        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content":
                    "You are an expert content writer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=1500,
            temperature=0.8
        )

        content = (
            response
            .choices[0]
            .message.content
        )

        log_interaction(
            "content_generation",
            prompt[:100],
            content[:100]
        )

        return content

    except Exception as e:

        return str(e)
