
from Range import Range

if __name__ == "__main__":
    with open("sections.txt", "r") as sections:
        contained_count = 0
        for assignment in sections:
            r1, r2 = map(Range.parse_range, assignment.strip().split(","))
            if any([r1.contains(r2), r2.contains(r1)]):
                contained_count += 1

        print(contained_count)