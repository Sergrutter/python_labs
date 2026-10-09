import sys

from text import count_freq, normalize, tokenize, top_n


text = sys.stdin.read()

text = normalize(text)
tokens = tokenize(text)
freq = count_freq(tokens)
top = top_n(freq)

print(f'Всего слов: {len(tokens)}')
print(f'Уникальных слов: {len(freq)}')
print('Топ-5:')

for word, count in top:
    print(f'{word}:{count}')
