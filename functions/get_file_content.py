import os
from config import CHARACTER_LIMIT


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" is not a file'

    try:
        with open(target_file, "r") as f:
            content = f.read(CHARACTER_LIMIT)
            if os.path.getsize(target_file) > CHARACTER_LIMIT:
                content += (
                    f'[...File "{file_path} truncated at {CHARACTER_LIMIT} characters'
                )

        return content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
