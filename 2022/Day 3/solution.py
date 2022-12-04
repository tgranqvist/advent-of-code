import string

PRIORITIES = {
    ltr:idx for (idx, ltr) in enumerate(string.ascii_letters, start=1)
}

if __name__ == "__main__":
     with open("contents.txt", "r") as contents:
        common = []
        for rucksack in contents:
            rucksack = rucksack.strip()
            half = len(rucksack) // 2
            upper, lower = set(rucksack[0:half]), set(rucksack[half:])
            common.append(list(upper & lower)[0])
            print(f"upper compartment stuff: {upper}, lower compartment stuff: {lower}.")
        
        total = sum(PRIORITIES[p] for p in common)
        print(f"Total is {total}")