from flask import Flask, render_template, request
import pickle
import time
import random
from threading import Thread

app = Flask(__name__)

# Load the model and vectorizer
try:
    model = pickle.load(open('model.pkl', 'rb'))
    tfidf_vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))
    print("> MODEL LOADED SUCCESSFULLY")
except Exception as e:
    print(f"> ERROR LOADING MODEL FILES: {e}")
    model = None
    tfidf_vectorizer = None

def simulate_scan_animation():
    """Simulate scanning animation in console"""
    animations = [
        "|/-\\",
        "▁▂▃▄▅▆▇█▇▆▅▄▃▂▁",
        "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    ]
    anim = random.choice(animations)
    for i in range(10):
        time.sleep(0.1)
        print(f"\r> SCANNING {anim[i % len(anim)]}", end="", flush=True)
    print("\r> SCAN COMPLETE" + " " * 20)

def detect(input_text):
    if not model or not tfidf_vectorizer:
        return "SYSTEM ERROR: MODEL NOT LOADED"
    
    try:
        print(f"\n> INITIATING SCAN ON TEXT: {input_text[:50]}...")
        simulate_scan_animation()
        
        start_time = time.time()
        vectorized_text = tfidf_vectorizer.transform([input_text])
        result = model.predict(vectorized_text)
        processing_time = time.time() - start_time
        
        print(f"> PROCESSING TIME: {processing_time:.2f}s")
        print(f"> RESULT: {'PLAGIARISM DETECTED' if result[0] == 1 else 'CLEAN'}")
        
        return "PLAGIARISM DETECTED" if result[0] == 1 else "NO PLAGIARISM DETECTED"
    except Exception as e:
        print(f"> SCAN ERROR: {e}")
        return "SYSTEM ERROR: SCAN FAILED"

@app.route('/')
def home():
    print("\n> ACCESS DETECTED: PLAGIARISM_SCAN.EXE INTERFACE")
    print("> SERVING MAIN INTERFACE")
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_plagiarism():
    input_text = request.form['text']
    
    # Simulate intensive scanning process
    print("\n> NEW SCAN REQUEST RECEIVED")
    print("> ANALYZING TEXT PATTERNS...")
    
    # Add dramatic processing delay (3-5 seconds)
    processing_time = random.uniform(2.5, 4.5)
    time.sleep(processing_time)
    
    detection_result = detect(input_text)
    
    # Add console-like response
    print("> RETURNING RESULTS TO USER INTERFACE")
    print("=" * 50)
    
    return render_template('index.html', result=detection_result)

def run_console_animation():
    """Background animation for terminal"""
    while True:
        time.sleep(5)
        print("\n> SYSTEM ACTIVE" + " " * 30 + f"{time.strftime('%H:%M:%S')}")
        print("> MEMORY USAGE: " + str(random.randint(200, 500)) + "MB")
        print("> CPU LOAD: " + str(random.randint(15, 85)) + "%")

if __name__ == "__main__":
    # Start background terminal animation thread
    if random.choice([True, False]):  # 50% chance to enable
        t = Thread(target=run_console_animation)
        t.daemon = True
        t.start()
    
    print("""
     ___  _   _ _____ ___ ___ ___ _____ ___    ___ ___  ___ 
    | _ \/_\ | |_   _|_ _/ __|_ _|_   _/ _ \  / __/ _ \| _ \\
    |  _/ _ \| | | |  | | (_ || |  | || (_) || (_| (_) |  _/
    |_|/_/ \_\_| |_| |___\___|___| |_| \___/  \___\___/|_|  
    """)
    print("> INITIALIZING PLAGIARISM DETECTION SYSTEM")
    print("> SYSTEM READY - AWAITING REQUESTS")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)