# !/usr/bin/env python3

"""The main script."""

from page_loader import engine


def main():
    """Parse arguments from CLI and load page."""
    args = engine.parser.parse_args()
    engine.load_page(
        args.output,
        args.url,
    )


if __name__ == '__main__':
    main()
