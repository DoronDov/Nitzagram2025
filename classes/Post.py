import pygame

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """

    def __init__(self, username, location, description):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []
    def add_like(self):
        self.likes_counter += 1

    def add_comment(self, text):
        self.comments.append(text)
    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        # TODO: write me!
        def display_header(self):
            """
            Display post location and description on screen

            :return:None
            """
            # display the location
            location_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE, bold=True)
            location_to_display = location_font.render(self.user_name,
                                                             True, GREY)
            screen.blit(location_to_display, (USER_NAME_X_POS, USER_NAME_Y_POS))
            # display description
            description_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE, bold=True)
            description_to_display = description_font.render(self.user_name,
                                                         True, GREY)
            screen.blit(description_to_display, (USER_NAME_X_POS, USER_NAME_Y_POS))
            # display the user name
            user_name_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE, bold=True)
            user_name_to_display = user_name_font.render(self.user_name,
                                                         True, GREY)
            screen.blit(user_name_to_display, (USER_NAME_X_POS, USER_NAME_Y_POS))
        pass


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



