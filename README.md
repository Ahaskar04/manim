# 🎞️ Manim Custom Animation: `interpolate_mobject`, `alpha`, and `add_updater()`

This README explains how to build custom animations in [Manim](https://docs.manim.community/) by subclassing the `Animation` class. Specifically, it covers:

- What `interpolate_mobject(alpha)` does
- How `alpha` controls animation progress
- How `add_updater()` is used to dynamically update mobjects on each frame

---

## 🔁 `interpolate_mobject(alpha)`

This is the **core function** of any custom Manim animation.

### ✅ What it does:

Manim automatically calls this method **once per frame** while the animation is running. You use it to update your mobject based on the animation progress.

### ✅ The `alpha` parameter:

- `alpha` is a float value that ranges from **0 to 1**
- `alpha = 0` → animation just started
- `alpha = 0.5` → halfway through
- `alpha = 1` → animation complete

You use `alpha` to interpolate (i.e., calculate values between start and end states).

---

### 📈 Example: Counting Up from 0 to 100

```python
class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs):
        super().__init__(number, **kwargs)
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float):
        value = self.start + alpha * (self.end - self.start)
        self.mobject.set_value(value)
```

````

This will make a `DecimalNumber` gradually increase from `start` to `end` over the course of the animation.

---

## ⚙️ `add_updater()` – Live Frame-by-Frame Updates

The `add_updater()` method attaches a **live function** to a mobject that runs on every frame, not just during animations.

### ✅ Use cases:

- Keep a number or shape centered as it changes
- Dynamically update position, rotation, color, etc.
- Apply physics-like motion (e.g., gravity, bouncing)

### 📌 Example:

```python
number = DecimalNumber().set_color(WHITE).scale(5)
number.add_updater(lambda m: m.move_to(ORIGIN))
```

Even when the number grows in size (e.g., from 0 to 100), this updater keeps it **centered** on the screen.

---

## 🎬 Full Example

```python
class CountingScene(Scene):
    def construct(self):
        number = DecimalNumber().set_color(WHITE).scale(5)
        number.add_updater(lambda m: m.move_to(ORIGIN))
        self.add(number)

        self.play(Count(number, 0, 100), run_time=4, rate_func=linear)
        self.wait()
```

- This scene displays a large number.
- The number **counts from 0 to 100** smoothly.
- It's always **centered**, even as the number of digits grows.

---

## 📚 Summary

| Concept                 | Purpose                                                            |
| ----------------------- | ------------------------------------------------------------------ |
| `interpolate_mobject()` | Core method for defining custom animations                         |
| `alpha`                 | Progress variable from 0 (start) to 1 (end)                        |
| `add_updater()`         | Real-time logic that runs every frame (not just during animations) |

---

## 🛠️ Tips

- You can animate **any mobject**: numbers, shapes, groups, graphs, etc.
- You can mix `play(...)`, `.animate`, `add_updater()`, and `interpolate_mobject()` for complex behaviors.
- Use `rate_func=linear` for smooth transitions, or try `there_and_back`, `smooth`, etc. for interesting easing.

````
