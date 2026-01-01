from store.models import Medicine

def get_bot_response(user_input):
    user_input_lower = user_input.lower()
    
    try:
        from store.models import Medicine
    except ImportError:
        return "Database connection issue. Please contact admin."

    # ========== SIMPLE QUERIES (Local Database - FAST) ==========
    
    # Greetings
    if any(word in user_input_lower for word in ["hi", "hello", "hey", "greetings"]):
        return "👋 <b>Hello!</b> I'm Dr. MedBot, your AI medical assistant. How can I help you today?"
    
    # Farewells
    elif any(word in user_input_lower for word in ["bye", "goodbye", "exit", "see you"]):
        return "👋 <b>Goodbye!</b> Stay healthy and visit again. Remember to consult a doctor for serious symptoms."
    
    # Thank you
    elif any(word in user_input_lower for word in ["thank", "thanks", "thank you"]):
        return "🤗 <b>You're welcome!</b> I'm here to help. Take care of your health!"
    
    # Who are you
    elif any(word in user_input_lower for word in ["who are you", "your name", "what are you"]):
        return "🤖 <b>I'm Dr. MedBot</b> - Your AI-powered medical assistant. I provide medicine information and basic health advice."
    
    # Help
    elif "help" in user_input_lower or "what can you do" in user_input_lower:
        return """🩺 <b>I can help you with:</b><br>
• 💊 <b>Medicine Recommendations:</b> Fever, headache, cold, pain, allergies<br>
• 🥗 <b>Diet & Nutrition:</b> Basic diet advice for common conditions<br>
• 🏥 <b>Health Advice:</b> Basic guidance (consult doctor for serious issues)<br>
• ⚠️ <b>Side Effects:</b> Common side effects information<br>
• 💡 <b>Dosage Tips:</b> General dosage guidelines<br><br>
<i>Try: "Medicine for fever" or "Diet for heat patient"</i>"""
    
    # ========== DIET & NUTRITION QUERIES ==========
    
    # Diet for heat-related issues
    elif "diet" in user_input_lower and ("heat" in user_input_lower or "summer" in user_input_lower or "hot" in user_input_lower):
        return """🍏 <b>Diet for Heat Stroke/Exhaustion:</b><br><br>
<b>💧 HYDRATION IS KEY:</b><br>
• Drink 3-4 liters of water daily<br>
• Coconut water (natural electrolytes)<br>
• ORS (Oral Rehydration Solution)<br>
• Lemon water with a pinch of salt<br>
• Buttermilk (chaas)<br><br>
<b>🥗 FOODS TO EAT:</b><br>
• Watermelon, cucumber, oranges, muskmelon<br>
• Curd rice, dal rice, khichdi<br>
• Boiled vegetables<br>
• Light soups and stews<br>
• Seasonal fruits<br><br>
<b>🚫 AVOID:</b><br>
• Spicy and oily food<br>
• Tea, coffee, alcohol<br>
• Processed and junk food<br>
• Heavy non-vegetarian meals<br><br>
<b>💡 IMPORTANT TIPS:</b><br>
• Rest in a cool, shaded place<br>
• Wear light, cotton clothes<br>
• Use fans or AC if available<br>
• Take cool showers<br>
• <i>Consult doctor if: High fever (>103°F), dizziness, confusion, or no urine for 8 hours</i>"""
    
    # Diet for diabetes
    elif "diet" in user_input_lower and ("diabet" in user_input_lower or "sugar" in user_input_lower):
        return """🩸 <b>Diet for Diabetes:</b><br><br>
<b>✅ RECOMMENDED FOODS:</b><br>
• Whole grains: oats, brown rice, barley<br>
• Vegetables: bitter gourd, fenugreek, spinach, broccoli<br>
• Protein: lentils, chickpeas, tofu, fish<br>
• Fruits: apple, guava, berries (in moderation)<br>
• Nuts: almonds, walnuts (small quantities)<br><br>
<b>🚫 AVOID:</b><br>
• Sugar, sweets, desserts<br>
• White bread, maida products<br>
• Processed foods, packaged snacks<br>
• Sweet drinks, fruit juices<br>
• Fried and oily foods<br><br>
<b>⏰ EATING SCHEDULE:</b><br>
• Eat small meals 5-6 times daily<br>
• Don't skip breakfast<br>
• Maintain regular meal timings<br>
• Monitor blood sugar levels regularly"""
    
    # Diet for blood pressure
    elif "diet" in user_input_lower and ("blood pressure" in user_input_lower or "bp" in user_input_lower or "hypertension" in user_input_lower):
        return """🫀 <b>Diet for High Blood Pressure:</b><br><br>
<b>🧂 REDUCE SALT INTAKE:</b><br>
• Limit to less than 5g salt per day (1 teaspoon)<br>
• Avoid table salt, papad, pickles, chips<br>
• Read food labels for sodium content<br><br>
<b>✅ POTASSIUM-RICH FOODS:</b><br>
• Bananas, oranges, watermelon<br>
• Spinach, potatoes, tomatoes<br>
• Beans, lentils, nuts<br><br>
<b>🌿 OTHER HELPFUL FOODS:</b><br>
• Garlic (2-3 cloves daily)<br>
• Celery, oats, flaxseeds<br>
• Low-fat dairy products<br><br>
<b>🚫 AVOID:</b><br>
• Processed and canned foods<br>
• Alcohol, tobacco<br>
• High-fat meats<br>
• Bakery products"""
    
    # General diet advice
    elif "diet" in user_input_lower:
        return """🥗 <b>General Healthy Diet Guidelines:</b><br><br>
<b>🍽️ BALANCED PLATE:</b><br>
• 50% Vegetables and fruits<br>
• 25% Whole grains (brown rice, oats)<br>
• 25% Protein (lentils, beans, lean meat)<br><br>
<b>💧 HYDRATION:</b><br>
• Drink 8-10 glasses of water daily<br>
• Include herbal teas, coconut water<br>
• Limit sugary drinks<br><br>
<b>⏰ EATING HABITS:</b><br>
• Eat 5-6 small meals daily<br>
• Don't skip breakfast<br>
• Chew food properly<br>
• Eat slowly, mindfully<br><br>
<b>🚫 AVOID:</b><br>
• Junk food and fast food<br>
• Excess sugar and salt<br>
• Processed foods<br>
• Late night heavy meals<br><br>
<i>💡 For personalized diet plans, consult a registered nutritionist or dietitian.</i>"""
    
    # ========== MEDICINE PRICE & STOCK ==========
    
    # Medicine price check
    elif any(word in user_input_lower for word in ["price", "cost", "how much", "rate"]):
        try:
            words = user_input_lower.split()
            for word in words:
                if len(word) > 3:
                    med = Medicine.objects.filter(name__icontains=word).first()
                    if med:
                        stock_status = "✅ In Stock" if med.stock > 0 else "❌ Out of Stock"
                        return f"💰 <b>{med.name}</b><br>• Price: <b>₹{med.price}</b><br>• Stock: {med.stock} units ({stock_status})<br>• Category: {getattr(med, 'category', 'General')}"
            
            # If no specific medicine found
            top_meds = Medicine.objects.all()[:3]
            if top_meds.exists():
                med_list = [f"• {m.name}: ₹{m.price}" for m in top_meds]
                return f"💰 <b>Popular Medicine Prices:</b><br>" + "<br>".join(med_list) + "<br><br><i>Ask: 'Price of [medicine name]'</i>"
            
            return "💰 <b>Tell me the medicine name</b> and I'll check the price for you."
        except Exception as e:
            print(f"Price check error: {e}")
            return "💰 Please tell me the specific medicine name for price information."
    
    # Stock check
    elif any(word in user_input_lower for word in ["stock", "available", "have", "quantity"]):
        try:
            words = user_input_lower.split()
            for word in words:
                if len(word) > 3:
                    med = Medicine.objects.filter(name__icontains=word).first()
                    if med:
                        if med.stock > 20:
                            status = "🟢 High Stock"
                        elif med.stock > 5:
                            status = "🟡 Moderate Stock"
                        else:
                            status = "🔴 Low Stock"
                        
                        return f"📦 <b>{med.name}</b><br>• Available: <b>{med.stock} units</b><br>• Status: {status}<br>• Price: ₹{med.price}"
            
            # Show low stock medicines
            low_stock = Medicine.objects.filter(stock__lt=10)[:3]
            if low_stock.exists():
                low_list = [f"• {m.name}: {m.stock} left" for m in low_stock]
                return f"📦 <b>Low Stock Alert:</b><br>" + "<br>".join(low_list) + "<br><br><i>Other medicines are well-stocked.</i>"
            
            return "📦 <b>Most medicines are available.</b> Please specify which medicine you're asking about."
        except:
            return "📦 Please specify the medicine name for stock information."
    
    # ========== SYMPTOM-BASED MEDICINE ADVICE ==========
    
    # Fever
    elif "fever" in user_input_lower:
        try:
            fever_meds = Medicine.objects.filter(
                name__icontains='paracetamol'
            ) | Medicine.objects.filter(
                name__icontains='dolo'
            ) | Medicine.objects.filter(
                name__icontains='crocin'
            ) | Medicine.objects.filter(
                name__icontains='panadol'
            )
            
            if fever_meds.exists():
                med_list = []
                for med in fever_meds[:4]:
                    stock_status = "✅" if med.stock > 0 else "⏳"
                    med_list.append(f"• {stock_status} {med.name} - ₹{med.price}")
                
                meds_text = "<br>".join(med_list)
                return f"""🌡️ <b>For Fever:</b><br>
{meds_text}<br><br>
<b>💡 Advice:</b><br>
• Rest and drink plenty of fluids<br>
• Monitor temperature every 4 hours<br>
• <b>Consult doctor if:</b> Fever > 103°F, lasts > 3 days, or with rash<br>
• <i>Children & pregnant women: Consult doctor before any medication</i>"""
            else:
                return """🌡️ <b>For Fever:</b><br>
• Paracetamol (500mg) - Every 6 hours<br>
• Dolo 650 - For high fever<br>
• Crocin - Alternative to Paracetamol<br><br>
<b>⚠️ Warning:</b> Avoid aspirin in children with viral fever."""
        except Exception as e:
            print(f"Fever error: {e}")
            return "🌡️ For fever: Paracetamol 500mg every 6 hours. Consult doctor if fever persists."
    
    # Headache
    elif "headache" in user_input_lower or "migraine" in user_input_lower:
        try:
            headache_meds = Medicine.objects.filter(
                name__icontains='saridon'
            ) | Medicine.objects.filter(
                name__icontains='combiflam'
            ) | Medicine.objects.filter(
                name__icontains='dispirin'
            ) | Medicine.objects.filter(
                name__icontains='aspirin'
            )
            
            if headache_meds.exists():
                med_list = []
                for med in headache_meds[:4]:
                    med_list.append(f"• {med.name} - ₹{med.price}")
                
                meds_text = "<br>".join(med_list)
                return f"""🤕 <b>For Headache:</b><br>
{meds_text}<br><br>
<b>💡 Advice:</b><br>
• Rest in a dark, quiet room<br>
• Drink water (dehydration causes headaches)<br>
• Apply cold compress to forehead<br>
• <b>Consult doctor if:</b> Severe pain, vomiting, vision changes<br>
• <i>Avoid frequent use of painkillers (>3 days/week)</i>"""
            else:
                return """🤕 <b>For Headache:</b><br>
• Saridon - Fast relief<br>
• Combiflam - For severe pain<br>
• Aspirin (only for adults)<br><br>
<b>⚠️ Note:</b> Avoid painkillers on empty stomach."""
        except:
            return "🤕 For headache: Saridon or Combiflam. Rest and stay hydrated."
    
    # Cold/Cough
    elif any(word in user_input_lower for word in ["cold", "cough", "flu", "sore throat"]):
        try:
            cold_meds = Medicine.objects.filter(
                name__icontains='vicks'
            ) | Medicine.objects.filter(
                name__icontains='chericof'
            ) | Medicine.objects.filter(
                name__icontains='benadryl'
            ) | Medicine.objects.filter(
                name__icontains='tixylix'
            )
            
            if cold_meds.exists():
                med_list = []
                for med in cold_meds[:4]:
                    stock_status = "✅" if med.stock > 10 else "⚠️"
                    med_list.append(f"• {stock_status} {med.name} - ₹{med.price}")
                
                meds_text = "<br>".join(med_list)
                return f"""🤧 <b>For Cold & Cough:</b><br>
{meds_text}<br><br>
<b>💡 Home Remedies:</b><br>
• Ginger-honey tea<br>
• Steam inhalation<br>
• Salt water gargle<br>
• <b>Consult doctor if:</b> High fever, breathing difficulty, symptoms > 7 days<br>
• <i>Children under 4: Avoid cough syrups without doctor's advice</i>"""
            else:
                return """🤧 <b>For Cold & Cough:</b><br>
• Vicks Action 500 - For cold with fever<br>
• Chericof - For dry cough<br>
• Benadryl - For allergic cough<br>
• Tixylix - For children (doctor's advice)<br><br>
<b>💧 Drink:</b> Warm water, herbal teas"""
        except:
            return "🤧 For cold: Vicks or Chericof. Stay warm and hydrated."

    # Pain
    elif any(word in user_input_lower for word in ["pain", "body pain", "back pain", "muscle pain"]):
        return """😣 <b>For Pain:</b><br>
• Ibuprofen (400mg) - For muscle/joint pain<br>
• Diclofenac gel - For localized pain<br>
• Paracetamol - Mild to moderate pain<br><br>
<b>⚠️ Important:</b><br>
• Take with food to avoid stomach upset<br>
• Don't mix different painkillers<br>
• <b>Consult doctor for:</b> Severe pain, injury, or chronic conditions<br>
• <i>Maximum: 3 days self-medication</i>"""
    
    # List medicines
    elif any(word in user_input_lower for word in ["list", "all medicines", "show medicines", "available medicines"]):
        try:
            all_meds = Medicine.objects.all()[:8]
            if all_meds.exists():
                med_list = []
                for med in all_meds:
                    stock_icon = "🟢" if med.stock > 10 else "🟡" if med.stock > 0 else "🔴"
                    med_list.append(f"• {stock_icon} {med.name}: ₹{med.price}")
                
                return f"📋 <b>Available Medicines:</b><br>" + "<br>".join(med_list) + f"<br><br><i>Total: {all_meds.count()} medicines in database</i>"
            else:
                return "📋 No medicines found in database."
        except:
            return "📋 We have medicines for fever, headache, cold, pain, and allergies."

    # Diarrhea
    elif "diarrhea" in user_input_lower or "loose motion" in user_input_lower:
        return """🤢 <b>For Diarrhea:</b><br>
• ORS (Oral Rehydration Solution)<br>
• Loperamide (for adults only)<br>
• Probiotics<br><br>
<b>💡 Advice:</b><br>
• Drink plenty of fluids<br>
• Eat BRAT diet (Banana, Rice, Applesauce, Toast)<br>
• <b>Consult doctor if:</b> Blood in stool, high fever, dehydration signs<br>
• <i>Avoid: Dairy, spicy food, caffeine</i>"""

    # Acidity
    elif any(word in user_input_lower for word in ["acidity", "heartburn", "indigestion"]):
        return """🔥 <b>For Acidity/Heartburn:</b><br>
• Antacids (Digene, Gelusil)<br>
• Ranitidine<br>
• Omeprazole (for severe cases)<br><br>
<b>💡 Prevention:</b><br>
• Avoid spicy/oily food<br>
• Don't lie down immediately after eating<br>
• Eat smaller, frequent meals<br>
• <i>Consult doctor if symptoms persist > 2 weeks</i>"""

    # Allergy
    elif any(word in user_input_lower for word in ["allergy", "itching", "rash"]):
        return """🤧 <b>For Allergies:</b><br>
• Cetirizine (Zyrtec)<br>
• Loratadine (Claritin)<br>
• Fexofenadine (Allegra)<br><br>
<b>💡 Advice:</b><br>
• Identify and avoid triggers<br>
• Use cold compress for itching<br>
• <b>Emergency:</b> Difficulty breathing, swelling - Go to hospital<br>
• <i>Consult doctor for proper diagnosis</i>"""

    # ========== OTHER COMMON QUERIES ==========
    
    elif "weight" in user_input_lower and ("loss" in user_input_lower or "reduce" in user_input_lower):
        return """⚖️ <b>Healthy Weight Loss Tips:</b><br>
• Eat more protein and fiber<br>
• Drink water before meals<br>
• Regular exercise (30 mins daily)<br>
• Avoid sugary drinks and snacks<br>
• Get enough sleep (7-8 hours)<br>
• <i>Consult doctor/nutritionist for personalized plan</i>"""
    
    elif "exercise" in user_input_lower or "workout" in user_input_lower:
        return """💪 <b>General Exercise Tips:</b><br>
• 30 minutes moderate exercise daily<br>
• Include cardio, strength, flexibility<br>
• Start slow if beginner<br>
• Stay hydrated during exercise<br>
• Listen to your body, don't overexert"""
    
    elif "sleep" in user_input_lower:
        return """😴 <b>Better Sleep Tips:</b><br>
• Maintain regular sleep schedule<br>
• Avoid screens 1 hour before bed<br>
• Create dark, quiet sleep environment<br>
• Avoid caffeine after 4 PM<br>
• Relax with reading or meditation before sleep"""
    
    elif "stress" in user_input_lower or "anxiety" in user_input_lower:
        return """🧘 <b>Stress Management:</b><br>
• Practice deep breathing exercises<br>
• Regular physical activity<br>
• Meditation or yoga<br>
• Talk to friends/family<br>
• Take breaks during work<br>
• <i>Consult doctor if stress affects daily life</i>"""
    
    # ========== COMPLEX MEDICAL QUERIES HANDLER ==========
    # Yeh check karo PEEHLE default se
    
    elif "heart" in user_input_lower and ("disease" in user_input_lower or "attack" in user_input_lower or "problem" in user_input_lower):
        return """❤️ <b>Heart Disease Information:</b><br><br>
<b>⚠️ WARNING: Heart conditions require immediate medical attention!</b><br><br>
<b>Common Medicines (Prescription Only):</b><br>
• Aspirin (low dose) - Blood thinner<br>
• Statins (Atorvastatin) - Cholesterol control<br>
• Beta-blockers (Metoprolol) - Heart rate control<br>
• ACE inhibitors (Ramipril) - Blood pressure<br><br>
<b>🩺 SYMPTOMS requiring IMMEDIATE attention:</b><br>
• Chest pain or discomfort<br>
• Shortness of breath<br>
• Nausea, lightheadedness<br>
• Pain in arms, back, neck, jaw<br><br>
<b>✅ LIFESTYLE CHANGES:</b><br>
• Quit smoking immediately<br>
• Reduce salt and fat intake<br>
• Regular exercise (doctor approved)<br>
• Manage stress, maintain healthy weight<br><br>
<b>🚨 EMERGENCY: If experiencing chest pain, call ambulance immediately!</b>"""
    
    elif "blood pressure" in user_input_lower or "bp" in user_input_lower or "hypertension" in user_input_lower:
        return """🫀 <b>Blood Pressure Management:</b><br><br>
<b>Common Medicines:</b><br>
• Amlodipine (Calcium channel blocker)<br>
• Telmisartan (ARB)<br>
• Hydrochlorothiazide (Diuretic)<br>
• Atenolol (Beta-blocker)<br><br>
<b>💡 Lifestyle Tips:</b><br>
• Reduce salt intake (<5g/day)<br>
• Regular exercise (30 mins/day)<br>
• Maintain healthy weight<br>
• Limit alcohol, quit smoking<br>
• Manage stress<br><br>
<b>📊 Normal BP: 120/80 mmHg</b><br>
<b>⚠️ High BP: >140/90 mmHg (Consult doctor)</b>"""
    
    elif "diabetes" in user_input_lower or "sugar" in user_input_lower:
        return """🩸 <b>Diabetes Management:</b><br><br>
<b>Common Medicines:</b><br>
• Metformin (First line treatment)<br>
• Glimepiride (Sulfonylurea)<br>
• Insulin (for Type 1/advanced Type 2)<br>
• DPP-4 inhibitors (Sitagliptin)<br><br>
<b>💡 Management Tips:</b><br>
• Monitor blood sugar regularly<br>
• Follow diabetic diet plan<br>
• Regular physical activity<br>
• Foot care (check daily)<br>
• Regular eye checkups<br><br>
<b>📊 Target Levels:</b><br>
• Fasting: 80-130 mg/dL<br>
• Post-meal: <180 mg/dL<br>
• HbA1c: <7%"""
    
    elif "asthma" in user_input_lower:
        return """🌬️ <b>Asthma Management:</b><br><br>
<b>Common Medicines:</b><br>
• Salbutamol inhaler (Quick relief)<br>
• Budesonide inhaler (Preventer)<br>
• Montelukast (Tablets)<br>
• Theophylline (Oral)<br><br>
<b>💡 Management Tips:</b><br>
• Avoid triggers (dust, pollen)<br>
• Use inhaler correctly<br>
• Keep rescue inhaler handy<br>
• Regular doctor checkups<br>
• Monitor peak flow<br><br>
<b>🚨 Emergency: If breathing difficulty persists, seek immediate help!</b>"""
    
    elif "cancer" in user_input_lower:
        return """🦠 <b>Cancer Information:</b><br><br>
<b>⚠️ IMPORTANT: Cancer requires specialist treatment!</b><br><br>
<b>Treatment Types:</b><br>
• Chemotherapy<br>
• Radiation therapy<br>
• Surgery<br>
• Immunotherapy<br>
• Targeted therapy<br><br>
<b>💡 Supportive Care:</b><br>
• Pain management<br>
• Nutrition support<br>
• Emotional counseling<br>
• Palliative care<br><br>
<b>✅ Early Detection Saves Lives:</b><br>
• Regular screenings<br>
• Know family history<br>
• Report unusual symptoms early<br>
• Maintain healthy lifestyle<br><br>
<b>🏥 Consult an oncologist for proper diagnosis and treatment.</b>"""
    
    elif "kidney" in user_input_lower:
        return """🧠 <b>Kidney Health:</b><br><br>
<b>Common Issues:</b><br>
• Kidney stones<br>
• Urinary tract infections<br>
• Chronic kidney disease<br>
• Kidney failure<br><br>
<b>💡 Prevention:</b><br>
• Drink plenty of water<br>
• Reduce salt intake<br>
• Control blood pressure and diabetes<br>
• Avoid NSAIDs long-term<br>
• Regular checkups if high risk<br><br>
<b>⚠️ Symptoms to watch:</b><br>
• Swelling in feet/ankles<br>
• Foamy urine<br>
• Fatigue, nausea<br>
• Changes in urine output"""
    
    elif "liver" in user_input_lower:
        return """🍏 <b>Liver Health:</b><br><br>
<b>Common Conditions:</b><br>
• Fatty liver disease<br>
• Hepatitis<br>
• Cirrhosis<br>
• Liver cancer<br><br>
<b>💡 Liver-Friendly Habits:</b><br>
• Limit alcohol consumption<br>
• Maintain healthy weight<br>
• Vaccinate against Hepatitis<br>
• Avoid sharing needles<br>
• Practice safe sex<br><br>
<b>⚠️ Warning Signs:</b><br>
• Jaundice (yellow skin/eyes)<br>
• Abdominal pain/swelling<br>
• Dark urine, pale stool<br>
• Chronic fatigue"""
    
    # ========== GENERIC MEDICINE QUERIES ==========
    
    elif "medicine for" in user_input_lower or "treatment for" in user_input_lower:
        # Extract the condition after "medicine for"
        query = user_input_lower.replace("medicine for", "").replace("treatment for", "").strip()
        
        if query:
            return f"""💊 <b>Information about {query.title()}:</b><br><br>
<b>General Advice:</b><br>
• Self-medication is risky for serious conditions<br>
• Proper diagnosis is essential<br>
• Dosage depends on age, weight, severity<br><br>
<b>💡 What I can help with:</b><br>
• Basic information about common conditions<br>
• When to consult a doctor<br>
• General prevention tips<br>
• Lifestyle modifications<br><br>
<b>🏥 For {query}, please consult a doctor for:</b><br>
• Accurate diagnosis<br>
• Prescription medications<br>
• Personalized treatment plan<br>
• Follow-up care"""
    
    elif "side effect" in user_input_lower or "side effects" in user_input_lower:
        return """⚠️ <b>Medicine Side Effects:</b><br><br>
<b>Common side effects to watch for:</b><br>
• Nausea, vomiting, diarrhea<br>
• Dizziness, drowsiness<br>
• Headache, insomnia<br>
• Rash, itching<br><br>
<b>🚨 Serious side effects (seek immediate help):</b><br>
• Difficulty breathing<br>
• Swelling of face/lips/tongue<br>
• Severe skin reactions<br>
• Chest pain, irregular heartbeat<br><br>
<b>💡 Tips to reduce side effects:</b><br>
• Take with food if stomach upset<br>
• Avoid alcohol with medications<br>
• Don't crush/break tablets unless advised<br>
• Follow prescribed dosage strictly<br><br>
<b>📝 Always read the package insert for complete side effects information.</b>"""
    
    elif "dosage" in user_input_lower or "how to take" in user_input_lower:
        return """💡 <b>General Dosage Guidelines:</b><br><br>
<b>Important Rules:</b><br>
1. Always follow doctor's prescription<br>
2. Never self-medicate<br>
3. Complete the full course<br>
4. Don't share medicines<br><br>
<b>📅 Common Dosage Schedules:</b><br>
• Once daily: Usually in morning<br>
• Twice daily: Every 12 hours<br>
• Three times daily: With meals<br>
• Four times daily: Every 6 hours<br><br>
<b>⏰ Best Practices:</b><br>
• Take at same time daily<br>
• Use pill organizer if multiple medicines<br>
• Set reminders on phone<br>
• Keep medication diary<br><br>
<b>❌ Never:</b><br>
• Double dose if missed<br>
• Stop abruptly without doctor advice<br>
• Take with alcohol<br>
• Use expired medicines"""

    # ========== FINAL DEFAULT RESPONSE ==========
    else:
        return f"""🤔 <b>I understand you're asking about:</b> "{user_input}"<br><br>
I can provide information on:<br>
• 💊 <b>Medicines</b> for common symptoms (fever, headache, cold, pain)<br>
• 🥗 <b>Diet & nutrition</b> advice<br>
• 💰 <b>Medicine prices</b> from our database<br>
• 📦 <b>Stock availability</b><br>
• ⚠️ <b>When to see a doctor</b><br><br>
<i>For complex medical conditions like heart disease, diabetes, etc.,<br>
please consult a qualified doctor for proper diagnosis and treatment.</i><br><br>
Try asking:<br>
• "Medicine for fever"<br>
• "Diet for diabetes"<br>
• "Price of paracetamol"<br>
• "Headache treatment"<br>
• "Healthy lifestyle tips"<br><br>
<b>🚨 Emergency: For serious symptoms, seek immediate medical help!</b>"""


# Helper function for medicine search
def search_medicine(keyword):
    """Search medicine in database"""
    try:
        results = Medicine.objects.filter(name__icontains=keyword)
        if results.exists():
            return [{"name": m.name, "price": m.price, "stock": m.stock} for m in results]
        return []
    except:
        return []