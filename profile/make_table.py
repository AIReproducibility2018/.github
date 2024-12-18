import pandas as pd
import json
from ast import literal_eval

with open("./data/paper_mapping_dict.py") as f:
    s = f.read()

#d = json.loads(s)
d = literal_eval(s)

df = pd.DataFrame(d)
df = df.set_index("id")
df["note"] = df["note"].fillna("")
print(df)


markdown = df.to_markdown()

print("\n-------- MARKDOWN --------\n")
print(markdown)
print("\n-------- MARKDOWN --------\n")


if __name__ == '__main__':
    with open("tmp_output_markdown_paper_table.md", "w") as f:
        f.write(markdown)
