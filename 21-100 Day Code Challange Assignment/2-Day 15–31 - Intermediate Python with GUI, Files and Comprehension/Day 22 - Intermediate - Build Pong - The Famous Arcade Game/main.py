import turtle
import time

# Setup layar
screen = turtle.Screen()
screen.title("Collision Detection Visualization")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Paddle setup
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)  # Height = 100 (5*20), Width = 20 (1*20)
paddle.penup()
paddle.goto(0, 0)  # Paddle berada di tengah layar

# Bola setup
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(1)
ball.goto(0, 150)  # Awal posisi bola di atas paddle


# Fungsi untuk menampilkan zona jarak
def draw_zone():
    zone = turtle.Turtle()
    zone.hideturtle()
    zone.penup()
    zone.color("yellow")
    zone.goto(paddle.xcor() - 20, paddle.ycor() + 50)  # Atas kiri zona
    zone.pendown()
    zone.begin_fill()
    # Menggambar zona (horizontal width=20, vertikal height=100)
    zone.goto(paddle.xcor() + 20, paddle.ycor() + 50)  # Atas kanan
    zone.goto(paddle.xcor() + 20, paddle.ycor() - 50)  # Bawah kanan
    zone.goto(paddle.xcor() - 20, paddle.ycor() - 50)  # Bawah kiri
    zone.goto(paddle.xcor() - 20, paddle.ycor() + 50)  # Kembali ke atas kiri
    zone.end_fill()


# Deteksi tabrakan
def check_collision():
    # Menghitung jarak horizontal dan vertikal
    horizontal_distance = abs(ball.xcor() - paddle.xcor())
    vertical_distance = abs(ball.ycor() - paddle.ycor())

    # Jika bola berada di area pantulan
    if horizontal_distance < 20 and vertical_distance < 50:
        ball.color("green")  # Warna kuning jika dalam zona pantulan
    else:
        ball.color("red")  # Warna merah jika di luar zona


# Gerakan bola untuk demonstrasi
def move_ball():
    ball.sety(ball.ycor() - 5)  # Bola bergerak turun
    check_collision()
    screen.ontimer(move_ball, 50)  # Panggil lagi fungsi setiap 50ms


# Menggambar zona jarak
draw_zone()

# Mulai gerakan bola
move_ball()

# Menjaga jendela tetap terbuka
screen.mainloop()
