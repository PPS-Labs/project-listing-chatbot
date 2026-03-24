"""
ML-powered recommendation engine for matching user components to robotics projects.
Uses TF-IDF vectorization and cosine similarity for intelligent matching.
"""
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Synonym / alias dictionary for component matching
COMPONENT_ALIASES = {
    # Arduino variants
    'arduino': 'arduino uno',
    'arduino board': 'arduino uno',
    'atmega': 'arduino uno',
    'atmega328': 'arduino uno',
    'uno': 'arduino uno',
    'mega': 'arduino mega',
    'arduino mega': 'arduino mega',
    'nano': 'arduino nano',
    'arduino nano': 'arduino nano',

    # Raspberry Pi
    'raspberry': 'raspberry pi',
    'raspi': 'raspberry pi',
    'rpi': 'raspberry pi',
    'pi': 'raspberry pi',

    # ESP
    'esp': 'esp8266',
    'esp32': 'esp32',
    'nodemcu': 'esp8266',
    'wemos': 'esp8266',

    # Sensors
    'ultrasonic': 'ultrasonic sensor hc-sr04',
    'ultrasound': 'ultrasonic sensor hc-sr04',
    'hcsr04': 'ultrasonic sensor hc-sr04',
    'hc-sr04': 'ultrasonic sensor hc-sr04',
    'distance sensor': 'ultrasonic sensor hc-sr04',
    'sonar': 'ultrasonic sensor hc-sr04',

    'ir': 'ir sensor',
    'infrared': 'ir sensor',
    'ir sensor': 'ir sensor',
    'obstacle sensor': 'ir sensor',
    'line sensor': 'ir sensor',

    'pir': 'pir motion sensor',
    'motion sensor': 'pir motion sensor',
    'motion': 'pir motion sensor',

    'dht11': 'dht11 temperature sensor',
    'dht22': 'dht11 temperature sensor',
    'temperature sensor': 'dht11 temperature sensor',
    'humidity sensor': 'dht11 temperature sensor',
    'temp sensor': 'dht11 temperature sensor',

    'ldr': 'ldr light sensor',
    'light sensor': 'ldr light sensor',
    'photoresistor': 'ldr light sensor',

    'mpu6050': 'mpu6050 gyroscope',
    'gyroscope': 'mpu6050 gyroscope',
    'accelerometer': 'mpu6050 gyroscope',
    'gyro': 'mpu6050 gyroscope',
    'imu': 'mpu6050 gyroscope',

    'soil moisture': 'soil moisture sensor',
    'moisture sensor': 'soil moisture sensor',

    'gas sensor': 'mq2 gas sensor',
    'mq2': 'mq2 gas sensor',
    'smoke sensor': 'mq2 gas sensor',

    'color sensor': 'tcs3200 color sensor',
    'tcs3200': 'tcs3200 color sensor',
    'colour sensor': 'tcs3200 color sensor',

    # Actuators
    'servo': 'servo motor sg90',
    'servo motor': 'servo motor sg90',
    'sg90': 'servo motor sg90',
    'micro servo': 'servo motor sg90',

    'dc motor': 'dc motor',
    'motor': 'dc motor',
    'dc': 'dc motor',

    'stepper': 'stepper motor',
    'stepper motor': 'stepper motor',
    'nema17': 'stepper motor',

    'buzzer': 'buzzer',
    'piezo': 'buzzer',

    'relay': 'relay module',
    'relay module': 'relay module',

    'pump': 'water pump',
    'water pump': 'water pump',

    # Modules
    'l298n': 'l298n motor driver',
    'motor driver': 'l298n motor driver',
    'h-bridge': 'l298n motor driver',
    'motor shield': 'l298n motor driver',

    'bluetooth': 'hc-05 bluetooth module',
    'hc-05': 'hc-05 bluetooth module',
    'hc05': 'hc-05 bluetooth module',
    'bt module': 'hc-05 bluetooth module',

    'wifi': 'esp8266',
    'wifi module': 'esp8266',

    'rf': 'rf module 433mhz',
    'rf module': 'rf module 433mhz',
    'radio': 'rf module 433mhz',
    '433mhz': 'rf module 433mhz',

    'gps': 'gps module neo-6m',
    'neo-6m': 'gps module neo-6m',

    # Displays
    'lcd': 'lcd 16x2 display',
    '16x2': 'lcd 16x2 display',
    'lcd display': 'lcd 16x2 display',

    'oled': 'oled display',
    'oled display': 'oled display',

    'led': 'led',
    'leds': 'led',

    # Power
    'battery': 'battery pack',
    'power supply': 'battery pack',
    'power bank': 'battery pack',

    # Other
    'potentiometer': 'potentiometer',
    'pot': 'potentiometer',
    'knob': 'potentiometer',
    'joystick': 'joystick module',
    'keypad': 'keypad 4x4',
    'camera': 'camera module',
    'webcam': 'camera module',
    'speaker': 'speaker',
}

# Greeting patterns
GREETING_PATTERNS = [
    r'\b(hi|hello|hey|howdy|greetings|good morning|good afternoon|good evening|yo|sup|hola)\b'
]

# Farewell patterns
FAREWELL_PATTERNS = [
    r'\b(bye|goodbye|see you|later|thanks|thank you|thank|exit|quit)\b'
]

# Help patterns
HELP_PATTERNS = [
    r'\b(help|how does this work|what can you do|instructions|guide|tutorial)\b'
]


def clean_text(text):
    """Clean and normalize text for processing."""
    text = text.lower().strip()
    # Keep hyphens for component names like hc-sr04
    text = re.sub(r'[^\w\s\-]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text


def detect_intent(message):
    """Detect the user's intent from their message."""
    msg = message.lower().strip()

    for pattern in GREETING_PATTERNS:
        if re.search(pattern, msg):
            return 'greeting'

    for pattern in FAREWELL_PATTERNS:
        if re.search(pattern, msg):
            return 'farewell'

    for pattern in HELP_PATTERNS:
        if re.search(pattern, msg):
            return 'help'

    # Check if user is asking for project ideas
    idea_keywords = ['project', 'idea', 'build', 'make', 'create', 'suggest', 'recommendation',
                     'what can i', 'what should i', 'give me', 'want to', 'i have', 'i got',
                     'using', 'with', 'use']
    if any(kw in msg for kw in idea_keywords):
        return 'project_request'

    # Check if mentioning components (fallback - treat as project request)
    for alias in COMPONENT_ALIASES:
        if alias in msg:
            return 'project_request'

    return 'unknown'


def extract_components(message):
    """Extract component keywords from user message and resolve to standard names."""
    msg = clean_text(message)
    found_components = set()

    # Sort aliases by length (longest first) to match multi-word aliases first
    sorted_aliases = sorted(COMPONENT_ALIASES.keys(), key=len, reverse=True)

    for alias in sorted_aliases:
        if alias in msg:
            standard_name = COMPONENT_ALIASES[alias]
            found_components.add(standard_name)

    return list(found_components)


def get_project_recommendations(user_components, all_projects):
    """
    Use TF-IDF + cosine similarity to find the best matching projects.

    Args:
        user_components: List of standardized component names from user input
        all_projects: QuerySet of Project objects

    Returns:
        List of (project, score, matched_components) tuples, sorted by relevance
    """
    if not user_components or not all_projects:
        return []

    recommendations = []

    for project in all_projects:
        project_components = [pc.component.name.lower() for pc in project.projectcomponent_set.all()]
        project_keywords = []
        for pc in project.projectcomponent_set.all():
            project_keywords.extend(pc.component.get_keywords_list())

        # Calculate match score
        user_comp_lower = [c.lower() for c in user_components]

        # Direct component matching
        matched = []
        for uc in user_comp_lower:
            for pc in project_components:
                if uc in pc or pc in uc:
                    matched.append(pc)
                    break

        if not matched:
            # Try keyword matching as fallback
            for uc in user_comp_lower:
                uc_words = set(uc.split())
                for kw in project_keywords:
                    if kw in uc or uc in kw or uc_words & set(kw.split()):
                        for pc in project_components:
                            matched.append(pc)
                        break

        if matched:
            # Score = percentage of project components that were matched
            match_ratio = len(set(matched)) / len(project_components)
            # Bonus for having more of the required components
            coverage_bonus = len(set(matched)) / max(len(user_comp_lower), 1)
            score = (match_ratio * 0.7) + (coverage_bonus * 0.3)
            recommendations.append((project, round(score * 100, 1), list(set(matched))))

    # Sort by score descending
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:5]  # Top 5 recommendations


def generate_tfidf_recommendations(user_text, all_projects):
    """
    Alternative TF-IDF approach: vectorize user input and project descriptions,
    then find most similar projects.
    """
    if not all_projects:
        return []

    # Build corpus: one document per project
    corpus = []
    projects_list = list(all_projects)

    for project in projects_list:
        # Combine project info into a single text
        comp_names = ' '.join([pc.component.name for pc in project.projectcomponent_set.all()])
        comp_keywords = ' '.join([
            pc.component.keywords for pc in project.projectcomponent_set.all()
        ])
        doc = f"{project.title} {project.description} {comp_names} {comp_keywords}"
        corpus.append(doc.lower())

    # Add the user's text as the last document
    corpus.append(clean_text(user_text))

    # Vectorize
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Compute similarity between user text (last doc) and all projects
    user_vector = tfidf_matrix[-1]
    project_vectors = tfidf_matrix[:-1]
    similarities = cosine_similarity(user_vector, project_vectors).flatten()

    # Get top matches
    results = []
    for idx, score in enumerate(similarities):
        if score > 0.05:  # Minimum threshold
            results.append((projects_list[idx], round(score * 100, 1)))

    results.sort(key=lambda x: x[1], reverse=True)
    return results[:5]


def format_bot_response(intent, components=None, recommendations=None, tfidf_results=None):
    """Format the chatbot response based on intent and results."""

    if intent == 'greeting':
        return {
            'message': "🤖 Hello! I'm **RoboHelper** — your robotics project idea assistant!\n\n"
                       "Tell me what components you have (like Arduino, sensors, motors) "
                       "and I'll suggest awesome robotics project ideas for you!\n\n"
                       "For example, try saying:\n"
                       "• *\"I have an Arduino Uno, ultrasonic sensor, and servo motor\"*\n"
                       "• *\"What can I build with IR sensors and DC motors?\"*",
            'components': [],
            'projects': [],
            'type': 'greeting'
        }

    if intent == 'farewell':
        return {
            'message': "👋 Goodbye! Happy building! Come back anytime for more robotics project ideas. 🤖🔧",
            'components': [],
            'projects': [],
            'type': 'farewell'
        }

    if intent == 'help':
        return {
            'message': "🔧 **How to use RoboHelper:**\n\n"
                       "1. Tell me the components/sensors/modules you have\n"
                       "2. I'll analyze your components using ML\n"
                       "3. I'll suggest the best robotics projects you can build!\n\n"
                       "**Components I know about:**\n"
                       "🔌 Microcontrollers: Arduino Uno/Mega/Nano, Raspberry Pi, ESP8266/ESP32\n"
                       "📡 Sensors: Ultrasonic, IR, PIR, DHT11, LDR, MPU6050, Soil Moisture\n"
                       "⚙️ Actuators: Servo Motor, DC Motor, Stepper Motor, Relay, Buzzer\n"
                       "📦 Modules: L298N Motor Driver, Bluetooth, WiFi, RF, GPS\n"
                       "🖥️ Displays: LCD 16x2, OLED\n\n"
                       "Just type your components and I'll find the perfect project for you!",
            'components': [],
            'projects': [],
            'type': 'help'
        }

    if intent == 'project_request':
        if not components:
            return {
                'message': "🤔 I couldn't identify any specific components from your message. "
                           "Could you tell me which electronics components you have?\n\n"
                           "For example: *\"I have Arduino Uno, ultrasonic sensor, and servo motor\"*",
                'components': [],
                'projects': [],
                'type': 'clarification'
            }

        # Build response with matched components and project suggestions
        comp_tags = ', '.join([f"**{c.title()}**" for c in components])
        msg = f"🔍 I detected these components: {comp_tags}\n\n"

        projects_data = []

        if recommendations:
            msg += "🚀 **Here are my top project suggestions for you:**\n\n"
            for i, (project, score, matched) in enumerate(recommendations, 1):
                difficulty_emoji = {'beginner': '🟢', 'intermediate': '🟡', 'advanced': '🔴'}
                emoji = difficulty_emoji.get(project.difficulty, '⚪')

                all_comps = [pc.component.name for pc in project.projectcomponent_set.all()]

                msg += f"---\n\n"
                msg += f"### {i}. {project.title} {emoji}\n"
                msg += f"**Match Score:** {score}% | **Difficulty:** {project.difficulty.title()}\n\n"
                msg += f"{project.description}\n\n"
                msg += f"**Components needed:** {', '.join(all_comps)}\n\n"

                if project.instructions:
                    msg += f"💡 **Tips:** {project.instructions}\n\n"

                projects_data.append({
                    'id': project.id,
                    'title': project.title,
                    'description': project.description,
                    'difficulty': project.difficulty,
                    'score': score,
                    'components': all_comps,
                    'instructions': project.instructions,
                    'matched_components': matched,
                })

            msg += "\n💡 *Want more ideas? Add or remove components and ask again!*"
        else:
            msg += ("😅 I couldn't find a perfect project match for that exact combination, "
                    "but try adding more components or different ones!\n\n"
                    "Type **help** to see all components I know about.")

        return {
            'message': msg,
            'components': components,
            'projects': projects_data,
            'type': 'recommendation'
        }

    # Unknown intent
    return {
        'message': "🤖 I'm not sure what you mean. I'm a robotics project assistant!\n\n"
                   "Tell me what components you have and I'll suggest project ideas.\n"
                   "Type **help** to learn more about how I work.",
        'components': [],
        'projects': [],
        'type': 'unknown'
    }
