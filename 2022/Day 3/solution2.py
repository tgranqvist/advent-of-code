import string

PRIORITIES = {
    ltr:idx for (idx, ltr) in enumerate(string.ascii_letters, start=1)
}

def identify_badge(data: str) -> str:
    return list(set(data[0]) & set(data[1]) & set(data[2]))[0]

if __name__ == "__main__":
     with open("contents.txt", "r") as contents:
        temp = []
        common = []
        for idx, rucksack in enumerate(contents, start=1):
            rucksack = rucksack.strip()
            temp.append(rucksack)
            if not idx % 3:
                common.append(identify_badge(temp))
                temp = []
        total = sum(PRIORITIES[p] for p in common)
        print(f"Total is {total}")