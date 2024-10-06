# yang biasanya ada di pygame:
#     - init          -> untuk membuat world gamenya
#     - input user    -> kayak gerak mouse, keyboard, kata sandi, dll
#     - update asset  -> kayak pilih menu
#     - render ke display -> menggambar dunia gamenya


### MULAI

import pygame

##### INIT
pygame.init()

is_run = True

##WINDOW
x_window = 700
y_window = 500
window = pygame.display.set_mode((x_window, y_window))

##BUAT OBJEK

#posisi
x = 500
y = 300

#ukuran objek
panjang = 20
tinggi = 20

#kecepatan gerak (berapa jauh bergerak per satu kali pencet)
speed = 1


while is_run:
    
    pygame.time.delay(5)
    
    #####INPUT USER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_run = False
            break
        
    # mengambil input user dari keyboard
    keys = pygame.key.get_pressed()
    
    # kiri
    if keys[pygame.K_LEFT] and x > 10:
        x -= speed
    # kanan
    if keys[pygame.K_RIGHT] and x < x_window - panjang - 10:
        x += speed
    # atas
    if keys[pygame.K_UP] and y > 10:
        y -= speed
    # bawah
    if keys[pygame.K_DOWN] and y < y_window - tinggi - 10:
        y += speed
        
    #####UPDATE ASSET
    window.fill((0,0,0,))
    pygame.draw.rect(window,(255,255,255),(x,y,panjang,tinggi)) #ukuran-posisi
    
    
    #####RENDER KE DISPLAY
    pygame.display.update()
    


# QUIT
pygame.QUIT()