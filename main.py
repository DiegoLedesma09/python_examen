import os
import sys

if __name__ == "__main__":
    package_dir = os.path.join(os.path.dirname(__file__), "src")
    if package_dir not in sys.path:
        sys.path.insert(0, package_dir)

    from deseq_utils import main
    main()
