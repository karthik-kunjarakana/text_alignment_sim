def left_align(words, width):
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) > width:
            lines.append(' '.join(current_line))
            current_line = []
            current_length = 0
        current_line.append(word)
        current_length += len(word)

    if current_line:
        lines.append(' '.join(current_line))

    return lines

def right_align(words, width):
    lines = left_align(words, width)
    return [line.rjust(width) for line in lines]

def center_align(words, width):
    lines = left_align(words, width)
    return [line.center(width) for line in lines]

def justify_align(words, width):
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) > width:
            if len(current_line) == 1:
                lines.append(current_line[0].ljust(width))
            else:
                total_spaces = width - current_length
                space_between_words = total_spaces // (len(current_line) - 1)
                extra_spaces = total_spaces % (len(current_line) - 1)
                line = ''
                for i in range(len(current_line) - 1):
                    line += current_line[i] + ' ' * (space_between_words + (1 if i < extra_spaces else 0))
                line += current_line[-1]
                lines.append(line)
            current_line = []
            current_length = 0
        current_line.append(word)
        current_length += len(word)

    if current_line:
        lines.append(' '.join(current_line).ljust(width))

    return lines

def align_text(text, width, alignment):
    lines = text.split('\n')
    aligned_lines = []
    for line in lines:
        words = line.split()
        if alignment == 'left':
            aligned_lines.extend(left_align(words, width))
        elif alignment == 'right':
            aligned_lines.extend(right_align(words, width))
        elif alignment == 'center':
            aligned_lines.extend(center_align(words, width))
        elif alignment == 'justify':
            aligned_lines.extend(justify_align(words, width))
        else:
            raise ValueError("Invalid alignment type")
    return '\n'.join(aligned_lines)

# Read multiline input from the user
print("Enter the text (end with an empty line):")
user_input = []
while True:
    line = input()
    if line == "":
        break
    user_input.append(line)

text = "\n".join(user_input)
width = int(input("Enter the width: "))
alignment = input("Enter the alignment (left, right, center, justify): ")

print(f"\n{alignment.capitalize()} Aligned:")
print(align_text(text, width, alignment))