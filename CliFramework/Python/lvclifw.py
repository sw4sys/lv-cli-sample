import argparse


def parser() -> argparse.ArgumentParser:
    root_parser = argparse.ArgumentParser(
        prog='lvclifw',
        description='Send commands to running LabVIEW application.'
        )
    root_subparsers = root_parser.add_subparsers(
        title='commands',
        description='List of available commands:',
        dest='cmd'
    )
    root_subparsers.add_parser(
        name='ping',
        help='Ping LabVIEW application.'
    )
    return root_parser
