if __name__ == '__main__':
    n = int(input())
    arr = list(input().split())
    arr1 = [int(i) for i in arr]
    m = max(arr1)
    arr_new = [i for i in arr1 if i != m]
    print(max(arr_new))