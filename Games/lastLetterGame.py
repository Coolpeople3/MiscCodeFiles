import random

words = ["apple", "banana", "carrot", "computer", "haha", "zebra", "xylophone", "giraffe", "elephant", "dolphin", "jungle", "mountain", "river", "forest", "desert", "ocean", "whale", "penguin", "tiger", "lion", "snake", "eagle", "falcon", "squirrel", "rabbit", "monkey", "gorilla", "chimpanzee", "kangaroo", "koala", "platypus", "shark", "lobster", "crab", "octopus", "seahorse", "urchin", "starfish", "snail", "turtle", "iguana", "dragonfly", "butterfly", "bee", "ant", "grasshopper", "ladybug", "mosquito", "spider", "scorpion", "hedgehog", "armadillo", "badger", "weasel", "beaver", "chipmunk", "wolf", "fox", "dog", "cat", "hamster", "guinea", "pig", "ferret", "parrot", "cockatoo", "canary", "crow", "raven", "peacock", "swan", "goose", "duck", "hen", "rooster", "pigeon", "sparrow", "owl", "hawk", "heron", "flamingo", "pelican", "seal", "walrus", "otter", "bear", "polar", "grizzly", "panda", "leopard", "cheetah", "panther", "jaguar", "hippopotamus", "rhinoceros", "gazelle", "antelope", "buffalo", "bison", "moose", "deer", "elk", "caribou", "stallion", "mare", "pony", "donkey", "mule", "camel", "llama", "alpaca", "emu", "ostrich", "kiwi", "gecko", "python", "cobra", "viper", "rattlesnake", "boa", "constrictor", "alligator", "crocodile", "salamander", "newt", "frog", "toad", "chameleon", "tarantula", "moth", "wasp", "hornet", "termite", "centipede", "millipede", "worm", "slug", "clam", "mussel", "oyster", "scallop", "barnacle", "jellyfish", "coral", "anemone", "kelp", "algae", "plankton", "krill", "cuttlefish", "squid", "anglerfish", "manta", "ray", "stingray", "bat", "wolverine", "meerkat", "mongoose", "hyena", "lemur", "aardvark", "pangolin", "porcupine", "tapir", "capybara", "manatee", "dugong", "narwhal", "orca", "beluga", "porpoise", "beetle", "firefly", "glowworm", "cockroach", "damselfly", "cricket", "katydid", "praying", "mantis", "toucan", "kingfisher", "woodpecker", "skylark", "nightingale", "albatross", "frigatebird", "tern", "gull", "auk", "puffin", "loonie", "yagnik", "x is a hard letter;( let me go pls"]

userWords = []
computerWords = []

score = 0
randomWord = random.choice(words)
computerWords.append(randomWord)

while True:
    print(f"The computer has chosen the word, {randomWord}")
    userInput = input("What is your word? --> ").strip().lower()
    if userInput in userWords:
        print("You already used that word. Try again!\n")
        continue
    if userInput and userInput[0] == randomWord[-1]:
        score += 1
        userWords.append(userInput)
        print("Good, keep going!\n")
        # Update randomWord to match the condition
        matchingWords = [word for word in words if word[0] == userInput[-1] and word not in userWords and word not in computerWords]
        if matchingWords:
            randomWord = random.choice(matchingWords)
            computerWords.append(randomWord)
        else:
            print("No more matching words for the computer. You win!\n")
            break
    else:
        print("Invalid word or doesn't match the rules. Try again!\n")
