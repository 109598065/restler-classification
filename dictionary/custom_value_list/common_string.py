import random
import string

whitespace = [' ', '\u1680', '\u2000', '\u2001', '\u2002', '\u2003', '\u2004', '\u2005', '\u2006',
              '\u2007', '\u2008', '\u2009', '\u200A', '\u2028', '\u2029', '\u202F', '\u205F', '\u3000', '\u00A0']
control_chars = ['\r\n', '\u0007', '\u0008', '\u0009', '\n', '\u000B', '\u000C', '\r', '\u200B', '\u200C', '\u200D',
                 '\u200E',
                 '\u200F', '\u202A', '\u202B', '\u202C', '\u202D', '\u202E', '\u2060', '\u2061', '\u2062', '\u2063',
                 '\u2064', '\u206D',
                 '\u0015', '\u0016', '\u0017', '\u0018', '\u0019', '\u001A', '\u001B', '\u001C', '\u001D', '\u001E',
                 '\u001F', '\u007F',
                 '\u0080', '\u0081', '\u0082', '\u0083', '\u0085', '\u0086', '\u0087', '\u0088', '\u008A', '\u008B',
                 '\u008C', '\u008D',
                 '\u0090', '\u0091', '\u0093', '\u0094', '\u0095', '\u0096', '\u0097', '\u0098', '\u0099', '\u009A',
                 '\u009B', '\u009C',
                 '\u009D', '\u009E', '\u009F', '\uFEFF', '\uFFFE', '\u00AD']
abugidas_chars = ['జ్ఞ\u200Cా', 'স্র\u200Cু']
single_code_point_emojis = ['\uD83E\uDD76', '\uD83D\uDC80', '\uD83D\uDC7B', '\uD83D\uDC7E']
multi_code_point_emojis = ['\uD83D\uDC69\uD83C\uDFFE', '\uD83D\uDC68\u200D\uD83C\uDFED',
                           '\uD83D\uDC69\u200D\uD83D\uDE80']
punctuation = list(string.punctuation)
null_chars = ['']

random_generate = []
i = 5
for _ in range(100):
    size = random.randint(i, i + 10)
    random_generate.append(''.join(random.choices(string.ascii_letters + string.digits, k=size)))

common_strings = whitespace + control_chars + abugidas_chars + single_code_point_emojis + multi_code_point_emojis + punctuation + null_chars + random_generate
