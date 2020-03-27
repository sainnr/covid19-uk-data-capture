"""
Parses raw lines of COVID cases by UTLA.
For raw data, credit to Cambridge News who published these for some time:
e.g. https://www.cambridge-news.co.uk/news/uk-world-news/coronavirus-confirmed-cases-england-cambridgeshire-17941049
"""
import json

source = "Source: www.cambridge-news.co.uk"

targets = [
    '13-03.txt',
    '14-03.txt',
    '15-03.txt',
    '16-03.txt',
    '17-03.txt',
]

if __name__ == "__main__":
    for t in targets:
        with open(t, 'r') as f:
            [prefix, _] = f.name.split('.')
            [d, m] = prefix.split('-')
            date = "2020-{}-{}".format(m, d)
            lines = f.readlines()
            data = {}
            i = 0
            sum = 0
            for l in lines:
                if l and len(l.strip()):
                    [k, v] = l.split(':')
                    curCases = int(v.strip())
                    data[k.strip()] = curCases
                    i += 1
                    sum += curCases

            assembled = {
                "meta": {"total": sum, "entries": i, "date": date, "description": source},
                "data": data
            }
            with open('../by_utla/{}.json'.format(date), 'w') as out:
                json.dump(assembled, out)
