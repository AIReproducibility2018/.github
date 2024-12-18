This directory contains the README.md that will appear on the landing page of the Github project,
which contains each of the paper-repositories.

The script `make_table.py` reads the structured specification that maps papers to repositories from
`data/paper_mapping_dict.py` and produces an output-file with a markdown table. The temporary output
file is called `tmp_output_markdown_paper_table.md`, but this is subject to change.

In any case, the resulting markdown table can be copied into README.md, to appear on the landing page.

Alternative ways to make tables from the temporary output file:

- `python3 make_table.py && pandoc -f markdown tmp_output_markdown_paper_table.md -t plain`
- `python3 make_table.py && pandoc -f markdown tmp_output_markdown_paper_table.md -t rst`

Note that the gfm format (github flavour markdown?) adds a \ infront of underscores,
so it breaks certain naive URLs.
