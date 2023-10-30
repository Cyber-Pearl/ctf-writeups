# Classic Checkers (500 points)

https://gist.github.com/AndyNovo/f1d9d18cbdbc4901066234077dac9b90

```lisp
(defun checkFlag (input)
    (if (not (= (length input) 34))
        nil
        (if (not (string= (subseq input 0 6) "UDCTF{"))
            nil
            (if (not (= (char-code (char input 6)) 104))
                nil
                (if (not (= (+ (char-code (char input 9)) 15) (- (char-code (char input 8)) (char-code (char input 7)))))
                    nil
                    (if (not (= (* (char-code (char input 7)) (char-code (char input 9))) 2652))
                        nil
                        (if (not (= (- (char-code (char input 7)) (char-code (char input 9))) 1))
                            nil
                            (if (not (string= (char input 10) (char input 14) ) )
                                nil
                                (if (not (string= (char input 14) (char input 21) ) )
                                    nil
                                    (if (not (string= (char input 10) (char input 25) ) )
                                        nil
                                        (if (not (string= (char input 21) (char input 27) ) )
                                            nil
                                            (if (not (= (ceiling (char-code (char input 10)) 2) (char-code (char input 12)) ) )
                                                nil
                                                (if (not (=  952 (- (expt (char-code (char input 11)) 2) (expt (char-code (char input 13)) 2)) ) )
                                                    nil
                                                    (if (not (string= (subseq input 14 21) (reverse "sy4wla_")))
                                                        nil
                                                        (if (not (string= (subseq input 22 24) (subseq input 6 8)))
                                                            nil
                                                            (if (not (= (mod (char-code (char input 24)) 97)  3))
                                                                nil
                                                                (if (not (string= (subseq input 14 16) (reverse (subseq input 26 28))))
                                                                    nil
                                                                    (if (not (= (complex (char-code (char input 28)) (char-code (char input 29)))  (conjugate (complex 76 -49))))
                                                                        nil
                                                                        (if (not (= (lcm (char-code (char input 30)) (char-code (char input 31))) 6640))
                                                                            nil
                                                                            (if (not (> (char-code (char input 30)) (char-code (char input 31)) ) )
                                                                                nil
                                                                                (if (not (= (char-code (char input 32)) (- (+ (char-code (char input 31)) (char-code (char input 30))) (char-code (char input 24)))))
                                                                                    nil
                                                                                    (if (not (= (char-code (char input 33)) 125))
                                                                                        nil
                                                                                        t))))))))))))))))))))))

(print (checkFlag "FLAGHERE"))
```

The code was written in Lisp, a family of programming languages known for their unique syntax and strong support for symbolic reasoning and recursion. In this specific code snippet, a function named checkFlag is defined, which takes a single argument (input) and performs a series of conditional checks on it. If all the conditions are met, the function returns t (true), indicating that the input string satisfies the specified criteria. 

Breaking down the conditions step by step:

1. The input must be exactly 34 characters long.
2. The first 6 characters must be "UDCTF{".
3. The 7th character must have a character code of 104 ('h').
4. The 10th character's code plus 15 must equal the difference  between the 8th and 7th character codes.
5. The product of the 7th and 9th character codes must be 2652.
6. The difference between the 7th and 9th character codes must be 1.
7. The 10th character must be equal to the 14th character.
8. The 14th character must be equal to the 21st character.
9. The 10th character must be equal to the 25th character.
10. The 21st character must be equal to the 27th character.
11. The ceiling of the 10th character's code divided by 2 must equal the 12th character's code.
12. The difference between the squares of the 11th and 13th character codes must be 952.
13. The substring from the 14th to the 21st character must be equal to the reverse of "sy4wla_".
14. The substring from the 22nd to the 24th character must be equal to the substring from the 6th to the 8th character.
15. The 24th character's code modulo 97 must be 3.
16. The substring from the 14th to the 16th character must be equal to the reverse of the substring from the 26th to the 28th character.
17. The complex number formed by the 28th and 29th character codes must be equal to the complex conjugate of the complex number (76, -49).
18. The least common multiple of the 30th and 31st character codes must be 6640.
19. The 30th character code must be greater than the 31st character code.
20. The 32nd character code must be equal to the sum of the 31st and 30th character codes minus the 24th character code.
21. The 33rd character code must be 125 ('}'). If all these conditions are met, the function returns true.

We manage to convert this to python so that we can easily run and trace the code. Although we can run the LISP code with `clisp` interpreter but we need more readability.


```python
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
```

**FLAG:** UDCTF{h4v3_y0u_alw4ys_h4d_a_L1SP?}