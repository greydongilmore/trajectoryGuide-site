# Shell script that runs process_markdowns.py and pandoc_script.py in sequence to build the pdf document

# prepare the copied src directory
python3 process_markdowns.py

# copy pandoc_script into the temp src_copy directory
cp pandoc_script.py header.tex cover.tex header_setup.tex docs_copy/docs

# run pandoc_script from src_copy directory
cd docs_copy/docs
python3 pandoc_script.py
mv edf2bids-spec.pdf ../..
cd ../..

# delete the duplicated src directory
#rm -rf docs_copy
