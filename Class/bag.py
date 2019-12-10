import pygame, sys, os

from .map import X_RANGE, Y_RANGE
dir_path = os.path.dirname(os.path.abspath(__file__))


BAG_IMGAE = {'bag_bg' : pygame.image.load(dir_path+'/../image/bag_bg.png'),
             'poke_balls' : pygame.image.load(dir_path+'/../image/poke_balls.png')}

BAGDEX = { 1:'PokeBalls'}

def display_text(bat_surf, str, pos):

    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render(str, True, (128,128,128))
    textRectObj = textSurfaceObj.get_rect()
    bat_surf.blit(textSurfaceObj, pos)

# def display_rect(move_to, offset):
#     if move_to is 'LEFT' and offset > 0: offset -= 1        
#     if move_to is 'RIGHT' and offset < 3: offset += 1
#     if move_to is 'UP' and offset > 1: offset -= 2      
#     if move_to is 'DOWN' and offset < 2 : offset += 2
#     return offset

class Items():

    def __init__(self, name, num, description, image) :
        self.name = name
        self.num = num
        self.description = description
        self.image = image

#draw an unfilled square
# pygame.draw.rect(background, (0, 255, 0), ((200, 5), (100, 100)), 3)

class Interface():
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        if name == 'Poké balls':
            self.items = [Items('PokeBalls', 5, 'Catching wild Pokémon props', BAG_IMGAE['poke_balls']),
                        Items('PokeBalls', 5, 'Catching wild Pokémon props', BAG_IMGAE['poke_balls'])]
        else :self.items = []


class Bag():

    def __init__(self) :
        self.balls = None
        self.items = None
        self.current_interface = 1
        self.current_item = 0
        self.interfaces = [Interface('Items',(95,50)),Interface('Poké balls',(65,50))]

    # def draw_bag_items(self,bag_surf):
    #     for i in range(len(self.balls)):
    #         if self.balls[i].item_name == BAGDEX[1]:
    #             bag_surf.blit(pygame.transform.scale(BAG_IMGAE['poke_balls'],(50,50)), (350,35)) #  上方圖片
    #             display_text(bag_surf, self.balls[i].item_name, (425,50))
    #             display_text(bag_surf, 'X'+ str(self.balls[i].num), (700,50)) # 幾個 ex. X5
    #             bag_surf.blit(pygame.transform.scale(BAG_IMGAE['poke_balls'],(50,50)),(35,500)) # 下方圖片
    #             display_text(bag_surf, self.balls[i].description, (150, 500)) # 下方圖片說明
                
    #             pygame.draw.rect(bag_surf, (255, 0, 0), ((290, 25), (485, 65)), 5)

    # def draw_bag(self, move_to) :
    #     bag_surf = pygame.Surface((X_RANGE, Y_RANGE))
    #     bag_surf.blit(pygame.transform.scale(BAG_IMGAE['bag_bg'],(800,600)), (0,0))
    #     if move_to == 'LEFT':
    #         display_text(bag_surf, self.interface[self.current_interface][0],self.interface[self.current_interface][1])
    #     else:
    #         display_text(bag_surf, 'Poké balls',(65,50))
    #         balls_list, item_list = [],[]
    #         balls = Items('PokeBalls', 5, 'Catching wild Pokémon props')
    #         balls_list.append(balls)
    #         self.balls = balls_list
    #         self.draw_bag_items(bag_surf)
    #         # item_list.append(balls)

    def draw_bag(self, move_to) :
        bag_surf = pygame.Surface((X_RANGE, Y_RANGE))
        bag_surf.blit(pygame.transform.scale(BAG_IMGAE['bag_bg'],(800,600)), (0,0))
        if move_to == 'LEFT' and self.current_interface > 0: self.current_interface -= 1
        elif move_to == 'RIGHT' and self.current_interface < len(self.interfaces)-1 : self.current_interface += 1
        elif move_to == 'UP' and self.current_item > 0: self.current_item -= 1
        elif move_to == 'DOWN' and self.current_item < len(self.interfaces[self.current_interface].items) -1 : self.current_item += 1


        display_text(bag_surf, self.interfaces[self.current_interface].name,self.interfaces[self.current_interface].pos)
        self.draw_bag_items(bag_surf, self.interfaces[self.current_interface])
        return bag_surf

    def draw_bag_items(self,bag_surf, interface):
        if len(interface.items) is not 0 :
            index = 0
            for i in interface.items:         
                bag_surf.blit(pygame.transform.scale(i.image,(50,50)), (350,35+index*60)) #  上方圖片
                display_text(bag_surf, i.name, (425,50+index*60))    
                display_text(bag_surf, 'X'+ str(i.num), (700,50+index*60)) # 幾個 ex. X5 
                index += 1
                
            bag_surf.blit(pygame.transform.scale(interface.items[self.current_item].image,(50,50)),(35,500)) # 下方圖片
            display_text(bag_surf, interface.items[self.current_item].description, (150, 500)) # 下方圖片說明
            pygame.draw.rect(bag_surf, (255, 0, 0), ((290, 25+(self.current_item*63)), (485, 65)), 5)