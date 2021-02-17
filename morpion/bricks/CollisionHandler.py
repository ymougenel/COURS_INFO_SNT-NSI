import pygame


def process_collisions(ball, paddle, blocks):
    _collision_ball_blocks(ball, blocks)
    _collision_ball_paddle(ball, paddle)


def _collision_ball_blocks(ball, blocks):
    block_collision = pygame.sprite.spritecollideany(ball, blocks)
    if block_collision:
        blocks.remove(block_collision)
        print("Block collision")
        #TODO: note block can be hittten from bottom
        ball.collide("top")


def _collision_ball_paddle(ball, paddle):
    paddle_collision = pygame.sprite.spritecollide(ball, [paddle], False)
    if paddle_collision:
        print("Paddle Collision")
        ball.collide("bot")
