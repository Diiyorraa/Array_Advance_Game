def two_sum(A, target):
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i]+ A[j] == target:
                print(A[i],",",A[j])
                return True
    return False

A=[1,2,3,4,5]
target = 8
print(two_sum(A, target))

A= [7,8,9,10]
target = 23
print(two_sum(A, target)) # here two_sum approach takes O(n in square) time to solve , as we are using two loops

#here is second solution

def two_suum_hash_table(A, target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target-A[i]] = A[i]
    return False

A= [-1,2,6,7,34]
target = 13
print(two_suum_hash_table(A, target)) # here two_suum_hash_table approach takes O(N) time to solve

#buy and sell stocks

