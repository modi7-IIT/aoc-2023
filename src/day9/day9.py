def parse_input(filename) :
    with open(filename,'r') as f :
        data = [line.strip() for line in f]
        data = [list(map(int,d.split()))for d in data]
        print(data)
        return data


def get_diff_series(series) :
    n = len(series)
    return [series[i+1] - series[i] for i in range(n-1)]


def get_extrapolation(series) :
    if all((val == 0 for val in series)) :
        return 0
    return series[-1] + get_extrapolation(get_diff_series(series))

def get_extrapolation_2(series) :
    if all((val == 0 for val in series)) :
        return 0
    return series[0] - get_extrapolation_2(get_diff_series(series))


def get_ans_1(data) :
    ans = [get_extrapolation(series) for series in data]
    return sum(ans)

def get_ans_2(data) :
    ans = [get_extrapolation_2(series) for series in data]
    return sum(ans)

data = parse_input('day9.txt')
ans = get_ans_2(data)
print(ans)