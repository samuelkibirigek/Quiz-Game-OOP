from quiz_brain import Quiz

brain = Quiz()

while brain.game_is_on:
    brain.question()
    brain.check_answer()
    brain.play_game()


