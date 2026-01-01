import openai
from django.conf import settings

def get_chatgpt_response(user_input, context=""):
    """
    Simple working ChatGPT response function
    """
    try:
        # Debug print
        print(f"🤖 ChatGPT Query: '{user_input}'")
        
        # Use older API method (more reliable)
        openai.api_key = settings.OPENAI_API_KEY
        
        # Simple medical prompt
        system_prompt = f"""You are a helpful medical assistant in India.
Provide short, practical medical advice.
Available in store: {context}
"""
        
        # Use gpt-3.5-turbo (works with most API keys)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150,
            temperature=0.7
        )
        
        result = response.choices[0].message.content.strip()
        print(f"✅ ChatGPT Response received: {result[:80]}...")
        return result
        
    except openai.error.AuthenticationError:
        print("❌ ChatGPT: Authentication failed - check API key")
        return None
        
    except openai.error.RateLimitError:
        print("❌ ChatGPT: Rate limit exceeded - no credits")
        return None
        
    except openai.error.APIError as e:
        print(f"❌ ChatGPT API Error: {e}")
        return None
        
    except Exception as e:
        print(f"❌ ChatGPT Unexpected Error: {type(e).__name__}: {e}")
        return None


def get_local_medical_response(user_input, context=""):
    """
    Local medical knowledge base
    """
    user_input = user_input.lower()
    
    # Diet related
    if "diet" in user_input and "heat" in user_input:
        return """🍏 **Diet for Heat Stroke/Exhaustion:**

**HYDRATE:**
• Drink 3-4 liters of water daily
• Coconut water (natural electrolytes)
• ORS solution or lemon water with salt
• Buttermilk (chaas)

**FOODS TO EAT:**
• Watermelon, cucumber, oranges, muskmelon
• Curd rice, dal rice, khichdi
• Boiled vegetables
• Light soups

**AVOID:**
• Spicy and oily food
• Tea, coffee, alcohol
• Processed and junk food
• Heavy non-vegetarian meals

**IMPORTANT:** Rest in cool place, wear light cotton clothes, consult doctor if symptoms persist."""

    elif "diet" in user_input and ("diabet" in user_input or "sugar" in user_input):
        return """🩸 **Diet for Diabetes:**
• Whole grains: oats, brown rice, barley
• Vegetables: bitter gourd, fenugreek, spinach
• Protein: lentils, chickpeas, tofu
• Fruits: apple, guava, berries (in moderation)
• Avoid: sugar, white bread, processed foods, sweet drinks"""

    elif "diet" in user_input and ("blood pressure" in user_input or "bp" in user_input):
        return """🫀 **Diet for High Blood Pressure:**
• Reduce salt intake (<5g/day)
• Potassium-rich: bananas, spinach, potatoes
• Garlic, celery, oats, flaxseeds
• Avoid: processed foods, pickles, papad, chips"""

    elif "diet" in user_input:
        return """🥗 **General Healthy Diet:**
• Balanced meals (carbs 50%, protein 30%, fats 20%)
• 5-6 small meals daily
• Drink 8-10 glasses of water
• Fresh fruits and vegetables daily
• Limit sugar, salt, and processed foods"""

    # Common symptoms
    elif "fever" in user_input:
        return "🌡️ **For Fever:** Paracetamol 500mg every 6 hours. Monitor temperature. Drink plenty of fluids. Consult doctor if fever >103°F or lasts >3 days."

    elif "headache" in user_input:
        return "🤕 **For Headache:** Saridon or Combiflam. Rest in dark room. Drink water. Consult doctor for severe/migraine headaches."

    elif "cold" in user_input or "cough" in user_input:
        return "🤧 **For Cold & Cough:** Vicks Action 500 or Chericof. Drink warm water, ginger tea. Steam inhalation. Rest well."

    elif "pain" in user_input:
        return "😣 **For Pain:** Ibuprofen 400mg or Diclofenac gel. Take with food. Consult doctor for chronic pain."

    elif "acidity" in user_input:
        return "🔥 **For Acidity:** Antacids (Digene, Gelusil). Eat small frequent meals. Avoid spicy/oily food. Don't lie down after eating."

    # Default
    return """💊 **Medical Assistance:**
I can help with:
• Medicine recommendations for common symptoms
• Basic first aid information
• General health and diet tips
• When to consult a doctor

For specific medical advice, please consult a qualified healthcare professional."""