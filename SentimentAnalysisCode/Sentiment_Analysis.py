import random

text = input("enter your sentence ")

positive_words = ["happy", "joy", "love", "excited"]
negative_words = ["sad", "angry", "hate", "frustrated"]
neutral_words = ["okay", "fine", "normal", "average"]

positive_count = 0
negative_count = 0
neutral_count = 0

words = text.split(" ")

for word in words:
    if word.lower() in positive_words: 
        positive_count += 1
    if word.lower() in negative_words: 
        negative_count += 1
    if word.lower() in neutral_words: 
        neutral_count += 1
    
# Generate a random emoji based on the sentiment
positive_emojis = ["😊", "😍", "🥰", "🤩"]
negative_emojis = ["😢", "😠", "😡", "😤"]
neutral_emojis = ["😐", "😑", "😶", "🙄"]

if positive_count > negative_count and positive_count > neutral_count: 
    emoji = random.choice(positive_emojis)
    print(f'Positive {emoji}')
elif negative_count > positive_count and negative_count > neutral_count: 
    emoji = random.choice(negative_emojis)
    print(f"Negative {emoji}")
    jokes = ["Why was the math book sad? Because it had too many problems.", 
                 "Why don't scientists trust atoms? Because they make up everything.",  
                 "Why do programmers prefer dark mode? Because light attracts bugs."]
    print(f"Here's a joke for you to feel better: {random.choice(jokes)}")
elif neutral_count > positive_count and neutral_count > negative_count: 
    emoji = random.choice(neutral_emojis)
    print(f"Neutral {emoji}")

total_words = len(words)

percentage_positive = (positive_count / total_words) * 100
percentage_negative = (negative_count / total_words) * 100
percentage_neutral = (neutral_count / total_words) * 100

print("The percentage of positive words in the text is:", percentage_positive,"%")
print("The percentage of negative words in the text is:", percentage_negative,"%")
print("The percentage of neutral words in the text is:", percentage_neutral,"%")
