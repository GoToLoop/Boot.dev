import shlex
import shutil
import pathlib


def parse_shebang_windows(file_path):
  """Parses the first line of a file for a shebang and returns a tuple:

  (executable, list_of_args)
  """
  try:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
      first_line = f.readline().strip()
      if not first_line.startswith("#!"):
        return None, []

      # Strip '#!' and split safely using shlex
      parts = shlex.split(first_line[2:])
      if not parts:
        return None, []

      executable = parts[0]
      args = parts[1:]

      # Handle Unix-style /usr/bin/env or /bin/env wrappers
      # e.g., "#!/usr/bin/env python3 -v" -> executable='python3', args=['-v']
      if pathlib.Path(executable).name.lower() in ("env", "env.exe"):
        if args:
          executable = args[0]
          args = args[1:]
        else:
          return None, []

      # Optional: Resolve short command names (like 'python3') via Windows PATH
      resolved_exe = shutil.which(executable)
      if resolved_exe:
        executable = resolved_exe

      return executable, args

  except Exception as e:
    print(f"Error parsing shebang: {e}")

  return None, []


# --- Example Usage ---
# exe, args = parse_shebang_windows("myscript.py")
# print(f"Executable: {exe}")
# print(f"Arguments: {args}")