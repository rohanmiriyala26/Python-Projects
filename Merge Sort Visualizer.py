import pygame
import random
import time
pygame.font.init()
screen = pygame.display.set_mode((900, 650))
font = pygame.font.SysFont(None, 30)
def draw_array(arr):
    screen.fill((255, 255, 255))
    array_width = 30
    x = 10
    for num in arr:
        pygame.draw.rect(screen, (0, 0, 0), (x, 300 - num * 3, array_width, num * 3))
        text_surface = font.render(str(num), True, (0, 0, 0))
        screen.blit(text_surface, (x, 320))
        x += array_width + 5
    pygame.display.flip()
    time.sleep(0.5)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            draw_array(arr)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            draw_array(arr)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            draw_array(arr)
array_to_sort = list(set(random.randint(1, 100) for _ in range(15)))
print('Unsorted array:', array_to_sort)
merge_sort(array_to_sort)
print("Sorted array:", array_to_sort)

