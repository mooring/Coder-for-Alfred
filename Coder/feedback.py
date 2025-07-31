# author: Peter Okma
import xml.etree.ElementTree as et


class Feedback:
    """Feedback class used by Alfred Script Filter"""

    def __init__(self):
        self.feedback = et.Element('items')

    def __str__(self):
        """Return XML string representation for Alfred"""
        return et.tostring(self.feedback, encoding='utf-8').decode('utf-8')

    def add_item(self, title, subtitle="", arg="", valid="yes", autocomplete="", icon="icon.png"):
        """
        Add item to Alfred Feedback

        Args:
            title (str): The title displayed by Alfred
        Keyword Args:
            subtitle (str): The subtitle displayed by Alfred
            arg (str): The value returned when item is selected
            valid (str): Whether the item is actionable (yes/no)
            autocomplete (str): Text to complete if 'valid' is 'no'
            icon (str): Filename of icon to display
        """
        item = et.SubElement(self.feedback, 'item', {
            'uid': str(len(self.feedback)),
            'arg': arg,
            'valid': valid,
            'autocomplete': autocomplete
        })
        et.SubElement(item, 'title').text = title
        et.SubElement(item, 'subtitle').text = subtitle
        et.SubElement(item, 'icon').text = icon