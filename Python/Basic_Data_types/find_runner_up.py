
if __name__ == '__main__':
    n = int(input())  # input n
    arr = input().split()  # an array
    arr = [int(x) for x in arr]  # convert to int

    m = max(arr)  # find the max value

    arr = [x for x in arr if x != m]  # arrange the list without max value

    m = max(arr)  # get the max value from the new list
    print(m)  # runner-up
