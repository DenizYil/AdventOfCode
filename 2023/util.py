import os
import requests
import dotenv

dotenv.load_dotenv()

ADVENT_MAIN = os.environ["ADVENT_MAIN"]
ADVENT_ALT = os.environ["ADVENT_ALT"]

YEAR = 2022

def _load_data_from_web(session, day):
    url = "https://adventofcode.com/{YEAR}/day/{day}/input"
    resp = requests.get(url, headers={"Cookie": f'session={session}'})
    resp.raise_for_status()
    return resp.text.splitlines()

def _submit_answer(session, day, answer, part):
    url = f"https://adventofcode.com/{YEAR}/day/{day}/answer"
    resp = requests.post(
        url,
        headers={"Cookie": f'session={session}'},
        data={"level": part, "answer": answer},
    )
    resp.raise_for_status()
    print(resp.text)

def load_data(day):
    main = _load_data_from_web(ADVENT_MAIN, day)
    alt = _load_data_from_web(ADVENT_ALT, day)

    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'w') as f:
        f.write('\n'.join(main))

    with open(os.path.join(os.path.dirname(__file__), 'input_alt.txt'), 'w') as f:
        f.write('\n'.join(alt))

def submit_answer(day, answer, part, alt=False):
    if alt:
        _submit_answer(ADVENT_ALT, day, answer, part)
    else:
        _submit_answer(ADVENT_MAIN, day, answer, part)
