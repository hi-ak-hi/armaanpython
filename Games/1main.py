while True:
    print("what game do you want to play(enter 1-5, or exit to exit)---")
    game = input("1. connect_four\n2. guessing_game\n3. rock_paper_siccors\n4. roll_a_die\n5. tic_tac_toe\n>>> ")
    game = game.lower()
    if game == "1":
        import connect_four
    if game == "2":
        import guessing_game
    if game == "3":
        import rock_paper_siccors
    if game == "4":
        import roll_a_die
    if game == "5":
        import tic_tac_toe
    if game == "exit":
        break
print("thank you for playing my games")