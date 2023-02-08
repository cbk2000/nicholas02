INPUT=../input
OUTPUT=../output

if [ ! -d "$INPUT" ]; then
	echo "Input directory doesn't exist, exiting status 1"
	exit 1
fi

INPUT_FILE="${INPUT}/OS231 REGISTRATION.csv.zip"

if [ ! -d "$OUTPUT" ]; then
	echo "Output directory doesn't exist, creating output directory"
	mkdir $OUTPUT
fi

unzip "$INPUT_FILE" -d $OUTPUT
