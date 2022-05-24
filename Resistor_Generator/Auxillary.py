def rangeCheck(value: int, min: int, max: int) -> int:
    if value < min:
        print("WARNING: Changed value from:", value, "to:", min)
        print("-> Use value within range")
        return min

    if value > max:
        print("WARNING: Changed value from:", value, "to:", max)
        print("-> Use value within range")
        return max

    return value


def toUnsigned(value: int) -> int:
    if value < 0:
        print("WARNING: Changed value from:", value, "to:", -value)
        print("-> Use value within range")
        return -value

    return value
