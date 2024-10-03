import argparse
import re
import logging
from pathlib import Path
import markdown

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_markdown_file(file_path):
    """Read the content of a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except IOError as e:
        logging.error(f"Error reading file: {e}")
        raise

def strip_markdown(content):
    """Convert markdown to plain text and strip remaining syntax."""
    # Convert markdown to HTML
    html = markdown.markdown(content)
    
    # Remove HTML tags
    text = re.sub('<[^<]+?>', '', html)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def optimize_for_speech(text):
    """Optimize text for speech synthesis."""
    # Expand common abbreviations
    abbreviations = {
        'e.g.': 'for example',
        'i.e.': 'that is',
        'etc.': 'et cetera',
        'Mr.': 'Mister',
        'Mrs.': 'Missus',
        'Dr.': 'Doctor',
    }
    for abbr, expansion in abbreviations.items():
        text = text.replace(abbr, expansion)
    
    # Convert numbers to words (simple version)
    text = re.sub(r'\b(\d+)\b', lambda m: num2words(int(m.group(1))), text)
    
    # Handle symbols
    text = text.replace('&', 'and')
    text = text.replace('%', 'percent')
    text = text.replace('$', 'dollar')
    
    return text

def num2words(num):
    """Convert a number to words (simple version for demonstration)."""
    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    if num < 10:
        return units[num]
    elif num < 20:
        return teens[num - 10]
    elif num < 100:
        return tens[num // 10] + ('-' + units[num % 10] if num % 10 != 0 else '')
    else:
        return str(num)  # For simplicity, we're not handling larger numbers in this example

def format_for_tts(text, output_format='plain'):
    """Format the text for TTS engine compatibility."""
    if output_format == 'plain':
        return text
    elif output_format == 'ssml':
        return f'<speak>{text}</speak>'
    else:
        logging.warning(f"Unsupported output format: {output_format}. Defaulting to plain text.")
        return text

def markdown_to_speech(input_file, output_file, output_format='plain'):
    """Convert markdown to optimized text for speech synthesis."""
    try:
        # Read markdown file
        content = read_markdown_file(input_file)
        
        # Strip markdown syntax
        plain_text = strip_markdown(content)
        
        # Optimize for speech
        optimized_text = optimize_for_speech(plain_text)
        
        # Format for TTS
        formatted_text = format_for_tts(optimized_text, output_format)
        
        # Write to output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(formatted_text)
        
        logging.info(f"Successfully converted {input_file} to {output_file}")
    
    except Exception as e:
        logging.error(f"Error in markdown_to_speech: {e}")
        raise

def main():
    parser = argparse.ArgumentParser(description="Convert markdown to optimized text for speech synthesis.")
    parser.add_argument("input_file", help="Path to the input markdown file")
    parser.add_argument("--output", default="output.txt", help="Path to the output text file")
    parser.add_argument("--format", choices=['plain', 'ssml'], default='plain', help="Output format (default: plain)")
    
    args = parser.parse_args()
    
    markdown_to_speech(args.input_file, args.output, args.format)

if __name__ == "__main__":
    main()