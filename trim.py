text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(" ")
number = text[pos::1]
sNumber = number.lstrip();
result = float(sNumber)
print(result)
