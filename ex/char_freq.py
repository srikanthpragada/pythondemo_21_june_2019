
st = input("Enter a string :")

freq = {}

for ch in st:
    if ch not in freq:
        freq[ch] = st.count(ch)


print(freq)

