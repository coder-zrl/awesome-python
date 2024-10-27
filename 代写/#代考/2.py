from nltk.classify import NaiveBayesClassifier

def word_feats(words):
    return dict([(word, True) for word in words])

# 数据准备
positive_vocab = ['awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)', 'incredible', 'like']
negative_vocab = ['bad', 'terrible', 'useless', 'hate', ':(', 'motherfucker']
neutral_vocab = ['movie', 'the', 'sound', 'was', 'is', 'actors', 'did', 'know', 'words', 'not']

# 特征提取
positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]

train_set = negative_features + positive_features + neutral_features
# 训练
classifier = NaiveBayesClassifier.train(train_set)

# 测试
neg = 0
pos = 0
sentence = "I like the wonderful movie, it is awesome!!!"
sentence = sentence.lower()
words = sentence.split(' ')
for word in words:
        classResult = classifier.classify(word_feats(word))
        if classResult == 'neg':
            neg = neg + 1
        if classResult == 'pos':
            pos = pos + 1

print('积极: ' + str(float(pos) / len(words)))
print('消极: ' + str(float(neg) / len(words)))