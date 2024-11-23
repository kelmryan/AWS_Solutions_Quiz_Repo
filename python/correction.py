import re
import sys

def correct_answer_parser(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()

    updated_content = []
    correct_answer = None
    for line in content:
        # Find the correct answer using regex
        correct_answer_match = re.search(r'\*\*Correct Answer:\s\*\*(\w)', line)
        if correct_answer_match:
            correct_answer = correct_answer_match.group(1)
            # Remove the correct answer line            continue
        
        if correct_answer:
            line = re.sub(r'\b' + re.escape(correct_answer) + r'\.\s', '- [x] ', line)
            line = re.sub(r'\b[A-D]\.\s', '- [ ] ', line)
        else:
            line = re.sub(r'\b[A-D]\.\s', '- [ ] ', line)
        updated_content.append(line)

    with open('corrected.md', 'w') as file:
        file.writelines(updated_content)
    print("Correct answer updated and copied to corrected.md successfully.")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python correction.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    correct_answer_parser(file_path)