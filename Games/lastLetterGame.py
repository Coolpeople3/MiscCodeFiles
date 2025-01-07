import random

words = ["apple", "banana", "carrot", "computer", "haha", "zebra", "xylophone", "giraffe", "elephant", "dolphin", "jungle", "mountain", "river", "forest", "desert", "ocean", "whale", "penguin", "tiger", "lion", "snake", "eagle", "falcon", "squirrel", "rabbit", "monkey", "gorilla", "chimpanzee", "kangaroo", "koala", "platypus", "shark", "dolphin", "lobster", "crab", "octopus", "seahorse", "urchin", "starfish", "snail", "turtle", "iguana", "dragonfly", "butterfly", "bee", "ant", "grasshopper", "ladybug", "mosquito", "spider", "scorpion", "hedgehog", "armadillo", "badger", "weasel", "beaver", "chipmunk", "wolf", "fox", "dog", "cat", "hamster", "guinea", "pig", "ferret", "parrot", "cockatoo", "canary", "crow", "raven", "peacock", "swan", "goose", "duck", "hen", "rooster", "pigeon", "sparrow", "owl", "hawk", "heron", "flamingo", "pelican", "seal", "walrus", "otter", "bear", "polar", "grizzly", "panda", "leopard", "cheetah", "panther", "jaguar", "hippopotamus", "rhinoceros", "zebra", "gazelle", "antelope", "buffalo", "bison", "moose", "deer", "elk", "caribou", "stallion", "mare", "pony", "donkey", "mule", "camel", "llama", "alpaca", "emu", "ostrich", "kiwi", "gecko", "python", "cobra", "viper", "rattlesnake", "boa", "constrictor", "alligator", "crocodile", "salamander", "newt", "frog", "toad", "chameleon", "tarantula", "moth", "wasp", "hornet", "termite", "centipede", "millipede", "worm", "slug", "clam", "mussel", "oyster", "scallop", "barnacle", "jellyfish", "coral", "anemone", "kelp", "algae", "plankton", "krill", "cuttlefish", "squid", "goblin", "anglerfish", "seahorse", "manta", "ray", "stingray", "bat", "hedgehog", "wolverine", "chipmunk", "meerkat", "mongoose", "hyena", "lemur", "aardvark", "pangolin", "porcupine", "tapir", "capybara", "manatee", "dugong", "narwhal", "orca", "beluga", "porpoise", "beetle", "firefly", "glowworm", "cockroach", "dragonfly", "damselfly", "cricket", "katydid", "praying", "mantis", "stick", "insect", "leaf", "cutter", "ant", "hornbill", "toucan", "kingfisher", "woodpecker", "skylark", "nightingale", "albatross", "booby", "frigatebird", "petrel", "tern", "gull", "auk", "puffin", "loonie"]


userWords = []

score = 0
randomWord = random.choice(words)

while True:
    print(f"The computer has chosen the word, {randomWord}")
    userInput = input("What is your word? --> ")
    if userInput[1] == randomWord[-1]:
        score += 1
        print("Good, keep going!\n")
        # Update randomWord to match the condition
        randomWord = random.choice([word for word in words if word[0] == userInput[-1]])
    else:
        randomWord = random.choice(words)
