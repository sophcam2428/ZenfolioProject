from __future__ import division
import collections


class CodingProject:
    user_input = 0
    numeric_list = []
    mean = ""
    median = ""
    mode = ""
    range = ""
    string_result = ""

    def set_user_input(self, user_input):
        self.user_input = user_input

    def get_user_input(self):
        return self.user_input

    def handle_numeric(self):
        # create a sorted list with the numeric sequence values.
        self.numeric_list = list(map(float, sorted(self.user_input.split(' '))))

        self.find_mean()
        self.find_median()
        self.find_mode()
        self.find_range()

    def clean_up(self):
        self.user_input = ""
        self.mode = ""
        self.mean = ""
        self.median = ""
        self.range = ""
        self.string_result = ""
        self.numeric_list = []


    def handle_string(self):

        dic_chars = {}

        # counting the number of appearance for each character and storing it in a dictionary
        for char in self.user_input:
            if char not in dic_chars:
                dic_chars[char] = 0

            dic_chars[char] += 1

        # extracting the key, value from the dictionary - .items() and sorting it using collections library.
        sorted_dic = collections.OrderedDict(sorted(dic_chars.items()))

        # prints the result in the same format as project example
        for key, value in sorted_dic.items():
            if key != " ":
                print(key + ": " + str(value))
                self.string_result += key + ": " + str(value) + " "

        # remove the unnecessary space
        self.string_result = self.string_result[0:len(self.string_result) - 1]

    def find_mean(self):
        self.mean = str(float(sum(self.numeric_list) / len(self.numeric_list)))
        print("mean = " + self.mean)

    def find_median(self):
        index = int(len(self.numeric_list) / 2)

        # check if the sequence length is even or odd
        if len(self.numeric_list) % 2 == 1:
            self.median = str(self.numeric_list[index])
        else:
            self.median = str((self.numeric_list[index] + self.numeric_list[index - 1]) / 2)

        print("median = " + self.median)

    def find_mode(self):

        max_appearances = 0
        dic_input = {}
        dic_mode = {}

        # creates a dictionary to count the amount of appearance for each number
        for num in self.numeric_list:
            if num not in dic_input:
                dic_input[num] = 1
            else:
                dic_input[num] += 1
                if dic_input[num] > max_appearances:
                    max_appearances = dic_input[num]

        # create a dictionary to group all the numbers with the same amount of appearances.
        # the key is the number of appearances and the value is a list of the numbers with the key amount of appearances
        for key, value in dic_input.items():
            if value not in dic_mode:
                dic_mode[value] = []

            dic_mode[value].append(key)

        # if all the numbers appears the same amount of time, the is no mode, therefor we print none.
        # else all the numbers that appears the max amount of time are the mode.אק
        if len(dic_mode) == 1:
            self.mode = "none "
        else:
            for num in dic_mode[max_appearances]:
                self.mode += str(num) + " "

        self.mode = self.mode[0:len(self.mode) - 1]
        # strip is called to remove the final and unnecessary last white space.
        print("mode = " + self.mode.strip())

    def find_range(self):

        self.range = str(self.numeric_list[len(self.numeric_list) - 1] - self.numeric_list[0])
        print("range = " + self.range)

    def check_for_numeric_sequence(self):
        numeric_list = self.user_input.split(" ")

        for num in numeric_list:
            try:
                float(num)
            except ValueError:
                return False

        return True


def main():

    user_input = " "
    cp = CodingProject()

    while cp.get_user_input() != "quit":
        cp.clean_up()
        # get input form the user and discard white spaces at the beginning and end of the input
        cp.set_user_input(input("Please state a string or a number, to quit write quit\n").strip())

        # handle upper case input
        user_input = user_input.lower()

        if len(user_input) > 0:
            # if user_input.replace(" ", "").isnumeric():
            if cp.check_for_numeric_sequence():
                cp.handle_numeric()
            else:
                if cp.get_user_input() != "quit":
                    cp.handle_string()


    print("Have a good day!")


if __name__ == "__main__":
    main()


