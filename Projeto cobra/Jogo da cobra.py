#configurações  iniciais
import pygame
import random

pygame.init()
pygame.display.set_caption("Jogo Snake Python")
largura, altura = 1280, 800

fundo = pygame.image.load("./fundoi.png")
corpo = pygame.image.load("./corpopepa.png")
cabeca = pygame.image.load("./cabecapepa.png")
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()


#cores
preto = (0 ,0 ,0)
branca = (255,255,255,)
vermelho = (255,0,0)
verde = (0,255,0)

#parametros da cobrinha
tamanho_quadrado = 20
velocidade_cobra = 20
tamanho_cobra = 1

comida_ = pygame.image.load("./comidapf.png")
comida_= pygame.transform.scale(comida_,(tamanho_quadrado ,tamanho_quadrado))

cabeca_ = pygame.image.load("./cabecapepa.png")
cabeca= pygame.transform.scale(cabeca,(tamanho_quadrado ,tamanho_quadrado))

corpo = pygame.image.load("./corpopepa.png")
corpo = pygame.transform.scale(corpo,(tamanho_quadrado ,tamanho_quadrado))

#1 usage
def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0
    return comida_x, comida_y
    
#1 usage
def desenhar_cobra(tamanho , pixels):
    for pixel in pixels:
        #pygame.draw.rect(tela, preto,[pixel[0],pixel[1], tamanho, tamanho]) 
         if(tamanho_cobra == 1):
            tela.blit(cabeca,(pixel[0], pixel[1], tamanho, tamanho) )
         elif tamanho_cobra > 1:
            tela.blit(corpo,(pixel[0], pixel[1], tamanho, tamanho) )
             

    #print("Posição 0:",pixels[0])
        
       # if(tamanho_cobra == 1):
       #     tela.blit(cabeca,(pixel[0], pixel[1], tamanho, tamanho) )
       # else:
       #     tela.blit(corpo,(pixel[0], pixel[1], tamanho, tamanho) )

        
#1 usage
def desenhar_comida(tamanho, comida_x, comida_y):
    #pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho, tamanho])
    tela.blit(comida_,(comida_x ,comida_y))
#1 usage
def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("helvetica", 35)
    texto = fonte.render(f"pontos: {pontuacao}", True , verde)
    tela.blit(texto, [1,1])

#1 usage
def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y =  tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = - tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = - tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y
 
# 1 usage
def rodar_jogo():
    fim_jogo = False

    x = largura /2
    y = altura /2

    global tamanho_cobra

    
    pixels = []

    comida_x, comida_y = gerar_comida()

    velocidade_x = 0
    velocidade_y = 0

    
    while not fim_jogo:
        tela.fill(preto)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        tela.blit(fundo,(0,0))
#desenhar comida
        desenhar_comida(tamanho_quadrado , comida_x , comida_y)

#atualizar a posição da cobra
        if x < 0 or x >= largura or y < 0 or y>= altura:
            fim_jogo = True

        x += velocidade_x
        y += velocidade_y

#desenhar cobra
        pixels.append([x,y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        
       

#se a cobra batel no proprio corbor
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        desenhar_cobra(tamanho_quadrado, pixels)

#desenhar pontos
        desenhar_pontuacao(tamanho_cobra -1)
        

#atualização da tela
        pygame.display.update()

#criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y =gerar_comida()

        relogio.tick(velocidade_cobra)

#criar loop infinito

rodar_jogo()
pygame.quit()