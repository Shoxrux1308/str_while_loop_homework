def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    k=0
    while i<len(str(s)):
        k+=int(str(s)[i])
        i+=1
    return k
print(main(123456))