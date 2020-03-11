from typing import List, TextIO
import random


class RandomPersonGeneratorClass:
    """A class where you can input a string of names and it will spit out
    each person from the string in a random order

    === Attributes ===
    name_list: a list of the names inputted
    name_list_str: the original string of names
    """
    name_list: List[str]
    name_list_str: str

    def __init__(self, names: str) -> None:
        """Initialize the generator with the given string of names"""
        self.name_list = names.split(", ")
        self.name_list_str = names

    def is_empty(self) -> bool:
        """Check if the name_list is empty"""
        return self.name_list == []

    def _reset(self) -> None:
        """Reset the name_list back to what name_list_str is """
        self.name_list = self.name_list_str.split(", ")

    def _update_name_list_str(self) -> None:
        """Update the string of the list of names name_list_str

        Precondition: this is only called after name_list has been changed
        """
        new_name_list_str = ", ".join(self.name_list)
        self.name_list_str = new_name_list_str

    def change_name_list(self, new_names: str) -> None:
        """Change the list of names to the new input list of strings"""
        self.name_list_str = new_names
        self._reset()

    def add(self, new_name: str) -> None:
        """Give a new name to the list and update the list and str
        accordingly
        """
        if not (new_name in self.name_list):
            self.name_list.append(new_name)
            self._update_name_list_str()
        else:
            new_name = input("The name already exists, enter another")
            self.add(new_name)

    def remove(self, name: str) -> None:
        """Remove a new name to the list and update the list and str
        accordingly
        """
        if name in self.name_list:
            self.name_list.remove(name)
            self._update_name_list_str()
        else:
            name = input("Invalid input, try again")
            self.remove(name)

    def next(self) -> str:
        """Return the str of the person's name, if the list is empty, it will
        reset back to what the str is
        """
        if self.is_empty():
            self._reset()
            return "the list is empty, it is going to reset"

        else:
            person = random.choice(self.name_list)
            self.name_list.remove(person)
            return person


def construct_file(output_file: TextIO):
    name_list = output_file.readlines()[6:]
    for i in range(len(name_list)):
        name_list[i] = name_list[i][0: len(name_list[i]) - 1] # this gets rid of the new line character at the end
    names = ", ".join(name_list)
    rpg = RandomPersonGeneratorClass(names)

    output_file.write("\nHere is the list of names in order:\n")
    while not (rpg.is_empty()):
        output_file.write(rpg.next() + "\n")

# TODO: make the program so that you can input the list through the console instead of modifying the txt file


if __name__ == "__main__":
    file = open("./testing.txt", "r+")
    construct_file(file)
    file.close()
