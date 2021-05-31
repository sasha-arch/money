import arcade
weight = 800
hight = 600

arcade.open_window(weight, hight, 'window' )
arcade.set_background_color(arcade.color.AERO_BLUE)
arcade.start_render()
arcade.draw_circle_outline(400 ,300 ,295 ,arcade.color.BLACK,5)
arcade.create_line(400, 300, 400, 295, arcade.color.BLACK, 5)
arcade.create_line(400, 300, 300, 400, arcade.color.BLACK, 5)
arcade.finish_render()
arcade.run()
