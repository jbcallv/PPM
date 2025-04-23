def AddArguments(cls, argument_group):
    """Adds command line arguments to an argument group.

    This method takes an argument parser or an argument group arguments and adds
    to it all the command line , this helper supports.

    Args:
      argument_group (argparse._ArgumentGroup|argparse.ArgumentParser):
          argparse group.
    """
    argument_group.add_argument(
        '--output_directory', '--output-directory', dest='output_directory',
        type=str, action='store', help=(
            'The location where the results will be stored.'))
    argument_group.add_argument(
        '--filter', '--filter', dest='filter', type=str, action='store',
        help=(
            'Filter expression to filter the image sources to process.'))


