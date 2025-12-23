import turtle


# Малювання дерева
def draw_pythagoras_tree(t, order, size):
    if order == 0:
        return
    else:
        # Стовбур
        t.forward(size)
        
        # Ліва гілка
        t.left(45)
        draw_pythagoras_tree(t, order - 1, size * 0.7)
        
        # Права гілка - повертаємо на 90 градусів
        t.right(90)
        draw_pythagoras_tree(t, order - 1, size * 0.7)
        
        # Повертаємо кут назад - дивимося вздовж стовбура
        t.left(45)
        # Повертаємось назад у точку розгалуження
        t.backward(size)


# Візуалізація
def run_visualization(order):
    # Налаштування вікна
    window = turtle.Screen()
    window.setup(width=1000, height=800) 
    window.bgcolor("white")
    window.title(f"Дерево Піфагора (рівень {order})")
    
    t = turtle.Turtle()
    t.speed(0) 
    t.color("brown")
    
    # Товщина (2 пікселі)
    t.pensize(2)  
    
    # Розрахунок розміру, щоб втиснути дерево
    initial_size = 150 + (order * 5)
    
    # Позиціювання знизу екрана
    t.penup()
    t.goto(0, -350)
    t.left(90)
    t.pendown()
    
    # Малювання великих дерев без анімації (для швидкості)
    if order > 5:
        window.tracer(0)

    print(f"Малюємо дерево рівня {order}")
    
    draw_pythagoras_tree(t, order, initial_size)
    
    # Оновлюємо екран після завершення (для tracer(0))
    if order > 5:
        window.update()

    print("Дивиться в окремому вікні! Клікніть на нього для виходу.")
    window.exitonclick()


if __name__ == "__main__":
    try:
        user_input = input("Введіть рівень рекурсії (6-16): ")
        order = int(user_input)
        
        if order < 0:
            print("Рівень не може бути від'ємним.")
        else:
            run_visualization(order)
            
    except ValueError:
        print("Введіть ціле число.")
