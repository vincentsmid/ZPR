def get_frequencies(text):
    freq = {}
    for char in text:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1
    return freq

def sort_by_frequency(symbols_freq):
    result = symbols_freq.copy()
    for i in range(len(result)):
        for j in range(len(result) - 1):
            if result[j][1] < result[j + 1][1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

def split_symbols(symbols_freq):
    total = 0
    for symbol, freq in symbols_freq:
        total += freq

    running_sum = 0
    best_diff = float('inf')
    split_index = 0

    for i in range(len(symbols_freq)):
        running_sum += symbols_freq[i][1]
        diff = abs(2 * running_sum - total)
        if diff < best_diff:
            best_diff = diff
            split_index = i + 1

    return symbols_freq[:split_index], symbols_freq[split_index:]

def generate_codes(symbols_freq, prefix=''):
    if len(symbols_freq) == 1:
        return {symbols_freq[0][0]: prefix}

    symbols_freq = sort_by_frequency(symbols_freq)
    left, right = split_symbols(symbols_freq)

    codes = {}
    left_codes = generate_codes(left, prefix + '1')
    right_codes = generate_codes(right, prefix + '0')

    codes.update(left_codes)
    codes.update(right_codes)
    return codes

def koduj(text):
    freq = get_frequencies(text)
    symbols_freq = []
    for symbol, frequency in freq.items():
        symbols_freq.append((symbol, frequency))

    codes = generate_codes(symbols_freq)

    encoded = ''
    for char in text:
        encoded += codes[char]

    return {
        'slova': codes,
        'zprava': encoded
    }
