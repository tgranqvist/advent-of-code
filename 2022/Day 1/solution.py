if __name__ == "__main__":
    elf_calories = []

    with open("input.txt", "r") as data:
        calories = 0
        for line in data:
            if line in ['\n', '\r\n']:
                elf_calories.append(calories)
                calories = 0
                continue

            calories += int(line, base=10)

    print(elf_calories)
    print(max(elf_calories))
    print(sum(sorted(elf_calories, reverse=True)[:3]))