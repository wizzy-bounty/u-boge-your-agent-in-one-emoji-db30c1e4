import os

ENTRY = "🐙"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as fh:
        fh.write(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
