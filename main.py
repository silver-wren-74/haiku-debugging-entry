HAIKU = """Midnight, one last run
a stray print line spills the truth
and the bug was mine"""


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
