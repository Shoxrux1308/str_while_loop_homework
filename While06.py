def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    i=0
    k=0
    while i<len(s):
        if s[i] in 'a, e, i, o, u,A,E,I,U,O':
            k+=1
        i+=1
    return len(s)-k
print(main('CodeschoolUz'))