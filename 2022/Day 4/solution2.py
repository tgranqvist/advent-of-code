
from Range import Range

if __name__ == "__main__":
    with open("sections.txt", "r") as sections:
        contained_count = 0
        for assignment in sections:
            a1, a2 = assignment.strip().split(",")
            print(f"Found assignments {a1} and {a2}")
            r1, r2 = Range.parse_range(a1), Range.parse_range(a2)
            if any([r1.contains(r2), r2.contains(r1)]):
                contained_count += 1

        print(contained_count)