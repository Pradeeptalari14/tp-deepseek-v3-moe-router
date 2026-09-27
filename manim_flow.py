from manim import *

class DeepSeekV3MoEScene(Scene):
    def construct(self):
        title = Text("DeepSeek-V3: 256-Expert MoE & DualPipe Overlap", font_size=32, color=VIOLET).to_edge(UP)
        self.play(Write(title))

        token_box = Rectangle(height=0.8, width=2.4, color=CYAN, fill_opacity=0.6).shift(LEFT * 4)
        t_label = Text("Token Embedding", font_size=18).move_to(token_box)
        self.play(Create(token_box), Write(t_label))

        router = Rectangle(height=1.4, width=2.2, color=GOLD, fill_opacity=0.7).shift(LEFT * 1)
        r_label = Text("Top-K Router\n(K=8 of 256)", font_size=16, color=BLACK).move_to(router)
        arr_in = Arrow(token_box.get_right(), router.get_left(), buff=0.1, color=WHITE)
        self.play(GrowArrow(arr_in), Create(router), Write(r_label))

        e_group = VGroup()
        for i in range(4):
            e_box = Rectangle(height=0.45, width=1.8, color=GREEN, fill_opacity=0.6).shift(RIGHT * 3 + UP * (1.2 - i*0.8))
            e_lbl = Text(f"Expert {i*64+1}", font_size=14).move_to(e_box)
            e_group.add(VGroup(e_box, e_lbl))
            
        self.play(Create(e_group))

        bot_box = Rectangle(height=0.8, width=7.5, color=BLUE).to_edge(DOWN)
        bot_txt = Text("DualPipe: Bidirectional Overlap | All-to-All Comm Bubble < 5%", font_size=16, color=BLUE).move_to(bot_box)
        self.play(Create(bot_box), Write(bot_txt))
        self.wait(2)
