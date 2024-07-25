import re
def decode_unicode_sequences(text):
    # 匹配 u 开头的十六进制数字序列
    unicode_sequences = re.findall(r'u([0-9a-fA-F]+)', text)
    # 转换匹配到的十六进制数字为 Unicode 字符
    decoded_chars = [chr(int(seq, 16)) for seq in unicode_sequences]
    # 替换原始文本中的序列为解码后的字符
    decoded_text = text
    for seq, char in zip(unicode_sequences, decoded_chars):
        decoded_text = decoded_text.replace('u' + seq, char)
    return decoded_text