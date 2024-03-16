def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    k=0
    while i<len(str(s)):
        if int(str(s)[i])%2!=0:
            k+=int(str(s)[i])
        i+=1
    return k
print(main(123456))