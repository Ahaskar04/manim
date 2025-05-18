from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(RED, opacity=0.5)
        circle.set_stroke(BLUE, width=4)
        self.play(Create(circle))

class SquareToCircle(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        square.set_fill(RED, opacity=0.5)
        circle.set_fill(BLUE, opacity=0.5)
        self.play(Create(square))
        # square.rotate(PI/4)
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  
        circle.set_fill(PINK, opacity=0.5)  

        square = Square() 
        square.set_fill(BLUE, opacity=0.5) 

        square.next_to(circle, RIGHT, buff=0.5) 
        self.play(Create(circle), Create(square))  

class AnimateSquareToCircle(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        square.set_fill(RED, opacity=0.5)
        circle.set_fill(BLUE, opacity=0.5)
        self.play(Create(square))
        self.play(square.animate.rotate(PI/4))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))