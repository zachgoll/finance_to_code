from nltk.tokenize import TweetTokenizer

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positives = set()
        self.negatives = set()
        
      # TODO - load positive and negative words into a dictionary 
      # so they can be easily accessed by analyze()
        with open(positives) as p:
            for line in p:
                if line.startswith(";") or line.startswith(" "):
                    continue
                else:
                    self.positives.add(line.rstrip("\n"))
            p.close()
                    
        with open(negatives) as n:
            for line in n:
                if line.startswith(";") or line.startswith(" "):
                    continue
                else:
                    self.negatives.add(line.rstrip("\n"))
            n.close()
        

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        # TODO - assign each word a value, calculate tweet's total score, and return that score
        counter = 0
        tokenizer = TweetTokenizer(preserve_case=False)
        tokens = tokenizer.tokenize(text)
        
        for word in tokens:
        #       check word to see if it is in either dictionary, or no dictionary
            if word in self.positives:
                counter = counter + 1
            elif word in self.negatives:
                counter = counter - 1
            else: 
                continue
        return counter
