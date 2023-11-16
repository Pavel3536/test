# def array_diff(a, b):
#     return [x for x in a if x not in b]
# result1 = array_diff([1, 2], [1]) 
# result2 = array_diff([1, 2, 2, 2, 3], [2])
# print(result1)
# print(result2)

# def win_round(your_cards, opponent_cards):
#     your_cards.sort(reverse=True)
#     opponent_cards.sort(reverse=True)
#     your_number = int(str(your_cards[0]) + str(your_cards[1]))
#     opponent_number = int(str(opponent_cards[0]) + str(opponent_cards[1]))
#     return your_number > opponent_number
# print(win_round([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]))  
# print(win_round([1, 2, 3, 4, 5], [9, 8, 7, 6, 5]))  
# print(win_round([4, 3, 4, 4, 5], [3, 2, 5, 4, 1]))  

# def duplicate_digits(number):
#     number_str = str(number)
#     result = ""
#     i = 0
#     while i < len(number_str):
#         current_digit = number_str[i]
#         group_start = i
#         group_end = i
#         while group_end < len(number_str) - 1 and number_str[group_end] == number_str[group_end + 1]:
#             group_end += 1
#         if group_start == group_end:
#             result += current_digit * 3  
#         else:
#             result += number_str[group_start:group_end + 1] * 3 
#         i = group_end + 1
#     return int(result)
# print(duplicate_digits(22733))  
# print(duplicate_digits(123))    
# print(duplicate_digits(56657))
# print(duplicate_digits(33))     

# def count_palindrome_timestamps(start_hours, start_minutes, start_seconds, end_hours, end_minutes, end_seconds):
#     count = 0
#     for hours in range(start_hours, end_hours + 1):
#         for minutes in range(start_minutes, end_minutes + 1):
#             for seconds in range(start_seconds, end_seconds + 1):
#                 timestamp = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
#                 reversed_timestamp = f"{seconds:02d}:{minutes:02d}:{hours:02d}"

#                 if timestamp == reversed_timestamp:
#                     count += 1
#     return count
# print(count_palindrome_timestamps(2, 12, 22, 4, 35, 10)) 
# print(count_palindrome_timestamps(12, 12, 12, 13, 13, 13))  
# print(count_palindrome_timestamps(6, 33, 15, 9, 55, 10))  



