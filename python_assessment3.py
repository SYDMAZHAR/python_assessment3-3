def count_case_characters(input_str):
    upper_count = 0
    lower_count = 0
    
    for char in input_str:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    return upper_count, lower_count

sample_string = 'The quick Brow Fox'
upper_count, lower_count = count_case_characters(sample_string)

print("Sample String:", sample_string)
print("No. of Upper case characters:", upper_count)
print("No. of Lower case characters:", lower_count)

