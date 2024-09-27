import sys
import pickle

file = sys.argv[1]

figx = pickle.load(open(file, 'rb'))
#figx = pickle.load(open('FigureObject.fig.pickle', 'rb'))

figx.show()

input("Press Enter to continue...")
