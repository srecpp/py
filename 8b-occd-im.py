class Snake:
    def __init__(self, name):
        self.name = name
    def change_name(self, new_name):
        self.name = new_name
        return self.name
    def __del__(self):
        print(f'Destructor called, {self.name} Killed.')
snake1 = Snake("python")
snake2 = Snake("anaconda")
print(snake1.name)
print(snake2.name)
print(snake2.change_name("cobra"))
del snake2
