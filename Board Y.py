import pygame
import yweather
import time
# Yahoo weather API Data extraction
pygame.init()

#   Initial Setup
display_prop = (800, 600)
main_display = pygame.display.set_mode(display_prop)
pygame.display.set_caption("Board Y")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)     # Make the mouse invisible
cursor_image = pygame.image.load('CR_Cursor.png')
pygame.mixer.music.load("1primavera.wav")

# Color Definitions
wood = (139, 35, 35)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 200, 0)
bright_green = (0, 255, 0)


def text_surface_function(text, font, text_color):
    text_surface = font.render(text, True, text_color)
    return text_surface, text_surface.get_rect()


def drawbutton(color, x, y, w, h, font_size, text, text_color):
    pygame.draw.rect(main_display, color, (x, y, w, h))
    button_font = pygame.font.Font("freesansbold.ttf", font_size)
    button_surface, button_rectangle = text_surface_function(text, button_font, text_color)
    button_rectangle.center = (x + w / 2, y + h / 2)
    main_display.blit(button_surface, button_rectangle)


def data_display(font_size, text, font_color, x, y):
    try:
                data_font = pygame.font.SysFont("comicsansms", font_size)
                data_d1 = data_font.render(text, True, font_color)
                data_surface, data_rectangle = data_d1, data_d1.get_rect()
                data_rectangle.center = (x, y)
                main_display.blit(data_surface, data_rectangle)
    except:
                pass


#def weather_data(set_location):

#   ['Sunset', 'Min Temperature', 'Current Temperature', 'Wind', 'Sunrise', 'Condition', 'Max Temperature']


def main():
    status = True
    pygame.mixer.music.play(-1)
    music_status = 1
    weather_location = 0
    connector = yweather.Client()

    weather_id_ny = connector.fetch_woeid('New York')
    weather_data_ny = connector.fetch_weather(weather_id_ny, metric=True)
    data_dict_ny = {}
    data_dict_ny.update({'Current Temperature': weather_data_ny["condition"]["temp"], \
                    'Sunrise': weather_data_ny['astronomy']['sunrise'], 'Sunset': weather_data_ny['astronomy']['sunset'], \
                    'Max Temperature': (str(weather_data_ny['forecast'][0]['high']) + " Degrees C"), \
                    'Min Temperature': (str(weather_data_ny['forecast'][0]['low'] + " Degrees C")),
                    'Wind': (str(weather_data_ny['wind']['speed'] + " km/h")), \
                    'Condition': weather_data_ny['condition']['text']})
    keys_list_ny = data_dict_ny.keys()

    weather_id_buffalo = connector.fetch_woeid('Buffalo')
    weather_data_buffalo = connector.fetch_weather(weather_id_buffalo, metric=True)
    data_dict_buffalo = {}
    data_dict_buffalo.update({'Current Temperature': weather_data_buffalo["condition"]["temp"], \
                    'Sunrise': weather_data_buffalo['astronomy']['sunrise'], 'Sunset': weather_data_buffalo['astronomy']['sunset'], \
                    'Max Temperature': (str(weather_data_buffalo['forecast'][0]['high']) + " Degrees C"), \
                    'Min Temperature': (str(weather_data_buffalo['forecast'][0]['low'] + " Degrees C")),
                    'Wind': (str(weather_data_buffalo['wind']['speed'] + " km/h")), \
                    'Condition': weather_data_buffalo['condition']['text']})
    keys_list_buffalo = data_dict_buffalo.keys()

    weather_id_hyd = connector.fetch_woeid('Hyderabad')
    weather_data_hyd = connector.fetch_weather(weather_id_hyd, metric=True)
    data_dict_hyd = {}
    data_dict_hyd.update({'Current Temperature': weather_data_hyd["condition"]["temp"], \
                    'Sunrise': weather_data_hyd['astronomy']['sunrise'], 'Sunset': weather_data_hyd['astronomy']['sunset'], \
                    'Max Temperature': (str(weather_data_hyd['forecast'][0]['high']) + " Degrees C"), \
                    'Min Temperature': (str(weather_data_hyd['forecast'][0]['low'] + " Degrees C")),
                    'Wind': (str(weather_data_hyd['wind']['speed'] + " km/h")), \
                    'Condition': weather_data_hyd['condition']['text']})
    keys_list_hyd = data_dict_hyd.keys()


    while status:
            main_display.fill(black)
            pointer_location = pygame.mouse.get_pos()
            pointer_click = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

#   Music Button
                if 700 < pointer_location[0] < 780 and 20 < pointer_location[1] < 50:
                    if pointer_click[0] == 1:
                        music_status = not music_status
                        if music_status == 0:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()

#   New York  Button Check
                if 20 < pointer_location[0] < 80 and 20 < pointer_location[1] < 50:
                    if pointer_click[0] == 1:
                        weather_location = 2
#   Buffalo  Button Check
                if 100 < pointer_location[0] < 160 and 20 < pointer_location[1] < 50:
                    if pointer_click[0] == 1:
                        weather_location = 1
#   Hyderabad  Button Check
                if 180 < pointer_location[0] < 240 and 20 < pointer_location[1] < 50:
                    if pointer_click[0] == 1:
                        weather_location = 0
#   Data Display
            if weather_location == 0:
                data_display(110, data_dict_hyd['Current Temperature'], white, 80, 160)  # Temperature number
                data_display(20, "Deg C", white, 180, 130)                           # Degree
                data_display(15, keys_list_hyd[5] + " : " + data_dict_hyd['Condition'], white, 95, 260)  # Condition
                data_display(15, keys_list_hyd[1] + " : " + data_dict_hyd['Min Temperature'], white, 130, 320)
                data_display(15, keys_list_hyd[6] + " : " + data_dict_hyd['Max Temperature'], white, 130, 360)
                data_display(15, keys_list_hyd[4] + " : " + data_dict_hyd['Sunrise'], white, 95, 400)   # Sunrise
                data_display(15, keys_list_hyd[0] + " : " + data_dict_hyd['Sunset'], white, 95, 440)    # Sunset
                data_display(15, keys_list_hyd[3] + " : " + data_dict_hyd['Wind'], white, 95, 480)  # Wind Speed
            elif weather_location == 1:
                data_display(110, data_dict_buffalo['Current Temperature'], white, 80, 160)  # Temperature number
                data_display(20, "Deg C", white, 180, 130)                           # Degree
                data_display(15, keys_list_buffalo[5] + " : " + data_dict_buffalo['Condition'], white, 95, 260)
                data_display(15, keys_list_buffalo[1] + " : " + data_dict_buffalo['Min Temperature'], white, 130, 320)
                data_display(15, keys_list_buffalo[6] + " : " + data_dict_buffalo['Max Temperature'], white, 130, 360)
                data_display(15, keys_list_buffalo[4] + " : " + data_dict_buffalo['Sunrise'], white, 95, 400)
                data_display(15, keys_list_buffalo[0] + " : " + data_dict_buffalo['Sunset'], white, 95, 440)    # Sunset
                data_display(15, keys_list_buffalo[3] + " : " + data_dict_buffalo['Wind'], white, 95, 480)  # Wind Speed
            elif weather_location == 2:
                data_display(110, data_dict_ny['Current Temperature'], white, 80, 160)  # Temperature number
                data_display(20, "Deg C", white, 180, 130)                           # Degree
                data_display(15, keys_list_ny[5] + " : " + data_dict_ny['Condition'], white, 95, 260)  # Condition
                data_display(15, keys_list_ny[1] + " : " + data_dict_ny['Min Temperature'], white, 130, 320)
                data_display(15, keys_list_ny[6] + " : " + data_dict_ny['Max Temperature'], white, 130, 360)
                data_display(15, keys_list_ny[4] + " : " + data_dict_ny['Sunrise'], white, 95, 400)   # Sunrise
                data_display(15, keys_list_ny[0] + " : " + data_dict_ny['Sunset'], white, 95, 440)    # Sunset
                data_display(15, keys_list_ny[3] + " : " + data_dict_ny['Wind'], white, 95, 480)  # Wind Speed
#   Buttons and Division Display
            pygame.draw.rect(main_display, white, (300, 0, 5, 600))
            pygame.draw.rect(main_display, white, (300, 70, 500, 5))
            drawbutton(white, 700, 20, 80, 30, 10, "Toggle Music", black)
            drawbutton(white, 20, 20, 60, 30, 10, "New York", black)
            drawbutton(white, 100, 20, 60, 30, 10, "Buffalo", black)
            drawbutton(white, 180, 20, 60, 30, 10, "Hyderabad", black)
#   Cursor Display
            main_display.blit(cursor_image, (pointer_location[0], pointer_location[1]))

            clock.tick(70)
            pygame.display.flip()

main()
