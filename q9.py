def pangram(a):
    alphabet_set=set("abcdefghijklmnopqrstuvwxyz")
    input_Set=set(a.lower())
    
    if alphabet_set <=input_Set:
        return True
    return False
p=pangram("the quick brown  fox jumps over the lazy dog ")
print(p)
