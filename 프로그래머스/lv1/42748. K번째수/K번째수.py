def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        res = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(res[commands[i][2]-1])
    return answer