
from Range import Range

if __name__ == "__main__":
    with open("sections.txt", "r") as sections:
        overlapped_count = 0
        for assignment in sections:
            r1, r2 = map(Range.parse_range, assignment.strip().split(","))
            if any([r1.overlaps(r2), r2.overlaps(r1)]):
                overlapped_count += 1

        print(overlapped_count)