import pygame
import random

SWAP_SOUND_FILE_PATH = 'visualization/audio/96525-Beep_tone-BLASTWAVEFX-30839.wav'
CHECK_SOUND_FILE_PATH = 'visualization/audio/83829-Beep_low_buzz-BLASTWAVEFX-20314.wav'
SORTED_SOUND_FILE_PATH = 'visualization/audio/mixkit-arcade-fast-game-over-233.wav'
pygame.mixer.init()
swap_sound = pygame.mixer.Sound(SWAP_SOUND_FILE_PATH)
check_sound = pygame.mixer.Sound(CHECK_SOUND_FILE_PATH)
sorted_sound = pygame.mixer.Sound(SORTED_SOUND_FILE_PATH)

WIDTH, HEIGHT = 900, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def quick_sort(arr, start, end):
    if start < end:
        pivot_index = partition(arr, start, end)
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)

def partition(arr, start, end):
    pivot_index = random.randint(start, end)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    i = start
    for j in range(start, end):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            draw(arr, i, j, end)
            check_sound.play()
    arr[i], arr[end] = arr[end], arr[i]
    draw(arr, i, end, end)
    swap_sound.play()
    return i

def draw(arr, partition_index=None, current_index=None, pivot_index=None, sorted=False):
    WINDOW.fill(WHITE)
    for i, val in enumerate(arr):
        color = BLACK
        if i == partition_index:
            color = GREEN
        elif i == current_index:
            color = RED
        elif i == pivot_index:
            color = BLUE
        elif sorted:
            color = GREEN
        pygame.draw.line(WINDOW, color, (i, HEIGHT), (i, HEIGHT - val), 1)
    pygame.display.update()

def draw_sorted(arr):
    for i in range(len(arr)):
        draw(arr[:i + 1], sorted=True)
        sorted_sound.play()
        
pygame.init()
pygame.display.set_caption("Quick Sort Visualization")

data = [random.randint(0, HEIGHT) for _ in range(WIDTH)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    quick_sort(data, 0, len(data) - 1)
    draw_sorted(data)
    pygame.time.delay(5000)
    running = False

pygame.quit()