import os
from utility import check_args,\
                    dict_line_length,\
                    list_line_length


title_rendered = ""

original_options = {}

data_rendered = []
options_rendered = []
options_list = []


def required_length(title: str, data: dict, options: dict):
    final_len = len(title)
    data_len = dict_line_length(data)
    options_len = list_line_length(list(options.keys()))

    if final_len < data_len:
        final_len = data_len
    if final_len < options_len:
        final_len = options_len

    return final_len


class TuiEngine:
    color = {"green": "\033[92m",
             "none": "\033[0m"}

    selected_index = 0
    options_list = []

    def execute_selected_item(self):
        pass

    def selection_up(self):
        pass

    def selection_down(self):
        pass

    def render(self, title: str, data: dict, options: dict):
        check_args(title, data, options)

        line_length = required_length(title, data, options)
        connector = f"#-{'-'*line_length}-#"
        title_render = f"| {title}{(line_length-len(title))*' '} |"
        data_render = self._render_data(data, line_length)
        options_render = self._render_options(options.keys())

        self._display(title,
                      data_render,
                      options_render,
                      connector)

    def _render_data(self, data: dict, line_length: int) -> str:
        data_render = ""
        for key, entry in data.items():
            line = f"{key}: {entry}"
            data_render += f"| {line}{(line_length - len(line)) * ' '} |\n"

        return data_render

    def _render_options(self, keys: list, line_length: int) -> str:
        options_render = ""
        for index, entry in enumerate(keys):
            if index == self.selected_index:
                options_render += f"->{self.color['green']}{entry}{self.color['none']}" \
                                  f"{(line_length-len(entry)*' ')} |\n"
            else:
                options_render += f"| {entry}{(line_length-len(entry)*' ')} |\n"

        return options_render

    def _display(self, title: str, data: str, options: str, connector: str):
        os.system("clear")

        print(f"{connector}\n"
              f"{title}"
              f"{connector}\n"
              f"{data}"
              f"{connector}\n"
              f"{options}"
              f"{connector}")
