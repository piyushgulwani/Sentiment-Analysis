
from tkinter import *
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

def analyze() : 

    sentence = TextBlob(e1_value.get(), analyzer = NaiveBayesAnalyzer())
    positivity = sentence.sentiment.p_pos
    negativity = sentence.sentiment.p_neg

    if positivity > negativity : 
        Label(gui, text = 'Sentence Is Positive 😍', bg = 'cyan').pack(fill = X, side = BOTTOM)

    elif positivity < negativity : 
        Label(gui, text = 'Sentence Is Negative 😞', bg = 'cyan').pack(fill = X, side = BOTTOM)

    else : 
        Label(gui, text = 'Couldnt Analyze Text', bg = 'cyan').pack(fill = X, side = BOTTOM)

gui = Tk()
gui.geometry('500x300')
gui.title('Sentiment Analyzer')

e1_value = StringVar()
Entry(gui, textvariable = e1_value, font = 'comicsnams 20', justify = CENTER).pack(pady = 80)

Button(gui, text = 'Analyze', command = analyze).pack()

gui.mainloop()