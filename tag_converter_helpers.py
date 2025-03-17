import random
import string
from bs4 import NavigableString

def replace_after_before_value(value):
    if value != 'auto' and value != '0':
        try:
            value = str(float(value[:-1]))
        except ValueError:
            value = str(int(value[:-1]))
        value += 'em'
        return value
    else:
        return value


def check_stroke(parent_t_pb, horizontal_attr, vertical_attr):
    if parent_t_pb is not None:
        stroke = parent_t_pb.attrs.get('stroke')
        if stroke == 'horizontal':
            return horizontal_attr
        elif stroke == 'vertical':
            return vertical_attr

    return horizontal_attr


def handle_after(parent_t_pb, value):
    horizontal_attr = 'margin-bottom'
    vertical_attr = 'margin-left'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    value = replace_after_before_value(value)
    return chosen_attr, value


def handle_before(parent_t_pb, value):
    horizontal_attr = 'margin-top'
    vertical_attr = 'margin-right'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    value = replace_after_before_value(value)
    return chosen_attr, value


def handle_end(parent_t_pb, value):
    horizontal_attr = 'margin-right'
    vertical_attr = 'margin-bottom'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    value = replace_after_before_value(value)
    return chosen_attr, value


def handle_start(parent_t_pb, value):
    horizontal_attr = 'margin-left'
    vertical_attr = 'margin-top'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    value = replace_after_before_value(value)
    return chosen_attr, value


def handle_linespace(parent_t_pb, value):
    value = str(1 + int(value[:-1])/100)
    return 'line-height', value


def handle_pad_before(parent_t_pb, value):
    horizontal_attr = 'padding-top'
    vertical_attr = 'padding-right'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    value = replace_after_before_value(value)
    return chosen_attr, value


def handle_pad_after(parent_t_pb, value):
    horizontal_attr = 'padding-bottom'
    vertical_attr = 'padding-left'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    value = replace_after_before_value(value)
    return chosen_attr, value


def handle_pad_end(parent_t_pb, value):
    horizontal_attr = 'padding-right'
    vertical_attr = 'padding-bottom'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    value = replace_after_before_value(value)
    return chosen_attr, value


def handle_pad_start(parent_t_pb, value):
    horizontal_attr = 'padding-left'
    vertical_attr = 'padding-top'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    value = replace_after_before_value(value)
    return chosen_attr, value


def handle_xsize(parent_t_pb, value):
    return 'font-size', str(int(value[:-1]) / 100) + "em"


def handle_align(parent_t_pb, value):
    return 'text-align', value


def handle_indent(parent_t_pb, value):
    return 'text-indent', value + "em"


def handle_border_after_color(parent_t_pb, value):
    horizontal_attr = 'border-bottom-color'
    vertical_attr = 'border-left-color'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    return chosen_attr, value


def handle_border_before_color(parent_t_pb, value):
    horizontal_attr = 'border-top-color'
    vertical_attr = 'border-right-color'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    return chosen_attr, value


def handle_border_start_color(parent_t_pb, value):
    horizontal_attr = 'border-left-color'
    vertical_attr = 'border-top-color'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    return chosen_attr, value


def handle_border_end_color(parent_t_pb, value):
    horizontal_attr = 'border-right-color'
    vertical_attr = 'border-bottom-color'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    return chosen_attr, value


def handle_border_after_style(parent_t_pb, value):
    horizontal_attr = 'border-bottom-style'
    vertical_attr = 'border-left-style'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    return chosen_attr, value


def handle_border_before_style(parent_t_pb, value):
    horizontal_attr = 'border-top-style'
    vertical_attr = 'border-right-style'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    return chosen_attr, value


def handle_border_start_style(parent_t_pb, value):
    horizontal_attr = 'border-left-style'
    vertical_attr = 'border-top-style'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    return chosen_attr, value


def handle_border_end_style(parent_t_pb, value):
    horizontal_attr = 'border-right-style'
    vertical_attr = 'border-bottom-style'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    return chosen_attr, value


def handle_border_after_width(parent_t_pb, value):
    horizontal_attr = 'border-bottom-width'
    vertical_attr = 'border-left-width'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    return chosen_attr, value + "px"


def handle_border_before_width(parent_t_pb, value):
    horizontal_attr = 'border-top-width'
    vertical_attr = 'border-right-width'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    return chosen_attr, value + "px"


def handle_border_start_width(parent_t_pb, value):
    horizontal_attr = 'border-left-width'
    vertical_attr = 'border-top-width'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    return chosen_attr, value + "px"


def handle_border_end_width(parent_t_pb, value):
    horizontal_attr = 'border-right-width'
    vertical_attr = 'border-bottom-width'
    chosen_attr = check_stroke(parent_t_pb, horizontal_attr, vertical_attr)
    return chosen_attr, value + "px"


def handle_img(soup):
    for tag in soup.find_all('t-img'):
        new_tag = soup.new_tag('img')
        src = '../' + tag.attrs['src'].replace('img', 'image')
        attrs = {
            'src': src,
            'class': ['fit']
        }
        if tag.has_attr('chars'):
            attrs['height'] = tag['chars'] + 'em'
        if tag.has_attr('line'):
            attrs['class'] += ['gaiji-line']

        new_tag.attrs = attrs

        text = tag.text
        if text:
            tag.insert_after(NavigableString(text))
        tag.replace_with(new_tag)


def handle_tmove(soup):
    for tag in soup.find_all('t-move'):
        parent = tag.find_parent()
        if parent:
            tag_contents = tag.contents
            tag.unwrap()
            parent.extend(tag_contents)


def handle_trb(soup):
    for custom_tag in soup.find_all('t-rb'):
        ruby_tag = soup.new_tag('ruby')
        rt_tag = soup.new_tag('rt')

        text = custom_tag.text.strip()
        split_pos = text.find('（')
        if split_pos == 0:
            ruby_tag.append(custom_tag.contents[0])
        else:
            ruby_tag.append(text[0:split_pos].strip())
        if len(text) == 0:
            continue
        rt_text = text[split_pos:].split('（')[1].split('）')[0]
        rt_tag.append(rt_text.strip())

        custom_tag.replace_with(ruby_tag)
        ruby_tag.append(rt_tag)


def handle_tyoko(soup):
    for custom_tag in soup.find_all('t-yoko'):
        span_tag = soup.new_tag('span')
        span_tag.attrs = {
            'class': ['tcy']
        }
        span_tag.append(custom_tag.get_text(strip=True))
        custom_tag.replace_with(span_tag)


def handle_tclass(soup):
    class_mapping = {}

    for tag in soup.find_all(attrs={"t-class": True}):
        original_t_class = tag.get("t-class")
        new_t_classes = generate_random_classes(original_t_class, class_mapping)

        if "class" in tag.attrs:
            current_classes = tag["class"]
            current_classes.extend(new_t_classes)
            tag["class"] = list(set(current_classes))
        else:
            tag["class"] = new_t_classes

        for orig, new in zip(original_t_class.split(), new_t_classes):
            class_mapping[orig] = new

        del tag["t-class"]

    return class_mapping


def generate_random_classes(original_t_class, existing_mapping):
    numbers = [s for s in original_t_class.split() if s[0] == "+" and s[1:].isdigit()]

    random_class_names = []

    for num in numbers:
        mapped_name = existing_mapping.get(num)
        if mapped_name:
            random_class_names.append(mapped_name)
        else:
            new_random_class = random.choice(string.ascii_letters) + ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            random_class_names.append(new_random_class)
            existing_mapping[num] = new_random_class

    return random_class_names


def handle_tfont(soup):
    for t_font_tag in soup.find_all('t-font'):
        t_font_tag.name = 'span'


def handle_tem(soup):
    for tem_tag in soup.find_all('t-em'):
        tem_tag.name = 'span'
        tem_tag.attrs = {
            'class': ['em-' + tem_tag.attrs['style']]
        }


def handle_tcode(soup):
    for tcode_tag in soup.find_all('t-code'):
        span_tag = soup.new_tag('span')
        img_tag = soup.new_tag('img')
        src = '../' + tcode_tag.attrs['src'].replace('img', 'image')

        img_tag['src'] = src
        img_tag['class'] = ['gaiji']

        span_tag.append(img_tag)
        tcode_tag.find_parent().extend(tcode_tag.contents)
        tcode_tag.replace_with(span_tag)



def handle_text_orientation(parent_t_pb, value):
    return 'text-orientation', value


def handle_face(parent_t_pb, value):
    return 'font-family', value[1:-1]


def handle_weight(parent_t_pb, value):
    return 'font-weight', value


def handle_charspace(parent_t_pb, value):
    return 'letter-spacing', value


def handle_length(parent_t_pb, value):
    return 'width', value
