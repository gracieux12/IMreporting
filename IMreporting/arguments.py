import argparse
from argparse import Namespace


def get_args() -> Namespace:
    """
    :param t : TeamMap.csv
    :param p : ProductMaster.csv
    :param s : Sales.csv
    :param team-report : TeamReport.cvs
    :param product-report : ProductReport.cv

    :return: argpaese Namespace object parsed arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-t", "--teamap",
        help="enter TeamMap.csv",
        required=True,
    )
    parser.add_argument(
        "-p",
        help=" enter Product file",
        required=True,
    )

    parser.add_argument(
        "-s",
        help=" enter Sales.cvs",
        required=True,
    )

    parser.add_argument(
        "--team-report",
        help=" enter TeamReport.cvs",
        required=True,
    )

    parser.add_argument(
        "--production-report", help="enter ProductReport.cdv", required=True
    )
    parser.add_argument(
        "--log-lvl",
        help="Logging level",
        choices=["DEBUG", "INFO", "WARN", "ERROR"],
        default="INFO",
        type=str.upper,
    )
    args = parser.parse_args()

    return args
