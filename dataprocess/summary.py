# utf-8
import sys

from textrank4zh import TextRank4Keyword, TextRank4Sentence

if __name__ == '__main__':
    content = sys.argv[1]
    tr4w = TextRank4Keyword()
    tr4s = TextRank4Sentence()
    # 取前3个
    labelWord = ""
    summary = ""
    tr4w.analyze(text=content, lower=True, window=2)
    for item in tr4w.get_keywords(3, word_min_len=1):
        labelWord += item['word']
        labelWord += ","
    tr4s.analyze(text=content, lower=True, source='no_stop_words')
    key_sentences = tr4s.get_key_sentences(num=1, sentence_min_len=2)
    for sentence in key_sentences:
        summary += sentence['sentence']
        summary += ","
    print(labelWord[:-1])
    print(summary[:-1])
