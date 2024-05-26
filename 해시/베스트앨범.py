from collections import defaultdict
def solution(genres, plays):
    genre_total = defaultdict(int)
    genre_list = defaultdict(list)

    for i in range(len(genres)):
        genre_total[genres[i]] += plays[i]
        genre_list[genres[i]].append((i,plays[i]))

    sorted_genre_total = sorted(genre_total, key=lambda x: genre_total[x], reverse=True)

    answer=[]
    for i in sorted_genre_total:
        l = sorted(genre_list[i], key=lambda x: x[1], reverse=True)[:2]
        for j in l:
            answer.append(j[0])
    return answer