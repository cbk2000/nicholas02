INPUT="$1"
OUTPUT="$2"

if [ ! -d "$INPUT" ]; then
	echo "Input directory doesn't exist, exiting status 1"
	exit 1
fi

INPUT_FILE="${INPUT}DUMMY-REGISTRATION.csv.zip"

if [ ! -d "$OUTPUT" ]; then
	echo "Output directory doesn't exist, creating output directory"
	mkdir $OUTPUT
fi

unzip "$INPUT_FILE" -d $OUTPUT
