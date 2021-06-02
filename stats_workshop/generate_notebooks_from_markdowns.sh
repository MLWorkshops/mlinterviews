# find all markdown files in the current folder
echo "Generating notebook files for the following markdown files:"
for i in *.md; do
    [ -f "$i" ] || break
    # make sure it is not a README.md file
    if [[ "${i}" != "README.md" ]];then
      notedown $i -o
      echo $i
    fi
done
