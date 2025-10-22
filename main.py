from fastapi import FastAPI

app = FastAPI(
    title="☕ CoffeeLingo API",
    description="""
Welcome to **CoffeeLingo API** — the perfect blend of *coffee vibes* and *English learning*!  
Use these fun endpoints to learn English words, quotes, and coffee facts every day.

---

### 🌟 Features:
- ☕ Daily Coffee Facts  
- 🧠 English Word of the Day  
- 🎯 Fun Coffee Quiz  
- 💬 Motivational Quotes  
- 🎓 Coffee-Inspired English Phrases  

---

💡 *"Sip, Learn, and Speak Better — with CoffeeLingo!"*  
""",
    version="1.0.0",
    contact={
        "name": "CoffeeLingo Team",
        "url": "https://coffeelingo.example.com",
        "email": "support@coffeelingo.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)



# --- 1. Coffee + English data ---
coffee_facts = [
    {
        "fact": "Coffee is the second most traded commodity in the world after oil.",
        "word": "Brew",
        "meaning": "To make coffee or tea by mixing it with hot water.",
        "example": "I like to brew my coffee early in the morning."
    },
    {
        "fact": "Espresso means 'pressed out' in Italian, referring to how the coffee is made.",
        "word": "Aroma",
        "meaning": "A pleasant smell, especially from coffee or flowers.",
        "example": "The aroma of freshly brewed coffee fills the room."
    },
    {
        "fact": "The first coffeehouse opened in Constantinople (now Istanbul) in 1550.",
        "word": "Caffeine",
        "meaning": "A natural substance found in coffee that helps you stay awake.",
        "example": "Too much caffeine can make you restless."
    },
    {
        "fact": "Cold brew coffee is brewed with cold water for 12 to 24 hours.",
        "word": "Mug",
        "meaning": "A large cup used for hot drinks like coffee or tea.",
        "example": "She poured coffee into her favorite mug."
    },
    {
        "fact": "Coffee beans are actually the seeds of a fruit called a coffee cherry.",
        "word": "Roast",
        "meaning": "To cook coffee beans with dry heat until brown and aromatic.",
        "example": "I prefer a medium roast because it tastes smoother."
    }
]

# --- 2. Coffee quotes ---
coffee_quotes = [
    "Life begins after coffee.",
    "Drink coffee and do good things.",
    "Good ideas start with great coffee — and better English!",
    "Coffee and kindness make the world go round.",
    "English first, espresso next ☕📖"
]

# --- 3. Brewing methods ---
brew_styles = [
    {"method": "Espresso", "description": "Strong, concentrated coffee made by forcing hot water through finely-ground beans."},
    {"method": "French Press", "description": "Steep coffee grounds in hot water, then press with a plunger for a rich flavor."},
    {"method": "Cold Brew", "description": "Brew coffee slowly in cold water for 12-24 hours; smooth and less acidic."},
    {"method": "Pour Over", "description": "Manually pour hot water over coffee grounds for clean and crisp flavor."},
    {"method": "Turkish Coffee", "description": "Finely ground coffee simmered in water with sugar, served unfiltered."}
]

# --- 4. Word of the Day Generator ---
def get_word_of_the_day():
    today = datetime.date.today()
    index = today.toordinal() % len(coffee_facts)
    return coffee_facts[index]

# --- 5. Mini Quiz Questions ---
quiz_questions = [
    {
        "question": "What does 'brew' mean?",
        "options": ["To roast beans", "To make coffee using hot water", "To grind coffee", "To chill coffee"],
        "answer": "To make coffee using hot water"
    },
    {
        "question": "Which country did espresso originate from?",
        "options": ["France", "Italy", "Brazil", "Turkey"],
        "answer": "Italy"
    },
    {
        "question": "What is caffeine?",
        "options": ["A coffee flavor", "A substance that keeps you awake", "A coffee brand", "A type of bean"],
        "answer": "A substance that keeps you awake"
    }
]

# --- ROUTES ---

@app.get("/")
def home():
    return {
        "message": "Welcome to CoffeeLingo API ☕📘",
        "description": "Learn English while sipping coffee! Try endpoints like /daily-coffee, /brew-style, /word-of-the-day, /quiz, and /quote."
    }

@app.get("/daily-coffee")
def daily_coffee():
    item = random.choice(coffee_facts)
    return {
        "coffee_fact": item["fact"],
        "english_word": item["word"],
        "meaning": item["meaning"],
        "example": item["example"],
        "motivation": random.choice(coffee_quotes)
    }

@app.get("/brew-style")
def get_brew_style():
    return random.choice(brew_styles)

@app.get("/word-of-the-day")
def word_of_day():
    word_data = get_word_of_the_day()
    return {
        "date": str(datetime.date.today()),
        "english_word": word_data["word"],
        "meaning": word_data["meaning"],
        "example": word_data["example"]
    }

@app.get("/quiz")
def get_quiz():
    return random.choice(quiz_questions)

@app.get("/quote")
def get_quote():
    return {"coffee_quote": random.choice(coffee_quotes)}

@app.get("/about")
def about():
    return {
        "creator": "Wajiha Akram",
        "api_name": "CoffeeLingo API ☕📘",
        "purpose": "To help coffee lovers learn English in a joyful, creative, and meaningful way.",
        "version": "2.0.0",
        "features": [
            "☕ Daily Coffee + English Tip",
            "📘 Word of the Day",
            "🧠 Mini Coffee Quiz",
            "🍵 Random Brew Style",
            "💬 Inspiring Quotes"
        ],
        "quote": "Learn English, one sip at a time ☕📖"
    }
