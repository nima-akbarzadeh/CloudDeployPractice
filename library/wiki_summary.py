import wikipedia

def summarize(name, length=1):
    return wikipedia.summary(name, sentences=length)
