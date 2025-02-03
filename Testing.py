USER_NAME_X_POS = 0.178 * WINDOW_WIDTH
USER_NAME_Y_POS = 0.156 * WINDOW_HEIGHT
def display_header(self):
    """
    Display post location and description on screen

    :return:None
    """
    # display the location

    # display description

    # display the user name
    user_name_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE, bold=True)
    user_name_to_display = user_name_font.render(self.user_name,
                                                 True, GREY)
    screen.blit(user_name_to_display, (USER_NAME_X_POS, USER_NAME_Y_POS))