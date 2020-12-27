def main():
    f = open('input.txt', 'r')
    rules = f.read().split('\n')[:-2]
    rulebook = make_rulebook(rules)
    traveler = RulebookTraveler(rulebook)
    print(traveler.count_bags('shiny gold'))

    
def make_rulebook(rules):
    rulebook = {}
    for rule in rules:
        rulebook = rulebook | parse_rule(rule)
    return rulebook

def parse_rule(rule):
    """
    Parses a single rule of the form:
    [color] bag contains ...
    Create a dict of form color : [color]
    """
    words = rule.split(' ')
    key_color = words[0] + ' ' + words[1]
    if rule.find('no other bags') != -1:
        return {key_color: []}
    return {key_color: get_colors(words[4:])}

def get_colors(words):
    # Gets the colors from the rest of the rule
    colors = []
    while len(words) > 0:
        color = words[1] + ' ' + words[2]
        colors.append(color)
        words = words[4:]
    return colors

class RulebookTraveler():
    # A rulebook just defines what each color bag contains
    # as a dictionary (color: [color]).
    # Also keep track of solutions (colors that can contain a goal color)
    # So if we ever see one of these colors we know the parent bag leads to
    # that goal color.
    
    def __init__(self, rulebook):
        self.rulebook = rulebook
        self.solutions = []

    def count_bags(self, goal_color):
        """
        Count how many colors of bags will eventually contain a
        bag of the given color
        Color -> Integer
        """
        self.solutions = []
        for color in self.rulebook:
            self.count_helper(color, goal_color)
        return len(self.solutions)

    def count_helper(self, origin_color, goal_color):
        """
        Helper for count_bags, returns whether a bag of color origin_color
        will eventually contain a bag of color goal_color.
        Color Color -> Boolean
        """
        if origin_color == goal_color:
            return True
        next_colors = self.rulebook[origin_color]
        solution = False
        for color in next_colors:
            if color in self.solutions:
                return True
            else:
                solution = self.count_helper(color, goal_color)
                if solution:
                    self.solutions.append(color)
        return solution
        
        
    
if __name__ == '__main__':
    main()
