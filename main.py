import random
import pygame

WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
LIGHT_GRAY = (230, 230, 230)

BAR_SPACING = 50


def bogo_sort(numbers):

    for i in range(0, len(numbers)):
        get_pos = random.randint(i, len(numbers) - 1)
        aux = numbers[i]
        numbers[i] = numbers[get_pos]
        numbers[get_pos] = aux

    return numbers

def bogo_check(numbers):
    ordered = True

    for i in range(0, len(numbers)):
        if i != len(numbers) - 1:
            if numbers[i] > numbers[i+1]:
                return False

    return ordered

def get_position_in_sorted(sorted_arr, number):

    for i in range(0, len(sorted_arr)):
        if sorted_arr[i] == number:
            return i

def draw_array_as_bars(arr):
    top_height = HEIGHT - 150

    ref_arr = arr.copy()
    ref_arr.sort()

    percentage = (100 // (len(arr) + 1)) / 100

    width_of_bar = ((WIDTH // len(arr)) - BAR_SPACING * 2) * .7
    pos = BAR_SPACING


    for i in range(0, len(arr)):
        height_of_bar = top_height * (percentage * (get_position_in_sorted(ref_arr, arr[i]) + 1))
        

        rect = pygame.Rect(pos, top_height - height_of_bar, width_of_bar, height_of_bar)
        pygame.draw.rect(WIN, WHITE, rect, 0)

        pos += width_of_bar + BAR_SPACING


def main():
    run = True
    clock = pygame.time.Clock()

    my_list = [9, 3, 1, 6, 10, 42, 23]

    while run:
        clock.tick(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
        
        bogo_sorted_list =  bogo_sort(my_list)
        print("List bogo sorted -> ", bogo_sorted_list)
        print("Is it sorted properly? ", bogo_check(bogo_sorted_list))

        WIN.fill(GRAY)
        draw_array_as_bars(bogo_sorted_list)
        pygame.display.update()

        if bogo_check(bogo_sorted_list):
            run = False

    pygame.quit()

        

if __name__ == "__main__":
    main()