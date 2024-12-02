import os
import re
import sys

def add_lang_to_mdx(file_path, lang_value):
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        
        # Check if file already has lang setting
        if f'lang: "{lang_value}"' in content or f"lang: '{lang_value}'" in content:
            return False
        
        # Find the frontmatter
        if content.lstrip().startswith('---\n'):
            # Split the frontmatter
            parts = content.split('---\n', 2)
            if len(parts) >= 2:
                # Add lang setting to frontmatter
                new_frontmatter = parts[1].rstrip() + f'\nlang: "{lang_value}"\n'
                new_content = f'---\n{new_frontmatter}---\n{parts[2]}'
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return False

def process_directory(directory, lang_value):
    modified_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.mdx'):
                file_path = os.path.join(root, file)
                if add_lang_to_mdx(file_path, lang_value):
                    modified_files.append(os.path.relpath(file_path, directory))
    return modified_files

if __name__ == '__main__':
    base_dir = '/Users/kennylee/Documents/Documentation_Sites/product-manual'
    directories = [
        os.path.join(base_dir, 'cn/apps/superloop')
    ]
    lang_value = 'zh-hans'
    
    for directory in directories:
        print(f'\nProcessing directory: {os.path.basename(directory)}')
        modified = process_directory(directory, lang_value)
        print(f'Modified {len(modified)} files:')
        for file in modified:
            print(f'- {file}')
