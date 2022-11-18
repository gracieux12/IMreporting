import logging
from IMreporting.arguments import get_args

_logger = logging.getLogger(__name__)


def main(args):
    """
    :param args: Command line argument

    """


if __name__ == "__main__":
    args = get_args()
    logging.basicConfig(level=args.log_lvl)
    _logger.info("Beginning Execution")
    _logger.debug("Debug level logging enabled")
    main(args)
    _logger.info("Execution Complete")
