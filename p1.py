import time
import random

# List of sentences to choose from
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing is a skill that improves with practice.",
    "Python is a powerful and versatile programming language.",
    "Speed and accuracy are important in competitive typing tests.",
    "Coding is not just about typing but also about thinking clearly."
]

def calculate_wpm(start_time, end_time, typed_text):
    time_taken = end_time - start_time  # in seconds
    word_count = len(typed_text.split())
    wpm = (word_count / time_taken) * 60
    return round(wpm, 2)

def calculate_accuracy(original, typed):
    original_words = original.strip().split()
    typed_words = typed.strip().split()
    correct = 0

    for o, t in zip(original_words, typed_words):
        if o == t:
            correct += 1

    accuracy = (correct / len(original_words)) * 100
    return round(accuracy, 2)

def typing_test():
    print("⌨️ Welcome to the Typing Speed Tester!\n")
    sentence = random.choice(sentences)
    print("📄 Type the following sentence:\n")
    print(f"👉 {sentence}\n")
    input("⏱️ Press Enter when you're ready to start typing...")

    start_time = time.time()
    typed = input("\nStart typing below:\n\n")
    end_time = time.time()

    print("\n🔍 Calculating results...\n")

    wpm = calculate_wpm(start_time, end_time, typed)
    accuracy = calculate_accuracy(sentence, typed)

    print(f"🕒 Time Taken: {round(end_time - start_time, 2)} seconds")
    print(f"📈 Words Per Minute (WPM): {wpm}")
    print(f"🎯 Accuracy: {accuracy}%")

if __name__ == "__main__":
    typing_test()