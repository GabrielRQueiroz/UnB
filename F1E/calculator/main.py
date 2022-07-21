import argparse
from stdev_m import stdev_m
from numpy import mean

parser = argparse.ArgumentParser(description="Calculate:\n > Mean standard deviation")

parser.add_argument(
    "values",
    metavar="V",
    type=float,
    nargs="+",
    help="List of one or more space-separated values.",
)
parser.add_argument(
    "--stdev_m", "-MD", action="store_true", help="return the values' mean standard variation",
)
parser.add_argument(
    "--mean", "-M", action="store_true", help="return the values' mean",
)


args = parser.parse_args()

values = args.values

if __name__ == "__main__":
    if args.stdev_m:
        print(f"> Standard deviation: {stdev_m(values)}")

    if args.mean:
        print(f"> Mean: {mean(values)}")

