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


# 示例文本
encoded_text = "u6211u521au521au63d0u95eeu4e86u4ec0u4e48"

# 解码文本
decoded_text = decode_unicode_sequences(encoded_text)

# 打印解码后的文本
print(decoded_text)