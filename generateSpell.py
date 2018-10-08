import sys
from textgenrnn import textgenrnn
textgen = textgenrnn(name="hp_spells")
fname = sys.argv[1]
textgen.train_from_file(fname,new_model=True,num_epochs=300)
textgen.generate(100)
