# 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant.sort()
    completion.sort()

    # 하나하나 대조해가면서 보다가 같은 인덱스에 안맞는 인원이 있으면 그 사람이 완주 못한 사람인 것.
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
    return participant[len(participant) - 1]
