import subprocess
from pathlib import Path
from typing import Tuple, Optional
from config import FormatSpec

def generate_unique_path(target_folder: Path, base_name: str, extension: str) -> Path:
    """Generates a non-conflicting path if a file with the same name exists."""
    candidate = target_folder / f"{base_name}.{extension}"
    counter = 1
    while candidate.exists():
        candidate = target_folder / f"{base_name} ({counter}).{extension}"
        counter += 1
    return candidate

def convert_audio(source_path: Path, output_folder: Path, target_format: FormatSpec) -> Tuple[bool, str, Optional[Path]]:
    """Converts an audio file using FFmpeg, returning status, message, and target path."""
    dest_path = generate_unique_path(output_folder, source_path.stem, target_format.extension)
    
    cmd = [
        "ffmpeg",
        "-y",
        "-hide_banner",
        "-loglevel", "error",
        "-i", str(source_path.resolve())
    ]
    
    if target_format.ffmpeg_codec:
        cmd.extend(["-c:a", target_format.ffmpeg_codec])
        
    if target_format.extra_args:
        cmd.extend(target_format.extra_args)
        
    cmd.append(str(dest_path.resolve()))

    try:
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if process.returncode == 0:
            return True, "Success", dest_path
        else:
            err_msg = process.stderr.strip() or "FFmpeg encoding error"
            return False, err_msg, None
    except Exception as e:
        return False, str(e), None