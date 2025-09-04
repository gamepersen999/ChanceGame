import pygame
#change None to any font you want, I used cour.ttf which I downloaded, use a path to get there

def ChanceGameW():
    import random as randint
    pygame.init()
    width, height = 800,600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("ChanceGame")

    black = (0,0,0)
    white = (255,255,255)
    cyan = (0,255,255)
    red = (255,0,0)
    green = (0,255,0)
    deathcolor = (150,0,0)
    startbuttonrect = pygame.Rect(250,400,300,130)
    state = 1
    titlefont = pygame.font.Font(None, 100)
    titleorg = 1
    instructfont = pygame.font.Font(None, 75)
    opt1rect = pygame.Rect(60,420,150,150)
    opt2rect = pygame.Rect(230,420,150,150)
    opt3rect = pygame.Rect(400,420,150,150)
    opt4rect = pygame.Rect(570,420,150,150)
    optfonts = pygame.font.Font("cour.ttf", 40)
    playerchoice = 0
    resfont = pygame.font.Font(None, 80)
    roundsleftfont = pygame.font.Font("cour.ttf", 55)
    losingnumberfont = pygame.font.Font("cour.ttf", 45)
    losingchoice = 0
    losingchoice2 = 0
    losingchoice3 = 0
    quitrect = pygame.Rect(325,400,150,80)
    quitfont = pygame.font.Font(None, 65)

    while True:
        mousepos = pygame.mouse.get_pos()
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                return
            if eve.type == pygame.MOUSEBUTTONDOWN:
                if state == 1:
                    if startbuttonrect.collidepoint(mousepos):
                        state = 2
                        rounds = 10
                elif state == 2:
                    if opt1rect.collidepoint(mousepos):
                        playerchoice = 1
                        state = 3
                    elif opt2rect.collidepoint(mousepos):
                        playerchoice = 2
                        state = 3
                    elif opt3rect.collidepoint(mousepos):
                        playerchoice = 3
                        state = 3
                    elif opt4rect.collidepoint(mousepos):
                        playerchoice = 4
                        state = 3
        if state == 1:
            pygame.time.Clock().tick(5)
            screen.fill(white)
            if titleorg % 5 == 1:
                title = titlefont.render(">    ChanceGame    <", True, black)
            elif titleorg % 5 == 2:
                title = titlefont.render(" >   ChanceGame   < ", True, black)
            elif titleorg % 5 == 3:
                title = titlefont.render("  >  ChanceGame  <  ", True, black)
            elif titleorg % 5 == 4:
                title = titlefont.render("   > ChanceGame <   ", True, black)
            else:
                title = titlefont.render("    >ChanceGame<    ", True, black)
            titleorg += 1
            screen.blit(title, (60,100))
            pygame.draw.rect(screen, cyan, startbuttonrect)
            inst = titlefont.render("Start", True, black)
            screen.blit(inst, inst.get_rect(center = startbuttonrect.center))
        elif state == 2:
            pygame.time.Clock().tick(30)
            screen.fill(black)
            if rounds > 5:
                warn_inst = instructfont.render("One number is losing.", True, white)
            elif rounds >= 3:
                warn_inst = instructfont.render("2 numbers are losing.", True, white)
            elif 3 > rounds > 0:
                warn_inst = instructfont.render("3 numbers are losing.", True, white)
            warn_inst_2 = instructfont.render("Don't pick that number.", True, red)
            pygame.draw.rect(screen,cyan,opt1rect)
            pygame.draw.rect(screen,cyan,opt2rect)
            pygame.draw.rect(screen,cyan,opt3rect)
            pygame.draw.rect(screen,cyan,opt4rect)
            screen.blit(warn_inst, (130,40))
            screen.blit(warn_inst_2, (120, 120))
            opt1no = optfonts.render("1", True, black)
            opt2no = optfonts.render("2", True, black)
            opt3no = optfonts.render("3", True, black)
            opt4no = optfonts.render("4", True, black)
            screen.blit(opt1no, opt1no.get_rect(center = opt1rect.center))
            screen.blit(opt2no, opt2no.get_rect(center = opt2rect.center))
            screen.blit(opt3no, opt3no.get_rect(center = opt3rect.center))
            screen.blit(opt4no, opt4no.get_rect(center = opt4rect.center))
        else:
            while rounds != 0:
                pygame.time.Clock().tick(30)
                screen.fill(black)
                if rounds > 5:
                    losingchoice = randint.randint(1,4)
                    losingnumber = losingnumberfont.render(f"Losing number: {losingchoice}      ", True, red)
                elif rounds >= 3:
                    losingchoice = randint.randint(1, 4)
                    losingchoice2 = randint.randint(1, 4)
                    while losingchoice2 == losingchoice:
                        losingchoice2 = randint.randint(1, 4)
                    losingnumber = losingnumberfont.render(f"Losing number: {losingchoice}, {losingchoice2}   ", True, red)
                elif 3 > rounds > 0:
                    losingchoice = randint.randint(1, 4)
                    losingchoice2 = randint.randint(1, 4)
                    losingchoice3 = randint.randint(1, 4)
                    while losingchoice2 == losingchoice:
                        losingchoice2 = randint.randint(1, 4)
                    while losingchoice3 == losingchoice or losingchoice3 == losingchoice2:
                        losingchoice3 = randint.randint(1, 4)
                    losingnumber = losingnumberfont.render(f"Losing number: {losingchoice}, {losingchoice2}, {losingchoice3}", True, red)

                if playerchoice != losingchoice and playerchoice != losingchoice2 and playerchoice != losingchoice3:
                    screen.fill(black)
                    result = resfont.render("Survived.", True, green)
                    roundsleft = roundsleftfont.render(f"{rounds} rounds left.", True, red)
                    screen.blit(result, (270,230))
                    screen.blit(roundsleft, (180, 280))
                    screen.blit(losingnumber, (130, 350))
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    state = 2
                    rounds -= 1
                    break
                else:
                    screen.fill(black)
                    result = resfont.render("Dead.", True, deathcolor)
                    screen.blit(result, (300,230))
                    screen.blit(losingnumber, (130, 350))
                    pygame.display.flip()
                    pygame.time.delay(1250)
                    pygame.draw.rect(screen, red, quitrect)
                    quitword = quitfont.render("Quit", True, black)
                    screen.blit(quitword, quitword.get_rect(center = quitrect.center))
                    pygame.display.flip()
                    waitingquit = True
                    while waitingquit:
                        mousepos = pygame.mouse.get_pos()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if quitrect.collidepoint(mousepos):
                                    pygame.quit()
                            
                    

            if rounds == 0:
                screen.fill(black)
                winfont = pygame.font.Font(None, 150)
                win = winfont.render("Win!", True, black)
                screen.blit(win, win.get_rect(center = (400,300)))
                infofont = pygame.font.Font("cour.ttf", 45)
                info = infofont.render("ChanceGame finished | 1 in 720 chance (0.139%)")
                screen.blit(info, info.get_rect(center = (400,400)))
                pygame.display.flip()


        pygame.display.flip()
        pygame.time.Clock().tick(35)

def ChanceGameT():
    import random
    print("One number is losing. Don't pick that number.")
    player = "n"
    playerattempts = 10

    while player != "win":
        if playerattempts != 0:
            if playerattempts > 5:
                print("One number will make you lose.")
                losingchoice = random.randint(1, 4)
                playerchoice = input("What is your choice? Choose a number between 1, 2, 3, and 4. ")
                if playerchoice.isdigit():
                    playerchoice = int(playerchoice)
                else:
                    playerchoicenumber = ""
                    for ch in playerchoice:
                        if ch.isdigit():
                            playerchoicenumber += ch
                    if playerchoicenumber == "":
                        playerchoice = 0
                    else:
                        playerchoice = int(playerchoicenumber)
                if playerchoice > 4:
                    playerchoice = 4
                    print("Registered as 4.")
                if playerchoice < 1:
                    playerchoice = 1
                    print("Registered as 1.")
                if playerchoice != losingchoice:
                    print("Survived.")
                    print(f"{playerattempts} times left.")
                    print("Losing Number:", losingchoice)
                    playerattempts -= 1
                else:
                    print("You Lose.")
                    print("Losing Number:", losingchoice)
                    break

            elif playerattempts >= 3:
                print("2 numbers will make you lose.")
                losingchoice = random.randint(1, 4)
                losingchoice2 = random.randint(1, 4)

                while losingchoice2 == losingchoice:
                    losingchoice2 = random.randint(1, 4)

                playerchoice = input("What is your choice? Choose a number between 1, 2, 3, and 4. ")
                if playerchoice.isdigit():
                    playerchoice = int(playerchoice)
                else:
                    playerchoicenumber = ""
                    for ch in playerchoice:
                        if ch.isdigit():
                            playerchoicenumber += ch
                    if playerchoicenumber == "":
                        playerchoice = 0
                    else:
                        playerchoice = int(playerchoicenumber)
                if playerchoice > 4:
                    playerchoice = 4
                    print("Registered as 4.")
                if playerchoice < 1:
                    playerchoice = 1
                    print("Registered as 1.")
                if playerchoice != losingchoice and playerchoice != losingchoice2:
                    print("Survived.")
                    print(f"{playerattempts} times left.")
                    print(f"Losing Numbers: {losingchoice}, {losingchoice2}")
                    playerattempts -= 1
                else:
                    print("You Lose.")
                    print(f"Losing Numbers: {losingchoice}, {losingchoice2}")
                    break

            elif 3 > playerattempts > 0:
                print("3 numbers will make you lose.")
                losingchoice = random.randint(1, 4)
                losingchoice2 = random.randint(1, 4)
                losingchoice3 = random.randint(1, 4)

                while losingchoice2 == losingchoice:
                    losingchoice2 = random.randint(1, 4)
                while losingchoice3 == losingchoice or losingchoice3 == losingchoice2:
                    losingchoice3 = random.randint(1, 4)

                playerchoice = input("What is your choice? Choose a number between 1, 2, 3, and 4. ")
                if playerchoice.isdigit():
                    playerchoice = int(playerchoice)
                else:
                    playerchoicenumber = ""
                    for ch in playerchoice:
                        if ch.isdigit():
                            playerchoicenumber += ch
                    if playerchoicenumber == "":
                        playerchoice = 0
                    else:
                        playerchoice = int(playerchoicenumber)
                if playerchoice > 4:
                    playerchoice = 4
                    print("Registered as 4.")
                if playerchoice < 1:
                    playerchoice = 1
                    print("Registered as 1.")
                if playerchoice != losingchoice and playerchoice != losingchoice2 and playerchoice != losingchoice3:
                    print("Survived.")
                    print(f"{playerattempts} times left.")
                    print(f"Losing Numbers: {losingchoice}, {losingchoice2}, {losingchoice3}")
                    playerattempts -= 1
                else:
                    print("You Lose.")
                    print(f"Losing Numbers: {losingchoice}, {losingchoice2}, {losingchoice3}")
                    break

        else:
            print("You Win!")
            player = "win"

def ChanceGame():
    playerchoice = input("Which version of ChanceGame would you like?\n[1] ChanceGame Window Version\n[2] ChanceGame Text Version\n >>> ")
    while playerchoice != '1' and playerchoice != '2':
        print("Invalid Option.")
        playerchoice = input("Which version of ChanceGame would you like?\n[1] ChanceGame Window Version\n[2] ChanceGame Text Version\n >>> ")
    playerchoice = int(playerchoice)
    if playerchoice == 1:
        ChanceGameW()
    else:
        ChanceGameT()
if __name__ == "__main__":
    ChanceGame()