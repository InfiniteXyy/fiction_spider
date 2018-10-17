from math import ceil


def create_page_index(count: int, page_size: int, sort: str = "asc") -> list:
    # count -> 32, page_size -> 12
    # return [
    #     "第 1 - 12 章",
    #     "第 13 - 24 章",
    #     "第 25 - 31 章",
    # ]

    page_count = ceil(count / page_size)
    result = []
    start, end = 0, 0
    if sort == "asc":
        for i in range(page_count - 1):
            start = i * page_size + 1
            end = start + page_size - 1
            result.append("第 {} - {} 章".format(start, end))
        result.append("第 {} - {} 章".format(end + 1, count - 1))
    elif sort == "desc":
        for i in range(page_count - 1):
            start = count - 1 - i * page_size
            end = start - page_size + 1
            result.append("第 {} - {} 章".format(start, end))
        result.append("第 {} - {} 章".format(end - 1, 1))
    return result


if __name__ == '__main__':
    print(create_page_index(32, 12, "desc"))
