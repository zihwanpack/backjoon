def get_next_number(number):
    # 짝수라면 그냥 1 더하면 된다.
    if number % 2 == 0:
        return number + 1
    # 홀수라면 7과 같은 수 때문에 무조건 '0' 앞에 붙이기
    binary_str = "0" + bin(number)[2:]
    last_zero_index = binary_str.rfind("0")
    next_binary_str = (
        binary_str[:last_zero_index] + "10" + binary_str[last_zero_index + 2 :]
    )

    return int(next_binary_str, 2)


def solution(numbers):
    answer = []

    for number in numbers:
        next_number = get_next_number(number)
        answer.append(next_number)

    return answer
