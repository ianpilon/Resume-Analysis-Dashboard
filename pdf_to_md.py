from pdfminer.high_level import extract_text
import os
import re

def clean_text(text):
    # Remove multiple newlines
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    # Add markdown formatting
    lines = text.split('\n')
    formatted_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            formatted_lines.append('')
            continue
            
        # Detect and format headers
        if len(line) < 50 and not any(char.islower() for char in line):
            formatted_lines.append(f'## {line}')
        else:
            formatted_lines.append(line)
    
    return '\n'.join(formatted_lines)

def convert_pdf_to_md(pdf_path):
    try:
        # Extract text from PDF
        text = extract_text(pdf_path)
        
        # Clean and format the text
        markdown_text = clean_text(text)
        
        # Create markdown filename
        md_path = pdf_path.rsplit('.', 1)[0] + '.md'
        
        # Write to markdown file
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(markdown_text)
            
        print(f'Successfully converted {pdf_path} to {md_path}')
        return True
    except Exception as e:
        print(f'Error converting {pdf_path}: {str(e)}')
        return False

def main():
    # Get all PDF files in the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_files = [f for f in os.listdir(current_dir) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print('No PDF files found in the current directory')
        return
    
    success_count = 0
    for pdf_file in pdf_files:
        pdf_path = os.path.join(current_dir, pdf_file)
        if convert_pdf_to_md(pdf_path):
            success_count += 1
    
    print(f'\nConversion complete: {success_count}/{len(pdf_files)} files converted successfully')

if __name__ == '__main__':
    main()
