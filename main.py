import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Pilih Suara Hewan")

# COLOR
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

pygame.mixer.music.set_volume(1.0)

# ASSETS
width, height = 300, 300
assets = {
    "kucing": {"gambar": pygame.transform.scale(pygame.image.load("assets/cat.jpg"), (width, height)), "suara": "sounds/cat.wav"},
    "anjing": {"gambar": pygame.transform.scale(pygame.image.load("assets/dog.jpg"), (width, height)), "suara": "sounds/dog.wav"},
    "monyet": {"gambar": pygame.transform.scale(pygame.image.load("assets/monkey.jpg"), (width, height)), "suara": "sounds/monkey.wav"},
    "burung": {"gambar": pygame.transform.scale(pygame.image.load("assets/bird.jpg"), (width, height)), "suara": "sounds/bird.wav"},
    "singa": {"gambar": pygame.transform.scale(pygame.image.load("assets/leon.jpg"), (width, height)), "suara": "sounds/leon.wav"},
    "kambing": {"gambar": pygame.transform.scale(pygame.image.load("assets/sheep.jpg"), (width, height)), "suara": "sounds/sheep.wav"},
    "babi": {"gambar": pygame.transform.scale(pygame.image.load("assets/pig.jpg"), (width, height)), "suara": "sounds/pig.wav"},
    "kuda": {"gambar": pygame.transform.scale(pygame.image.load("assets/horse.jpg"), (width, height)), "suara": "sounds/horse.wav"},
}

# BACKGROUND
background_image = pygame.image.load("assets/jungle.jpg")

# SOUDN FUNCTION
def mainkan_suara(suara):
    pygame.mixer.music.load(suara)
    pygame.mixer.music.play()

# GAME FUNCTION
def main():
    clock = pygame.time.Clock()
    current_animal = None
    game_started = False 

    # FONTS
    font_large = pygame.font.Font(None, 48)
    font_small = pygame.font.Font(None, 36)

    while True:
        screen.fill(BLACK)

        screen_width, screen_height = screen.get_size()
        center_x = screen_width // 2
        center_y = screen_height // 2

        if game_started:
            background_image_resized = pygame.transform.scale(background_image, (screen_width, screen_height))
            screen.blit(background_image_resized, (0, 0))

        if not game_started:
            title_text = font_large.render("Mari Tebak Suara Hewan!", True, WHITE)
            screen.blit(title_text, (center_x - title_text.get_width() // 2, center_y - 100))
            start_text = font_large.render("Press S to Start", True, WHITE)
            screen.blit(start_text, (center_x - start_text.get_width() // 2, center_y + 50))

        # INPUT PILIHAN SUARA
        elif game_started and not current_animal:
            instructions = [
                "Klik 1 untuk Kucing",
                "Klik 2 untuk Anjing",
                "Klik 3 untuk Monyet",
                "Klik 4 untuk Burung",
                "Klik 5 untuk Singa",
                "Klik 6 untuk Kambing",
                "Klik 7 untuk Babi",
                "Klik 8 untuk Kuda"
            ]
            
            total_height = len(instructions) * 40
            start_y = (screen_height - total_height) // 2
            
            for i, text in enumerate(instructions):
                option_text = font_small.render(text, True, BLACK)
                screen.blit(option_text, (center_x - option_text.get_width() // 2, start_y + i * 40))

        if current_animal:
            screen.blit(assets[current_animal]["gambar"], (center_x - width // 2, center_y - height // 2))
            animal_name = font_large.render(current_animal.capitalize(), True, BLACK)
            screen.blit(animal_name, (center_x - animal_name.get_width() // 2, center_y - height // 2 - 40))

        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_s and not game_started:
                    game_started = True

                if game_started:
                    if event.key == pygame.K_1:
                        current_animal = "kucing"
                    elif event.key == pygame.K_2:
                        current_animal = "anjing"
                    elif event.key == pygame.K_3:
                        current_animal = "monyet"
                    elif event.key == pygame.K_4:
                        current_animal = "burung"
                    elif event.key == pygame.K_5:
                        current_animal = "singa"
                    elif event.key == pygame.K_6:
                        current_animal = "kambing"
                    elif event.key == pygame.K_7:
                        current_animal = "babi"
                    elif event.key == pygame.K_8:
                        current_animal = "kuda"

                    if current_animal in assets:
                        mainkan_suara(assets[current_animal]["suara"])

        # DISPLAY GAME
        pygame.display.flip()
        clock.tick(30)

main()