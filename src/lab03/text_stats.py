import sys

from text import count_freq, normalize, tokenize, top_n


data = sys.stdin.read()

if data.startswith(b'\xff\xfe'):
    text = data.decode('utf-16')
elif data.startswith(b'\xfe\xff'):
    text = data.decode('utf-16')
else:
    try:
        text = data.decode('utf-8')
    except UnicodeDecodeError:
        text = data.decode('cp1251')

text = normalize(text)
tokens = tokenize(text)
freq = count_freq(tokens)
top = top_n(freq)

print(f'Всего слов: {len(tokens)}')
print(f'Уникальных слов: {len(freq)}')
print('Топ-5:')

for word, count in top:
    print(f'{word}:{count}')