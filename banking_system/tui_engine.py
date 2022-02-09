import os


tui_width = 0
selected_index = 0

connector = ""
title_rendered = ""

selection_color = "\033[92m"
no_color = "\033[0m"

original_options = {}

data_rendered = []
options_rendered = []
options_list = []


def get_required_length(title: str, data: {}, options: {}) -> int:
    title_len = len(title)

    data_max_len = 0
    for entry, key in data.items():
        current_data_len = len(f"{key}: {entry}")
        if current_data_len > data_max_len:
            data_max_len = current_data_len

    options_max_len = 0
    for key, entry in options.items():
        current_options_len = len(key)
        if current_options_len > options_max_len:
            options_max_len = current_options_len

    if title_len >= data_max_len and\
       title_len >= options_max_len:
        return title_len
    if data_max_len >= title_len and\
       data_max_len >= options_max_len:
        return data_max_len
    if options_max_len >= title_len and\
       options_max_len >= data_max_len:
        return data_max_len


def create_gap(length: int) -> str:
    current_line = ""
    for i in range(length):
        current_line = current_line + " "

    return current_line


def create_connector():
    global connector
    global tui_width

    connector = "#-"
    for i in range(tui_width):
        connector = connector + "-"
    connector = connector + "-#"


def create_title(title: str):
    global title_rendered
    global tui_width

    title_len = len(title)
    gap_len = tui_width - title_len + 1

    title_rendered = "| " + title + create_gap(gap_len) + "|"


def create_data(data: {}):
    global tui_width
    global data_rendered

    for key, entry in data.items():
        converted_entry = f"{key}: {entry}"
        current_data_len = len(converted_entry)
        gap_len = tui_width - current_data_len + 1

        current_line = "| " + converted_entry + create_gap(gap_len) + "|"
        data_rendered.append(current_line)


def create_options(options: {}):
    global tui_width
    global options_rendered
    global options_list

    options_rendered = []
    options_list = []

    options_list = list(options.values())

    counter = 0
    for key, entry in options.items():

        current_option_len = len(key)
        gap_len = tui_width - current_option_len + 1

        selection_char = "| "
        if selected_index == counter:
            selection_char = f"|{selection_color}→"

        current_line = f"{selection_char}{key}{no_color}{create_gap(gap_len)}|"
        options_rendered.append(current_line)

        counter = counter + 1


def execute_selection():
    global selected_index
    global options_list

    options_list[selected_index]()


def select_next():
    global selected_index
    global options_list

    if selected_index < len(options_list) - 1:
        selected_index = selected_index + 1
    else:
        selected_index = 0

    _local_render()


def select_prev():
    global selected_index
    global options_list

    if selected_index > 0:
        selected_index = selected_index - 1
    else:
        selected_index = len(options_list) - 1

    _local_render()


def _local_render():
    global original_options

    create_options(original_options)
    display()


def render(title: str, data: {}, options: []):
    global tui_width
    global title_rendered
    global data_rendered
    global options_rendered
    global original_options

    original_options = options

    tui_width = get_required_length(title, data, options)
    create_connector()
    create_title(title)
    create_data(data)
    create_options(options)

    display()


def display():
    os.system("clear")

    print(connector)
    print(title_rendered)
    print(connector)
    for line in data_rendered:
        print(line)
    print(connector)
    for line in options_rendered:
        print(line)
    print(connector)
