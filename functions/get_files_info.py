import os

def get_files_info(working_directory, directory=None):
    
    absolute_path = os.path.join(os.path.abspath(working_directory), directory)

    if not absolute_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(absolute_path):
        return f'Error: "{directory}" is not a directory'

    try:
        dir_contents = os.listdir(absolute_path)
    except FileNotFoundError:
        return "Error: File not found"

    strings = []
    for content in dir_contents:
        try:
            is_dir = False
            file_path = os.path.join(absolute_path, content)
        
            file_size = os.path.getsize(file_path)

            if os.path.isdir(file_path):
                is_dir = True
        
            string = f"- {content}: file_size={file_size}, is_dir={is_dir}"
            strings.append(string)
        except OSError as e:
            return f"Error: {e}"

    return "\n".join(strings)
