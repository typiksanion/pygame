import pygame
import random
import time
import os
import platform



# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Настройки экрана
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('ЗАХВАТЧИКИ КИБКРБЕЗОПАСНОСТИ')
clock = pygame.time.Clock()

# Загрузка изображения
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    image_boom = load_image("boom.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)
        self.boom_frame = 0

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)

        # Проверка выхода за границы
        if self.rect.left < 0 or self.rect.right > width or self.rect.top < 0 or self.rect.bottom > height:
            self.rect.x = random.randrange(width)
            self.rect.y = random.randrange(height)

        # Проверка нажатия мыши
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom
            self.boom_frame = 1
            # Воспроизведение звука взрыва (вам нужно добавить его)
            explosion_sound.play()

        # Анимация взрыва (по желанию)
        if self.boom_frame:
            self.boom_frame += 1
            if self.boom_frame > 5:  # 5 кадров анимации взрыва
                self.kill()  # Удалить бомбу из игры

# Загрузка звука взрыва
explosion_sound = pygame.mixer.Sound("cartoon-water-bomb.mp3")  # Замените "explosion.wav" на имя вашего файла

# Группа, содержащая все спрайты
all_sprites = pygame.sprite.Group()

# Создание бомб
for i in range(20):
    Bomb(all_sprites)

# Основной цикл игры
running = True
while running:
    clock.tick(30)
    all_sprites.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)

    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    pygame.display.flip()


bg_image_menu = pygame.image.load('menu and quest.jpg')
bg_image_quest = pygame.image.load('menu and quest.jpg')
bg_image_game = pygame.image.load('game.jpg')
bg_image_boss = pygame.image.load('boss_2bg.jpg')


pygame.mixer.init()
pygame.mixer.music.load('ggg.mp3')
pygame.mixer.music.play(-1)

bulletSound = pygame.mixer.Sound('bullet_sound.mp3')
bulletSound.set_volume(0.2)
#Цвета
BLAC = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 128)

# Шрифты
font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Arial", 40)
bold_font = pygame.font.SysFont("Arial", 80, bold=True)

# Загружаем и изменяем размер изображений игроков и врагов
player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (50, 50))

enemy_image = pygame.image.load("enemy.png")
enemy_image = pygame.transform.scale(enemy_image, (40, 40))

# Загружаем изображения боссов
boss_image_1 = pygame.image.load("boss1.png")
boss_image_2 = pygame.image.load("boss2.png")
boss_image_1 = pygame.transform.scale(boss_image_1, (150, 150))  # Увеличиваем масштаб до большего размера
boss_image_2 = pygame.transform.scale(boss_image_2, (150, 150))  # Тот же размер анимации


#Настройки плеера
player_width = player_image.get_width()
player_height = player_image.get_height()
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 10
player_speed = 5
player_lives = 3

# Настройки маркера
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []
last_shot_time = 0
shoot_interval = 0.1

# Настройки противника
enemy_width = enemy_image.get_width()
enemy_height = enemy_image.get_height()
enemy_speed = 2
enemy_bullet_speed = 5
enemies = []
enemy_direction = 1
enemy_shoot_prob = 0.003
enemy_bullets = []

# Настройки босса
boss_width = boss_image_1.get_width()
boss_height = boss_image_1.get_height()
boss_x = (screen_width - boss_width) // 2
boss_y = 100  # Сдвигаем выступ немного вниз с 50 до 100
boss_speed = 3
boss_health = 100
boss_max_health = 100  # Общее состояние здоровья босса
boss_shoot_interval = 1.0  # Босс стреляет каждую 1 секунду
last_boss_shot_time = 0
boss_bullets = []
boss_animation_interval = 0.5  # Переключаем изображения каждые 0,5 секунды
last_boss_animation_time = 0
boss_current_image = boss_image_1  # Начинаем с первого изображения босса
boss_direction = 1  # 1 для правого, -1 для левого

# Настройки панели здоровья
health_bar_width = 200  # Общая ширина полосы работоспособности
health_bar_height = 20  # Высота планки работоспособности
health_bar_position = (screen_width // 2 - health_bar_width // 2, 10)  # По центру в верхней части экрана


# Игровые переменные
game_over = False
level = 1
total_levels = 2
boss_fight = False
clock = pygame.time.Clock()
show_title_screen = True
question_limit = 3
questions_asked = 0
asked_questions = []
message_displayed_time = 0
last_hit_time = 0  # Отслеживание последнего нажатия игрока
hit_duration = 1.5  # Продолжительность, в течение которой должно отображаться сообщение

# Определяем список вопросов по кибербезопасности с возможностью множественного выбора и правильными ответами на них
cybersecurity_questions = [
    {"question": "Что означает 'HTTPS'?",
     "options": ["A) Hypertext Transfer Protocol Standard", "B) Hypertext Transfer Protocol Secure", "C) High Transfer Protocol Secure"],
     "answer": "B"},

    {"question": "Что является распространенной формой фишинговой атаки?",
     "options": ["A) Электронная почта", "B) Телефонный звонок", "C) USB-накопитель"],
     "answer": "A"},

    {"question": "Какой тип вредоносной программы блокирует ваши файлы и требует оплаты?",
     "options": ["A) Вирус", "B) Червь", "C) Вирус-вымогатель"],
     "answer": "C"},

    {"question": "Что такое надежный пароль?",
     "options": ["A) Ваша дата рождения", "B) Комбинация букв, цифр и символов", "C) Имя вашего питомца"],
     "answer": "B"},

    {"question": "Что означает '2FA'?",
     "options": ["A) Двухфакторная аутентификация", "B) Двухфакторный доступ", "C) Двухфакторная надбавка"],
     "answer": "A"}
]

def wrap_text(text, font, max_width):
    """Обтекаем текст так, чтобы он соответствовал максимальной ширине при отрисовке заданным шрифтом."""
    words = text.split(' ')
    lines = []
    current_line = ''
    for word in words:
        test_line = current_line + word + ' '
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + ' '
    if current_line:
        lines.append(current_line)
    return lines

def ask_cybersecurity_question():
    """Задаем случайный вопрос о кибербезопасности и везвращаем значение True, если ответ правильный."""
    global bullets, enemy_bullets, questions_asked, asked_questions

    # Проверяем, достигнут ли лимит вопросов
    if questions_asked >= question_limit:
        return False  # Автоматически возвращает значение False, поскольку больше никаких вопросов задавать нельзя

    # Увеличиваем количество задаваемых вопросов
    questions_asked += 1

    # Удаляем все маркеры, когда будет задан вопрос
    bullets = []
    enemy_bullets = []

    # Выбераеи вопрос, который еще не был задан
    available_questions = [q for q in cybersecurity_questions if q not in asked_questions]

    if not available_questions:
        return False  # Больше вопросов нет

    question_data = random.choice(available_questions)
    asked_questions.append(question_data)  # Следим за заданным вопросом

    question = question_data["question"]
    options = question_data["options"]
    correct_answer = question_data["answer"]

    # Обернем текст вопроса
    question_lines = wrap_text(question, big_font, screen_width - 40)
    screen.blit(bg_image_quest, (0, 0))
    # Вычисляем начальную позицию y, чтобы центрировать текст по вертикали
    total_text_height = len(question_lines) * big_font.get_linesize()
    y_offset = screen_height // 2 - 150 - total_text_height // 2
    for i, line in enumerate(question_lines):
        question_text = big_font.render(line, True, WHITE)
        screen.blit(question_text, (screen_width // 2 - question_text.get_width() // 2, y_offset + i * big_font.get_linesize()))

    # Отображаем инструкцию о том, как ответить
    instruction_text = font.render("Используйте клавиши со стрелками для выбора варианта ответа", True, WHITE)
    screen.blit(instruction_text, (screen_width // 2 - instruction_text.get_width() // 2, screen_height // 2 + 100))

    pygame.display.flip()

    selected_index = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Проверяем выбранный ответ
                    selected_answer = chr(pygame.K_a + selected_index).upper()
                    if selected_answer == correct_answer:
                        display_feedback("Правильно!", GREEN)
                        return True
                    else:
                        display_feedback("Неправильно!", RED)
                        return False
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(options)
                elif event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(options)

        # Отображаем вопрос и варианты ответов, выделив выбранный из них
        screen.blit(bg_image_quest, (0, 0))
        # Повторное отображение строк с вопросами
        for i, line in enumerate(question_lines):
            question_text = big_font.render(line, True, WHITE)
            screen.blit(question_text, (screen_width // 2 - question_text.get_width() // 2, y_offset + i * big_font.get_linesize()))

        # Параметры отображения
        option_y_start = screen_height // 2 - 50
        for i, option in enumerate(options):
            color = GREEN if i == selected_index else WHITE
            option_lines = wrap_text(option, font, screen_width - 40)
            for j, line in enumerate(option_lines):
                option_text = font.render(line, True, color)
                line_y = option_y_start + i * 60 + j * font.get_linesize()
                screen.blit(option_text, (screen_width // 2 - option_text.get_width() // 2, line_y))

        screen.blit(instruction_text, (screen_width // 2 - instruction_text.get_width() // 2, screen_height // 2 + 150))
        pygame.display.flip()


def display_feedback(message, color):
    """Отображение обратной связи о том, был ли ответ правильным или неправильным."""
    screen.blit(bg_image_quest, (0, 0))
    feedback_text = bold_font.render(message, True, color)
    screen.blit(feedback_text, (screen_width // 2 - feedback_text.get_width() // 2, screen_height // 2 - feedback_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

def show_splash_screen():
    """Экран главного меню с кратким текстом и акцентом на ключевых фразах."""
    screen.blit(bg_image_menu, (0, 0))
    
    # Отображение названия игры
    title_text = bold_font.render('"ЗАХВАТЧИКИ', True, RED)
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 2 - 100 - title_text.get_height()))

    title_text = bold_font.render('кибербезопасности"', True, RED)
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 2 - title_text.get_height()))

    # Отображение названия игры
    controls_text1 = big_font.render("Используйте клавиши со стрелками", True, (255, 255, 0))
    screen.blit(controls_text1, (screen_width // 2 - controls_text1.get_width() // 2, screen_height // 2 + 50))

    controls_text2 = big_font.render("для перемещения и пробел для стрельбы", True, (255, 255, 0))
    screen.blit(controls_text2, (screen_width // 2 - controls_text2.get_width() // 2, screen_height // 2 + 100))

    # Дисплей "Нажмите любую клавишу, чтобы продолжить"
    continue_text = big_font.render("Нажмите любую клавишу, чтобы продолжить", True, WHITE)
    screen.blit(continue_text, (screen_width // 2 - continue_text.get_width() // 2, screen_height // 2 + 150))

    pygame.display.flip()
    
    # Ждем ввода данных пользователем или заданного времени
    wait_for_keypress()

def boss_fight_splash_screen():
    """Отображаем заставку, которая объявляет о битве с боссом и ожидает любого нажатия клавиши для продолжения."""
    screen.blit(bg_image_boss, (0, 0))

    # Выделяем жирным красным шрифтом надпись "Битва с боссом!"
    boss_fight_text = bold_font.render("Битва с боссом!", True, RED)
    screen.blit(boss_fight_text, (screen_width // 2 - boss_fight_text.get_width() // 2, screen_height // 2 - 100))

    # Выводим белым текстом надпись "Нажмите любую клавишу для продолжения".
    continue_text = big_font.render("Нажмите любую клавишу для продолжить", True, WHITE)
    screen.blit(continue_text, (screen_width // 2 - continue_text.get_width() // 2, screen_height // 2 + 50))

    pygame.display.flip()

    # Ждем, пока игрок нажмет любую клавишу
    wait_for_keypress()

def update_boss():
    global boss_x, last_boss_shot_time, boss_current_image, last_boss_animation_time, boss_direction, player_lives

    # Перемещаем босса влево и вправо
    boss_x += boss_speed * boss_direction
    if boss_x <= 0 or boss_x + boss_width >= screen_width:
        boss_direction *= -1  # Меняем направление при ударе о край

    # Переключаем изображение босса, чтобы создать простую анимацию
    current_time = time.time()
    if current_time - last_boss_animation_time >= boss_animation_interval:
        if boss_current_image == boss_image_1:
            boss_current_image = boss_image_2
        else:
            boss_current_image = boss_image_1
        last_boss_animation_time = current_time

    # Нарисуем босса
    screen.blit(boss_current_image, (boss_x, boss_y))

    # Нарисуем полосу здоровья босса
    draw_boss_health_bar()

    # Босс стреляет пулями в сторону игрока
    if current_time - last_boss_shot_time >= boss_shoot_interval:
        boss_bullets.append([boss_x + boss_width // 2, boss_y + boss_height])
        last_boss_shot_time = current_time

    # Обновляем пули босса
    for bullet in boss_bullets:
        bullet[1] += enemy_bullet_speed * 2  # Пули босса летят быстрее
        pygame.draw.rect(screen, YELLOW, (bullet[0], bullet[1], bullet_width, bullet_height))

        # Проверяем, попадают ли пули босса в игрока
        if player_x < bullet[0] < player_x + player_width and player_y < bullet[1] < player_y + player_height:
            boss_bullets.remove(bullet)
            last_hit_time = time.time()  # Обновить время последнего обращения
            if not ask_cybersecurity_question():
                player_lives -= 1
                if player_lives == 0:
                    game_over_screen()  # Запускайте игру, когда жизни заканчиваются.

        # Удаляем маркеры, которые исчезают за пределами экрана
        if bullet[1] > screen_height:
            boss_bullets.remove(bullet)

def check_boss_hit():
    global boss_health

    for bullet in bullets:
        if boss_x < bullet[0] < boss_x + boss_width and boss_y < bullet[1] < boss_y + boss_height:
            bullets.remove(bullet)
            boss_health -= 1

            if boss_health <= 0:
                boss_defeated_screen()  # Отображаем сообщение о поражении босса
                reset_game()  # Перезапускаем игру
                
def check_player_hit():
    global player_x, player_y, player_width, player_height, enemy_bullets
    for bullet in enemy_bullets:
        if player_x < bullet[0] < player_x + player_width and player_y < bullet[1] < player_y + player_height:
            enemy_bullets.remove(bullet)  #Удаляем пулю, попавшую в игрока
            return True  # Игрок был поражен
    return False  # Попадание не обнаружено



def boss_defeated_screen():
    screen.blit(bg_image_boss, (0, 0))
    defeated_text = bold_font.render("Босс повержен!", True, GREEN)
    screen.blit(defeated_text, (screen_width // 2 - defeated_text.get_width() // 2, screen_height // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    
def draw_boss_health_bar():
    """Нарисуем на экране полосу здоровья босса."""
    # Рассчитаем текущую ширину полосы здоровья, основываясь на состоянии здоровья босса
    current_health_ratio = boss_health / boss_max_health
    current_health_width = int(health_bar_width * current_health_ratio)

    # Нарисуем фон индикатора работоспособности (красным цветом по всей длине).
    pygame.draw.rect(screen, RED, (*health_bar_position, health_bar_width, health_bar_height))

    # Нарисуем текущее состояние здоровья (зеленое), основываясь на оставшемся состоянии босса
    pygame.draw.rect(screen, GREEN, (*health_bar_position, current_health_width, health_bar_height))

def wait_for_keypress():
    """Ждем, пока не будет нажата клавиша для продолжения."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def draw_player(x, y):
    screen.blit(player_image, (x, y))

def create_enemies():
    global enemies
    enemies = []
    for row in range(5):
        for col in range(10):
            enemy_x = col * (enemy_width + 10) + 50
            enemy_y = row * (enemy_height + 10) + 50
            enemies.append([enemy_x, enemy_y])

def draw_enemies():
    for enemy in enemies:
        screen.blit(enemy_image, (enemy[0], enemy[1]))

def update_enemies():
    global enemy_direction, game_over, level, boss_fight
    if not enemies:
        if level < total_levels:
            level += 1
            increase_difficulty()  # Увеличиваем сложность при повышении уровня
            create_enemies()
        else:
            boss_fight_splash_screen()
            boss_fight = True

    edge_reached = False
    for enemy in enemies:
        enemy[0] += enemy_speed * enemy_direction
        if enemy[0] <= 0 or enemy[0] + enemy_width >= screen_width:
            edge_reached = True

        if random.random() < enemy_shoot_prob:
            enemy_bullets.append([enemy[0] + enemy_width // 2, enemy[1] + enemy_height])

        if enemy[1] + enemy_height >= screen_height:
            game_over_screen()

    if edge_reached:
        for enemy in enemies:
            enemy[1] += 20
        enemy_direction *= -1

def increase_difficulty():
    """Увеличиваем сложность, ускоряя врагов или изменяя вероятность выстрела."""
    global enemy_speed, enemy_shoot_prob
    enemy_speed += 0.5
    enemy_shoot_prob += 0.001

def update_bullets():
    for bullet in bullets:
        bullet[1] -= bullet_speed
        pygame.draw.rect(screen, GREEN, (bullet[0], bullet[1], bullet_width, bullet_height))

        if bullet[1] < 0:
            bullets.remove(bullet)

        for enemy in enemies:
            if enemy[0] < bullet[0] < enemy[0] + enemy_width and enemy[1] < bullet[1] < enemy[1] + enemy_height:
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

def update_enemy_bullets():
    global player_lives, last_hit_time, player_lives
    for bullet in enemy_bullets:
        bullet[1] += enemy_bullet_speed
        pygame.draw.rect(screen, RED, (bullet[0], bullet[1], bullet_width, bullet_height))

        if bullet[1] > screen_height:
            enemy_bullets.remove(bullet)

        # Проверяем столкновение с игроком
        if player_x < bullet[0] < player_x + player_width and player_y < bullet[1] < player_y + player_height:
            enemy_bullets.remove(bullet)
            last_hit_time = time.time()  # Обновляем время последнего обращения
            if not ask_cybersecurity_question():
                player_lives -= 1
                if player_lives == 0:
                    game_over_screen()  # Запускаем игру, когда жизни заканчиваются.


def game_over_screen():
    """Отображает экран завершения игры с опциями перезапуска или выхода из игры"""
    screen.fill(RED)  # Красный фон

    # Вывод жирным белым шрифтом надпись "ИГРА ОКОНЧЕНА!"
    game_over_text = bold_font.render("ИГРА ОКОНЧЕНА!", True, WHITE)
    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - 100))

    # Отобразятся инструкция по нажатию "R" для перезапуска или "Q" для выхода
    instruction_text = big_font.render("Нажмите R для перезапуска или Q для выхода", True, WHITE)
    screen.blit(instruction_text, (screen_width // 2 - instruction_text.get_width() // 2, screen_height // 2 + 50))

    pygame.display.flip()

    # Ждеи, пока игрок нажмет "R" или "Q"
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Нажмите "R" для перезапуска
                    waiting_for_input = False
                    reset_game()
                elif event.key == pygame.K_q:  # Нажмите "Q", чтобы выйти
                    pygame.quit()
                    quit()


def reset_game():
    """Сбросим игровые переменные и начнем все сначала."""
    global player_lives, bullets, enemy_bullets, level, boss_fight, questions_asked, message_displayed_time, last_hit_time, asked_questions
    player_lives = 3
    bullets = []
    enemy_bullets = []
    level = 1
    questions_asked = 0
    message_displayed_time = 0
    asked_questions = []
    last_hit_time = 0 
    boss_fight = False
    create_enemies()
    main_game_loop()


def main_game_loop():
    global player_x, player_y, last_shot_time, boss_fight

    player_hit = False
    
    while not game_over:
        screen.blit(bg_image_game, (0, 0))

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Обработка ключей
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_SPACE]:
            if time.time() - last_shot_time >= shoot_interval:
                bullets.append([player_x + player_width // 2, player_y])
                last_shot_time = time.time()
        if keys[pygame.K_SPACE]:
            bulletSound.play()
        # Убеждаемся, что игрок не уходит за пределы экрана
        if player_x < 0:
            player_x = 0
        if player_x + player_width > screen_width:
            player_x = screen_width - player_width

        draw_player(player_x, player_y)
        update_bullets()

        if boss_fight:
            update_boss()
            check_boss_hit()

        else:
            update_enemies()
            draw_enemies()
            update_enemy_bullets()  # Убеждаемся, что вражеские пули обновлены здесь

        # Проверяем, не попала ли в игрока вражеская пуля
        if check_player_hit():
            player_hit = True

        # Отображение жизней и уровня игрока
        lives_text = font.render(f"Жизни: {player_lives}", True, WHITE)
        screen.blit(lives_text, (10, 10))


        pygame.display.update()
        clock.tick(60)


        
def main():
    create_enemies()
    show_splash_screen()
    main_game_loop()

main()

