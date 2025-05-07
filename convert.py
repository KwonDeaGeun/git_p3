def convert_p6_file_to_p3(input_path: str, output_path: str):
    with open(input_path, 'rb') as f:

        magic_number = f.readline().strip()
        if magic_number != b'P6':
            raise ValueError("Not a P6 PPM file.")


        def read_non_comment_line():
            while True:
                line = f.readline()
                if not line.startswith(b'#'):
                    return line.strip()

        dimensions = read_non_comment_line()
        width, height = map(int, dimensions.split())
        max_val = int(read_non_comment_line())


        pixel_data = f.read(width * height * 3)


    with open(output_path, 'w') as out:
        out.write("P3\n")
        out.write(f"{width} {height}\n")
        out.write(f"{max_val}\n")

        for i in range(0, len(pixel_data), 3):
            r, g, b = pixel_data[i], pixel_data[i+1], pixel_data[i+2]
            out.write(f"{r} {g} {b}\n")



convert_p6_file_to_p3('/home/data/colorP6File.ppm', './colorP3File.ppm')
