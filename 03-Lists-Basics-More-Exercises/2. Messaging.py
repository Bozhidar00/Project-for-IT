def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def send_message(numbers, text):
    message = ''
    text_length = len(text)

    for number in numbers:
        index = sum_of_digits(number)
        while index >= text_length:
            index -= text_length
        message += text[index]
        text = text[:index] + text[index+1:]

    return message

numbers = input().split()
numbers = [int(num) for num in numbers]
text = input()

result = send_message(numbers, text)
print(result)
