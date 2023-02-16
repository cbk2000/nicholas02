parent_dir=$(cd "$(dirname "$0")"; pwd)

input_dir="$parent_dir/../input/"
output_dir="$parent_dir/../output/"
data_csv="DUMMY-REGISTRATION.csv"
csv_output="OS_GH_USERNAME.txt"
quiz_input="input.txt"
quiz_output="output.txt"

bash "$parent_dir/../pdir/unzip.sh" "$input_dir" "$output_dir"
python3 "$parent_dir/../pdir/process.py" <<EOF
"$output_dir$data_csv"
"$output_dir$csv_output"
EOF
python3 "$parent_dir/../pdir/quiz.py" <<EOF
"$input_dir$quiz_input"
"$output_dir$quiz_output"
EOF
