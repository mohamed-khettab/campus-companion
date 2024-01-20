class ButtonModel:
    def change_color(textbox, color):
        selected_text = textbox.tag_ranges('sel')
        if selected_text:
            tag_name = 'color_' + color
            textbox.tag_config(tag_name, foreground=color)
        for tag in textbox.tag_names(selected_text[0]):
            textbox.tag_remove(tag, selected_text[0], selected_text[1])
            textbox.tag_add(tag_name, selected_text[0], selected_text[1])

    def insert_bullet_point(textbox):
        current_index = textbox.index("insert")
        bullet_point_text = "\n    \u2022"
        textbox.insert(current_index, bullet_point_text)