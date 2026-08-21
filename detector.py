import json
import subprocess
from pathlib import Path
from typing import Optional

def is_audio_file(file_path: Path) -> bool:
    """Uses ffprobe to detect if a file contains a valid audio stream."""
    cmd = [
        "ffprobe",
        "-v", "quiet",
        "-print_format", "json",
        "-show_streams",
        str(file_path.resolve())
    ]
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        data = json.loads(result.stdout)
        streams = data.get("streams", [])
        return any(stream.get("codec_type") == "audio" for stream in streams)
    except Exception:
        return False

def get_audio_codec(file_path: Path) -> Optional[str]:
    """Retrieves the primary audio codec name of the file."""
    cmd = [
        "ffprobe",
        "-v", "quiet",
        "-print_format", "json",
        "-show_streams",
        "-select_streams", "a:0",
        str(file_path.resolve())
    ]
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        data = json.loads(result.stdout)
        streams = data.get("streams", [])
        if streams:
            return streams[0].get("codec_name")
    except Exception:
        pass
    return None