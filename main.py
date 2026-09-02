from split_mp3 import split_mp3

if __name__ == "__main__":

    split_mp3(
        input_file="./resources/input/input.mp3",
        output_dir="./resources/output",
        chunk_duration=360
    )