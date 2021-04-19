"""Use the pandoc library as a final step to build the pdf.

This is done once the duplicate src directory is processed.
"""
import os
import pathlib
import subprocess
import re

def sorted_nicely(lst):
    sort_lst=[x for x in lst if '_' in os.path.basename(x)]
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    sorted_lst = sorted(sort_lst, key = alphanum_key)
    prepend=[x for x in lst if '_' not in os.path.basename(x)]
    
    return prepend+sorted_lst

def build_pdf(filename):
    """Construct command with required pandoc flags and run using subprocess.

    Parameters
    ----------
    filename : str
        Name of the output file.

    """
    # Get all input files
    markdown_list = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(".md") and file != 'index.md':
                markdown_list.append(os.path.join(root, file))
            elif file == 'index.md':
                index_page = os.path.join(root, file)

    # Prepare the command options
    cmd = [
        'pandoc',
        '--from=gfm',
        '--include-before-body=./cover.tex',
        '--toc',
        '--toc-depth=4',
        '--listings',
        '--include-in-header=./header.tex',
        '--include-in-header=./header_setup.tex',
        '-V documentclass=article',
        '-V linkcolor:blue',
        '-V mainfont:Arial',
        '-V geometry:margin=.5in',
        '--pdf-engine=xelatex',
        '--output={}'.format(filename),
    ]

    # Add input files to command
    # The filenames in `markdown_list` will ensure correct order when sorted
    root = pathlib.Path(__file__).parent.absolute()
    cmd += [str(root / index_page)]
    cmd += [str(root / i) for i in sorted_nicely(markdown_list)]

    # print and run
    print('running: \n\n' + '\n'.join(cmd))
    subprocess.run(cmd)


if __name__ == "__main__":
    build_pdf('edf2bids-spec.pdf')
