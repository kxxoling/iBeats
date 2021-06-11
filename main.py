import re
import argparse

GITHUB_README_COMMENTS = (
    "(<!--START_SECTION:{name}-->\n)(.*)(<!--END_SECTION:{name}-->\n)"
)

HEART_RATE_STAT_TEMPLATE = "| {time} | {value} |\n"

def replace_readme_comments(file_name, comment_str, comments_name):
    with open(file_name, "r+") as f:
        text = f.read()
        # regrex sub from github readme comments
        text = re.sub(
            GITHUB_README_COMMENTS.format(name=comments_name),
            r"\1{}\n\3".format(comment_str),
            text,
            flags=re.DOTALL,
        )
        f.seek(0)
        f.write(text)
        f.truncate()


def parse_ios_str_to_list(list_str):
	pass


def main(time_list_str, value_list_str):
	print(time_list_str, value_list_str)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("time_list_str", help="time_list_str")
    parser.add_argument("value_list_str", help="value_list_str")
    options = parser.parse_args()
    main(
        options.time_list_str,
        options.value_list_str,
    )