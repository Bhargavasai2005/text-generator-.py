import random 

#list of adjectives
adjectives = ["attractive", "brave", "calm", "elegant", "friendly", "honest", 
"joyful", "kind", "lively", "modest", "nervous", "optimistic", "powerful", 
"reliable", "sincere", "thoughtful", "witty"]

#list of nouns
nouns = ["apple", "bear", "cat", "dog", "elephant", "fish", "girl", "horse", 
"jacket", "kite", "lamb", "monkey", "night", "owl", "pizza", "queen", "rainbow", 
"strawberry"]

#select a random adjective from list
adjective = random.choice(adjectives)

#select a random noun from list
noun = random.choice(nouns)

#generate a random text
random_text = adjective + " " + noun 

#print the random text
print(random_text)
