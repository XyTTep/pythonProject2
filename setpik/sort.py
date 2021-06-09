# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97,
#      -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96,
#      -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39,
#      60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71,
#      -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48,
#      39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9,
#      -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
# n = len(a)
# for i in range(n):
#     b = a[:n].index(max(a[:n]))
#     [a[b], a[n - 1]] = [a[n - 1], a[b]]
#     n -= 1
# print(a)
# n = input()
# n3 = 0
# n_last = 0
# n_2 = 0
# n_5 = 0
# n_7 = 1
# n0_5 = 0
# for i in range(len(n)):
#     if int(n[i]) == 3:
#         n3 += 1
#     if int(n[-1]) == int(n[i]):
#         n_last += 1
#     if int(n[i]) % 2 == 0:
#         n_2 += 1
#     if int(n[i]) > 5:
#         n_5 += int(n[i])
#     if int(n[i]) > 7:
#         n_7 *= int(n[i])
#     if int(n[i]) == 0 or int(n[i]) == 5:
#         n0_5 += 1
# print(n3, n_last, n_2, n_5, n_7, n0_5, sep='\n')
# объявление функции
# объявление функции
def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True


#
#
# def is_prime_2(num):
#     while True:
#         num += 1
#         if is_prime(num):
#             return num
#
#
# n = int(input())
# print(is_prime_2(n))
# объявление функции
# def is_password_good(password):
#     nums = '1234567890'
#     small = 'qwertyuiopasdfghjklzxcvbnm'
#     large = 'qwertyuiopasdfghjklzxcvbnm'.upper()
#     if (len(password) >= 8
#         and len(set(nums).intersection(password)) > 0
#         and len(set(small).intersection(password)) > 0
#         and len(set(large).intersection(password))) > 0:
#         return True
#     return False
#
#
# txt = input()
# print(is_password_good(txt))

# def is_one_away(word1, word2):
#     if len(word2) == len(word1) and (len(word1) - len(set(word1).intersection(word2))) == 1:
#         return True
#     else:
#         return False
#
#
# txt1 = input()
# txt2 = input()
#
# print(is_one_away(txt1, txt2))


# объявление функции

# объявление функции

def is_valid_password(password):
    password = password.split(':')
    print(len(password))
    if (len(password) == 3
            and password[0] == password[0][-1::-1]
            and is_prime(int(password[1]))
            and int(password[2]) % 2 == 0):
        return True
    return False


psw = input()
print(is_valid_password(psw))
