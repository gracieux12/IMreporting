import logging
from IMreporting.arguments import get_args
from IMreporting.get_file import Tasks

_logger = logging.getLogger(__name__)


def main(args):
    """
    :param args: Command line argument

    """

    Tasks.generate_report(args.teamap, args.p, args.s, args.team_report, args.production_report)


if __name__ == "__main__":
    args = get_args()
    logging.basicConfig(level=args.log_lvl)
    _logger.info("Beginning Execution")
    _logger.debug("Debug level logging enabled")
    main(args)
    _logger.info("Execution Complete")
