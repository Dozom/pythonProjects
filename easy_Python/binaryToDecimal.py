number = str(input("Introduce your binary number: "))
binari = number[::-1];
answer = 0;
for i in range(len(binari)):
    if binari[i] == "1":
        answer += 2**i;
print(answer)
        
