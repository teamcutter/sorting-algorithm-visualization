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

def merge(arr, start, mid, end):
    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]

    i = j = 0
    k = start
    # Слияние
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

        draw(arr, start, end, mid, k)
        swap_sound.play()
    
    # Проверяем остатки
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        draw(arr, start, end, mid, k)
        check_sound.play()

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        draw(arr, start, end, mid, k)
        check_sound.play()

def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)

        merge(arr, start, mid, end)

def draw(arr, start, end, mid, k, sorted=False):
    WINDOW.fill(WHITE)
    for i, val in enumerate(arr):
        color = BLACK
        if start <= i <= end:
            color = RED  
        if i == mid:
            color = GREEN 
        if i == k:
            color = BLUE
        if sorted:
            color = GREEN
        pygame.draw.line(WINDOW, color, (i, HEIGHT), (i, HEIGHT - val), 1)
    pygame.display.update()

def draw_sorted(arr):
    for i in range(len(arr)):
        draw(arr[:i + 1], 0, 0, 0, 0, sorted=True)
        sorted_sound.play()

pygame.init()
pygame.display.set_caption("Merge Sort Visualization")

data = [random.randint(0, HEIGHT) for _ in range(WIDTH)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    merge_sort(data, 0, len(data) - 1)
    draw_sorted(data)
    pygame.time.delay(5000)
    running = False

pygame.quit()