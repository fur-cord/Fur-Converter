# Katt-Converter

Katt-Converter is a simple, interactive command-line audio converter built with Python and FFmpeg. It provides an easy to use terminal interface for converting audio files between multiple formats without requiring complicated commands.

The converter lets the user:

* Choose a target audio format using an interactive arrow-key menu.
* Enter a source folder containing the audio files to convert.
* Automatically convert supported audio files using FFmpeg.
* Save converted files into a dedicated `Katt-Converted` output folder.
* Display clear success, skipped, and failed conversion results.
* Use format-specific FFmpeg codecs and quality settings.

### Supported Formats

* WAV — PCM 16-bit
* MP3 — LAME encoder with high-quality VBR settings
* FLAC — Lossless FLAC
* OGG — Vorbis
* M4A — AAC
* AAC — Raw AAC
* OPUS — Opus
* WMA — WMA2
* AIFF — PCM 16-bit Big Endian
* AC3 — 384 kbps
* ALAC — Lossless Apple Audio Codec

### Interface

Katt-Converter uses `InquirerPy` for interactive menus and `Colorama` for colored terminal output. The interface is designed to be simple and beginner-friendly, with arrow-key navigation and clear conversion status messages.

The format configuration is separated into its own `config.py` file using `FormatSpec` dataclasses, making it easy to add or modify supported formats and FFmpeg settings in the future.

### Goal

The goal of Katt-Converter is to provide a lightweight, fast, and user-friendly audio conversion tool that makes batch audio conversion as simple as selecting a format and choosing a folder.
---
*Made with 💜 by Katt-Dev*
