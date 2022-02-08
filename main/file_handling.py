class FileHandling:
    @staticmethod
    def read(file_name):
        lines = []
        with open(file_name, "r") as input_file:
            for line in input_file:
                lines.append(line)
        return lines

    @staticmethod
    def write(file_name, lines):
        with open(file_name, "w") as output_file:
            for line in lines:
                output_file.write(line)
