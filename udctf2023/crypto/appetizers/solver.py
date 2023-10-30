def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # If the sum of the current subset equals the target, print the flag
    if s == target:
        flag = "UDCTF{%s}" % ("_".join(map(str, partial)))
        print("Flag:", flag)
    
    # If the sum of the current subset exceeds the target, stop exploring this path
    if s >= target:
        return
    
    # Recursively try including and excluding elements from the subset
    for i in range(len(numbers)):
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [numbers[i]])

# Your list of numbers and target sum
choices = [19728964, 30673077, 137289540, 195938621, 207242611, 237735979, 298141799, 302597011, 387047012, 405520686, 424852916, 461998372, 463977415, 528505766, 557896298, 603269308, 613528675, 621228168, 654758801, 670668388, 741571487, 753993381, 763314787, 770263388, 806543382, 864409584, 875042623, 875651556, 918697500, 946831967]
target = 7627676296

# Call the subset_sum function to find and print the flag
subset_sum(choices, target)