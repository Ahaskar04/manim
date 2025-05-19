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

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()

class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(0.5)  # wait for 0.5 seconds
        self.replacement_transform()

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)

class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        # place the circle two units left from the origin
        circle.move_to(LEFT * 2)
        # place the square to the left of the circle
        square.next_to(circle, LEFT)
        # align the left border of the triangle to the left border of the circle
        triangle.align_to(circle, LEFT)

        self.add(circle, square, triangle)
        self.wait(1)

class AnimateExample(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        # animate the change of color
        self.play(square.animate.set_fill(WHITE), run_time = 20)
        # self.wait(1)
        self.wait(10)

        # animate the change of position and the rotation at the same time
        self.play(square.animate.shift(UP).rotate(PI / 3))
        self.wait(1)

from manim import *

class MobjectExample(Scene):
    def construct(self):
        p1 = [-1,-1, 0]
        p2 = [ 1,-1, 0]
        p3 = [ 1, 1, 0]
        p4 = [-1, 1, 0]
        a  = Line(p1,p2).append_points(Line(p2,p3).points).append_points(Line(p3,p4).points)
        point_start  = a.get_start()
        point_end    = a.get_end()
        point_center = a.get_center()
        self.add(Text(f"a.get_start() = {np.round(point_start,2).tolist()}", font_size=24).to_edge(UR).set_color(YELLOW))
        self.add(Text(f"a.get_end() = {np.round(point_end,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(RED))
        self.add(Text(f"a.get_center() = {np.round(point_center,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(BLUE))

        self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        self.add(Dot(a.get_end()).set_color(RED).scale(2))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[Dot(x) for x in a.points])
        self.add(a)

class ExampleTransform(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1 = Square().set_color(RED)
        m2 = Rectangle().set_color(RED).rotate(0.2)
        self.play(Transform(m1,m2))

class ShowScreenResolution(Scene):
    def construct(self):
        pixel_height = config["pixel_height"]  #  1080 is default
        pixel_width = config["pixel_width"]  # 1920 is default
        frame_width = config["frame_width"]
        frame_height = config["frame_height"]
        self.add(Dot())
        d1 = Line(frame_width * LEFT , frame_width * RIGHT ).to_edge(DOWN)
        self.add(d1)
        self.add(Text(str(pixel_width)).next_to(d1, UP))
        d2 = Line(frame_height * UP / 2, frame_height * DOWN / 2).to_edge(LEFT)
        self.add(d2)
        self.add(Text(str(pixel_height)).next_to(d2, RIGHT))

class ZoomedOutScene(Scene):
    def construct(self):
        # Default frame height is 8.0 → Let’s zoom out
        config.frame_height = 16.0  # double the height (zoom out)

        # Add cross grid
        self.add(NumberPlane())

        # Show center
        self.add(Dot(color=RED))

        # Draw boundary box of frame
        frame_box = Rectangle(width=config.frame_width, height=config.frame_height)
        frame_box.set_stroke(YELLOW, width=2)
        self.add(frame_box)

        self.wait()


class SIZoo(MovingCameraScene):
    def construct(
        self,
        units = [
            ("Length", "m", "#a2d2ff"),
            ("Mass", "kg", "#ffc9de"),
            ("Time", "s", "#caffbf"),
            ("Electric Current", "A", "#fdffb6"),
            ("Temperature", "K", "#ffd6a5"),
            ("Amount", "mol", "#bdb2ff"),
            ("Luminous Intensity", "cd", "#ffadad"),
        ],
        highlight_script = [],
        highlight_style = "indicate",  # "indicate", "red_flash", or "wiggle"
        show_previous_units = False
    ):
        spacing = 5
        unit_groups = []
        unit_name_to_group = {}

        # Create visual elements
        for i, (name, symbol, color) in enumerate(units):
            icon = Circle(radius=0.5, color=color, fill_opacity=0.8).shift(UP * 0.5)
            label = Text(name, font_size=28).next_to(icon, DOWN, buff=0.3)
            symbol_text = Text(symbol, font_size=24).next_to(icon, UP, buff=0.3)

            group = VGroup(icon, label, symbol_text).move_to(RIGHT * spacing * i)
            unit_groups.append(group)
            unit_name_to_group[name] = group

        # Offset so first unit is centered
        total_width = spacing * (len(units) - 1)
        offset = LEFT * total_width / 2
        for group in unit_groups:
            group.shift(offset)

        # Animate unit by unit
        last_group = None
        for group, (name, _, _) in zip(unit_groups, units):
            self.play(FadeIn(group), run_time=0.5)
            self.play(self.camera.frame.animate.move_to(group), run_time=0.5)
            self.wait(0.2)

            # Highlight logic
            if name in highlight_script:
                if highlight_style == "indicate":
                    self.play(Indicate(group))
                elif highlight_style == "red_flash":
                    group.set_color(RED)
                    self.wait(0.3)
                    group.set_color(WHITE)
                elif highlight_style == "wiggle":
                    self.play(Wiggle(group))

            if last_group and not show_previous_units:
                self.play(FadeOut(last_group), run_time=0.2)

            last_group = group

        self.wait(1)

class SIZoo2(MovingCameraScene):
    def construct(self):
        units = getattr(self, "units", [
            ("Length", "m", "#a2d2ff"),
            ("Mass", "kg", "#ffc9de"),
            ("Time", "s", "#caffbf"),
            ("Electric Current", "A", "#fdffb6"),
            ("Temperature", "K", "#ffd6a5"),
            ("Amount", "mol", "#bdb2ff"),
            ("Luminous Intensity", "cd", "#ffadad"),
        ])
        highlight_script = getattr(self, "highlight_script", [])
        highlight_style = getattr(self, "highlight_style", "indicate")
        show_previous_units = getattr(self, "show_previous_units", False)

        spacing = 5
        unit_groups = []
        unit_name_to_group = {}

        for i, (name, symbol, color) in enumerate(units):
            icon = Circle(radius=0.5, color=color, fill_opacity=0.8).shift(UP * 0.5)
            label = Text(name, font_size=28).next_to(icon, DOWN, buff=0.3)
            symbol_text = Text(symbol, font_size=24).next_to(icon, UP, buff=0.3)

            group = VGroup(icon, label, symbol_text).move_to(RIGHT * spacing * i)
            unit_groups.append(group)
            unit_name_to_group[name] = group

        total_width = spacing * (len(units) - 1)
        offset = LEFT * total_width / 2
        for group in unit_groups:
            group.shift(offset)

        last_group = None
        for group, (name, _, _) in zip(unit_groups, units):
            self.play(FadeIn(group), run_time=0.5)
            self.play(self.camera.frame.animate.move_to(group), run_time=0.5)
            self.wait(0.2)

            if name in highlight_script:
                if highlight_style == "indicate":
                    self.play(Indicate(group))
                elif highlight_style == "red_flash":
                    group.set_color(RED)
                    self.wait(0.3)
                    group.set_color(WHITE)
                    self.wait(0.3)
                    group.set_color(RED)
                    self.wait(0.3)
                    group.set_color(WHITE)
                    self.wait(0.3)
                    group.set_color(RED)
                    self.wait(0.3)
                    group.set_color(WHITE)
                elif highlight_style == "wiggle":
                    self.play(Wiggle(group))

            if last_group and not show_previous_units:
                self.play(FadeOut(last_group), run_time=0.2)

            last_group = group

        self.wait(1)
