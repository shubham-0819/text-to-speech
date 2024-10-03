# Markdown to Speech Pipeline

This pipeline converts markdown text files into optimized text for speech synthesis. It provides a flexible foundation that can be easily extended for more advanced features in the future.

## Features

- Reads markdown files and converts them to plain text
- Optimizes text for speech synthesis (expands abbreviations, handles numbers and symbols)
- Supports multiple output formats (plain text and SSML)
- Provides basic customization options
- Includes error handling and logging

## Requirements

- Python 3.6+
- `markdown` library (install with `pip install markdown`)

## Usage

1. Clone this repository or download the `markdown_to_speech.py` script.

2. Install the required dependencies:

   ```
   pip install markdown
   ```

3. Run the script with your markdown file:

   ```
   python markdown_to_speech.py input.md --output optimized_text.txt
   ```

   Options:
   - `--output`: Specify the output file name (default: output.txt)
   - `--format`: Choose the output format, either 'plain' or 'ssml' (default: plain)

## Customization

You can customize the pipeline by modifying the following functions in `markdown_to_speech.py`:

- `optimize_for_speech()`: Add or modify rules for text optimization
- `num2words()`: Improve number-to-word conversion for larger numbers
- `format_for_tts()`: Add support for additional output formats

## Future Enhancements

- Improved handling of specific markdown elements (e.g., tables, code blocks)
- Support for voice customization parameters
- Integration with popular TTS engines
- Handling of more complex document structures
- Support for additional input formats (e.g., HTML, PDF)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).