import argparse

from .getip import getip


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="getip",
        description="Simple script for getting your IP"
    )
    parser.add_argument(
        "-s", "--server",
        help="Server IP",
        default="ifconfig.me"
    )

    args = parser.parse_args()
    print(getip(args.server))
