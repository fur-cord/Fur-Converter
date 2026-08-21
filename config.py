from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class FormatSpec:
    name: str
    extension: str
    ffmpeg_codec: Optional[str] = None
    extra_args: Optional[list] = None

SUPPORTED_FORMATS: Dict[str, FormatSpec] = {
    "WAV": FormatSpec("WAV", "wav", ffmpeg_codec="pcm_s16le"),
    "MP3": FormatSpec("MP3", "mp3", ffmpeg_codec="libmp3lame", extra_args=["-q:a", "2"]),
    "FLAC": FormatSpec("FLAC", "flac", ffmpeg_codec="flac"),
    "OGG": FormatSpec("OGG (Vorbis)", "ogg", ffmpeg_codec="libvorbis", extra_args=["-q:a", "6"]),
    "M4A": FormatSpec("M4A (AAC)", "m4a", ffmpeg_codec="aac", extra_args=["-b:a", "192k"]),
    "AAC": FormatSpec("AAC Raw", "aac", ffmpeg_codec="aac", extra_args=["-b:a", "192k"]),
    "OPUS": FormatSpec("OPUS", "opus", ffmpeg_codec="libopus", extra_args=["-b:a", "128k"]),
    "WMA": FormatSpec("WMA", "wma", ffmpeg_codec="wmav2", extra_args=["-b:a", "192k"]),
    "AIFF": FormatSpec("AIFF", "aiff", ffmpeg_codec="pcm_s16be"),
    "AC3": FormatSpec("AC3", "ac3", ffmpeg_codec="ac3", extra_args=["-b:a", "384k"]),
    "ALAC": FormatSpec("ALAC", "m4a", ffmpeg_codec="alac"),
}

OUTPUT_FOLDER_NAME = "Katt-Converted"