from textgenrnn import textgenrnn
textgen = textgenrnn()
textgen.train_from_file('spells.txt',num_epochs=100)
textgen.generate(1)
