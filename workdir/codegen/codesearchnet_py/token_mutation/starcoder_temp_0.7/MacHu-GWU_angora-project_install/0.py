def install():
    """Manual and of script.
    """
    parser = argparse.ArgumentParser(
        description="Install and setup dotfiles and packages.")
    parser.add_argument(
        "-s",
        "--setup",
        action="store_true",
        help="Setup and install software and dotfiles.")
    parser.add_argument(
        "-c",
        "--clean",
        action="store_true",
        help="Remove temporary files created during installation.")

    args = parser.parse_args()

    install_packages()
    install_dotfiles()
    install_fonts()

    if args.setup:
        setup_shell()
        setup_vim()
        setup_i3()

    if args.clean:
        clean()


