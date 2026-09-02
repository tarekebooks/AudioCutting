import subprocess
from pathlib import Path

def split_mp3(input_file, output_dir="output", chunk_duration=60):
    """
    Split an MP3 into multiple files without re-encoding.

    Parameters:
        input_file      : Path to the MP3
        output_dir      : Folder where chunks will be saved
        chunk_duration  : Duration of each chunk in seconds
                          600 = 10 minutes
                          300 = 5 minutes
                          1800 = 30 minutes
    """

    input_file = Path(input_file)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    output_pattern = output_dir / f"{input_file.stem}_part_%03d.mp3"

    command = [
        "ffmpeg",
        "-i", str(input_file),
        "-map", "0:a",
        "-c", "copy",
        "-f", "segment",
        "-segment_time", str(chunk_duration),
        "-reset_timestamps", "1",
        str(output_pattern)
    ]

    print("Splitting audio...")
    print(f"Input: {input_file}")
    print(f"Chunk duration: {chunk_duration} seconds")

    subprocess.run(command, check=True)

    print("\nDone!")
    print(f"Files saved to: {output_dir}")