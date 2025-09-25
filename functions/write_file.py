import os

from google.genai import types


def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(target_file):
        try:
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    if os.path.exists(target_file) and os.path.isdir(target_file):
        return f'Error: "{file_path}" is a directory, not a file'

    try:
        with open(target_file, "w") as f:
            f.write(content)

        return f'Successfuly wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: writing to file: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write text content to a file in the working directory. If the file or its parent directories do not exist, they will be created. Access is restricted to files within the working directory and cannot overwrite directories.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path where the file will be written inside the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The text content to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)
