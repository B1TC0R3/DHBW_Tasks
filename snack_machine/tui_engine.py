#!/usr/lib/python3

import os
from utility import check_args,\
                    dict_line_length,\
                    list_line_length


def required_length(title: str, data: dict, options: list):
    final_len = len(title)
    data_len = dict_line_length(data)
    options_len = list_line_length(options)

    if final_len < data_len:
        final_len = data_len
    if final_len < options_len:
        final_len = options_len

    return final_len


def _display(title: str, data: str, options: str, connector: str):
    os.system("clear")

    print(f"{connector}\n"
          f"{title}\n"
          f"{connector}\n"
          f"{data}"
          f"{connector}\n"
          f"{options}"
          f"{connector}")


class TuiEngine:
    color = {"green": "\033[92m",
             "none": "\033[0m"}

    selected_index = 0

    title = ""
    data = dict
    options = list

    line_length = 0

    def render(self, title: str, data: dict, options: list, selected_index: int):
        """
        Converts input into a box-like structure
        :param title: The title of the structure
        :param data: The data displayed in the middle box.
                     Both key and entry of the dict are displayed
        :param options: The options displayed in the bottom box
                        The keys should be strings, the entries have to be
                        function pointers
        """
        check_args(title, data, options, selected_index)
        if not isinstance(title, str)\
           or not isinstance(data, dict)\
           or not isinstance(options, list)\
           or not isinstance(selected_index, int):
            raise TypeError("A parameter passed to TuiEngine.render() had the wrong type.")

        self.title = title
        self.data = data
        self.options = options

        self.line_length = required_length(title, data, options)
        connector = f"#-{'-'*self.line_length}-#"
        title_render = f"| {title}{(self.line_length-len(title))*' '} |"
        data_render = self._render_data()
        options_render = self._render_options()

        _display(title_render,
                 data_render,
                 options_render,
                 connector)

    def _render_data(self) -> str:
        data_render = ""
        for key, entry in self.data.items():
            line = f"{key}: {entry}"
            data_render += f"| {line}{(self.line_length - len(line)) * ' '} |\n"

        return data_render

    def _render_options(self) -> str:
        options_render = ""
        for index, entry in enumerate(self.options):
            if index == self.selected_index:
                options_render += f"->{self.color['green']}{entry}{self.color['none']}" \
                                  f"{(self.line_length-len(entry))*' '} |\n"
            else:
                options_render += f"| {entry}{(self.line_length-len(entry))*' '} |\n"

        return options_render
