import math

def check_flag(input):
    res = 0
    if len(input) != 34:
        return False
    if input[:6] == "UDCTF{":
        res += 1
        if ord(input[6]) == 104:
            res += 1 
            if (ord(input[9]) + 15) == (ord(input[8]) - ord(input[7])):
                res += 1 
                if (ord(input[7]) * ord(input[9])) == 2652:
                    res += 1 
                    if (ord(input[7]) - ord(input[9])) == 1:
                        res += 1 
                        if input[10] == input[14]:
                            res += 1
                            if input[14] == input[21]:
                                res += 1
                                if input[10] == input[25]:
                                    res += 1
                                    if input[21] == input[27]:
                                        res += 1
                                        if math.ceil(ord(input[10]) // 2) == ord(input[12]):
                                            res += 1
                                            if (952 - (pow(ord(input[11]), 2) - pow(ord(input[13]), 2))) == 0:
                                                res += 1
                                                if input[14:21] == "sy4wla_"[::-1]:
                                                    res += 1
                                                    if input[22:24] == input[6:8]:
                                                        res += 1
                                                        if (ord(input[24]) % 97) == 3:
                                                            res += 1
                                                            if input[14:16] == input[26:28][::-1]:
                                                                res += 1
                                                                if complex(ord(input[28]), ord(input[29])) == complex(76, 49):
                                                                    res += 1
                                                                    if (ord(input[30]) * ord(input[31])) // math.gcd(ord(input[30]), ord(input[31])) == 6640:
                                                                        res += 1
                                                                        if ord(input[30]) > ord(input[31]):
                                                                            res += 1
                                                                            if (ord(input[32]) - (ord(input[31]) + ord(input[30]) - ord(input[24]))) == 0:
                                                                                res += 1
                                                                                if ord(input[33]) == 125:
                                                                                    res += 1
    return res



print(check_flag("UDCTF{h4v3_y0u_alw4ys_h4d_a_L1SP?}"))