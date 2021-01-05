import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
from PIL import Image


def Result(path):
    text = open(path).read()

    wordcloud = WordCloud().generate(text)

    # Display the generated image:
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
