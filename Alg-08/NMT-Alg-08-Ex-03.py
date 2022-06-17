def palindromo(s):
    return (len(s) < 2) or ((s[0]==s[-1]) and palindromo(s[1:-1]))

print(palindromo("nattan"))