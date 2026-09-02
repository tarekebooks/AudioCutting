# AudioCutting

A lightweight Python utility for splitting MP3 audio files into multiple smaller audio files with a configurable target duration.

The application uses **FFmpeg** with stream copying, which means the MP3 audio is split **without re-encoding**. This preserves the original audio quality and avoids additional compression.

## Features

* Split an MP3 file into multiple parts.
* Configure the expected duration of each part.
* Supports duration formats such as:

  * Seconds: `90s`
  * Minutes: `5m`
  * Hours: `1h`
  * Combined durations: `1h30m`
* Supports numeric duration values in seconds.
* No audio re-encoding.
* Preserves the original MP3 quality.
* Automatically creates the output directory.
* Sequentially numbers generated files.

## Requirements

### Python

Python 3.9+ is recommended.

Check your Python version:

```bash
python --version
```

### FFmpeg

FFmpeg must be installed and available in your system `PATH`.

Check whether FFmpeg is installed:

```bash
ffmpeg -version
```

If the command is not recognized, install FFmpeg and add its `bin` directory to your system `PATH`.

## Project Structure

Example:

```text
AudioCutting/
│
├── audio_cutting.py
├── input.mp3
├── output/
└── README.md
```

The Python file can have any name. In the examples below, it is assumed to be:

```text
audio_cutting.py
```

## Installation

Clone the repository:

```bash
git clone git@github-work:tarekebooks/AudioCutting.git
```

Enter the project directory:

```bash
cd AudioCutting
```

No external Python package is required if the application only uses Python's standard library.

Make sure FFmpeg is installed:

```bash
ffmpeg -version
```

## Usage

The application exposes a `split_mp3()` function:

```python
split_mp3(
    input_file="input.mp3",
    output_dir="output",
    duration="10m"
)
```

### Parameters

| Parameter    | Description                    | Example       |
| ------------ | ------------------------------ | ------------- |
| `input_file` | Path to the source MP3         | `"input.mp3"` |
| `output_dir` | Directory for generated files  | `"output"`    |
| `duration`   | Expected duration of each part | `"10m"`       |

## Duration Configuration

The duration of the generated parts can be changed directly through the `duration` parameter.

### 5 minutes

```python
split_mp3(
    input_file="input.mp3",
    output_dir="output",
    duration="5m"
)
```

### 10 minutes

```python
split_mp3(
    input_file="input.mp3",
    output_dir="output",
    duration="10m"
)
```

### 30 minutes

```python
split_mp3(
    input_file="input.mp3",
    output_dir="output",
    duration="30m"
)
```

### 1 hour

```python
split_mp3(
    input_file="input.mp3",
    output_dir="output",
    duration="1h"
)
```

### 1 hour 30 minutes

```python
split_mp3(
    input_file="input.mp3",
    output_dir="output",
    duration="1h30m"
)
```

### Duration in seconds

A numeric value can also be used:

```python
split_mp3(
    input_file="input.mp3",
    output_dir="output",
    duration=600
)
```

`600` seconds = 10 minutes.

## Running the Application

Place the source MP3 file in the project directory.

For example:

```text
AudioCutting/
├── audio_cutting.py
├── input.mp3
└── README.md
```

Run:

```bash
python audio_cutting.py
```

The application will create the `output` directory automatically.

Example console output:

```text
Input      : input.mp3
Duration   : 10m
Output     : output

Splitting...

Finished.
```

## Output

For an input file:

```text
input.mp3
```

with a target duration of 10 minutes, the output will look like:

```text
output/
├── input_part_000.mp3
├── input_part_001.mp3
├── input_part_002.mp3
├── input_part_003.mp3
└── ...
```

The final file may be shorter than the requested duration if the source audio ends before another complete chunk can be created.

## Audio Quality

The application uses FFmpeg's stream-copy mode:

```bash
-c copy
```

This means the audio is **not decoded and re-encoded** during splitting.

Advantages:

* No additional lossy compression.
* No additional generation loss.
* Faster processing.
* Original MP3 encoding is preserved.

## Important: Expected Duration vs Exact Duration

The `duration` parameter specifies the **target/expected duration** of each output file.

For example:

```python
duration="10m"
```

requests approximately 10-minute segments.

Because the application uses stream copying, the split can occur at MP3 frame/key boundaries rather than at an arbitrary sample-accurate position. Therefore, the resulting files may not always be exactly:

```text
10:00.000
```

This is intentional because exact arbitrary-duration cutting would generally require re-encoding.

### Why not re-encode?

Re-encoding could provide more precise cutting but would introduce another encoding step and potentially reduce audio quality.

This application prioritizes:

1. Original audio quality
2. Fast processing
3. No unnecessary re-encoding

over sample-perfect duration boundaries.

## Example

Suppose the source file is:

```text
input.mp3
Duration: 47 minutes
```

and the configured duration is:

```python
duration="10m"
```

The application will produce approximately:

```text
input_part_000.mp3
input_part_001.mp3
input_part_002.mp3
input_part_003.mp3
input_part_004.mp3
```

The first four files will be approximately 10 minutes each, while the final file contains the remaining audio.

## Error Handling

If the duration is invalid, the application raises an error.

Valid examples:

```text
90
90s
5m
10m
1h
1h30m
```

Invalid examples:

```text
abc
-10
0m
```

## Troubleshooting

### `ffmpeg is not recognized`

If Windows shows an error such as:

```text
'ffmpeg' is not recognized as an internal or external command
```

FFmpeg is either not installed or its `bin` directory is not in the system `PATH`.

Verify with:

```bash
ffmpeg -version
```

### Input file not found

Make sure the input file exists:

```text
AudioCutting/
└── input.mp3
```

Or provide an absolute path:

```python
split_mp3(
    input_file=r"resources\inputs\input.mp3",
    output_dir="resources\outputs",
    duration="10m"
)
```

## License

This project is intended for personal and educational use.

## Author

**tarekebooks**
