
def swap_case(s):
    
    result = list(s)
    for i in range(len(s)):
        if s[i].isalpha() == True:
            if s[i].isupper() == True:
                result[i] = s[i].lower()
            elif s[i].islower() == True:
                result[i] = s[i].upper()

    end_result="".join(result)

    return end_result
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
