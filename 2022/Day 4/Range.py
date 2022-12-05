class Range():

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def contains(self, other: "Range") -> bool:
        """Check if this range completely contains another range"""
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other) -> bool:
        """Check if this range overlaps with another range"""
        pass

    def __str__(self) -> str:
        return f"Range of {self.start}..{self.end}"

    @classmethod
    def parse_range(cls, range) -> "Range":
        start, end = map(int, range.split("-"))
        return Range(start, end)