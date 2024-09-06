# Definiujemy funkcję create_board, która tworzy listę 9 liczb od 1 do 9
def create_board():
    # Tworzymy pustą listę o nazwie board
    board = []

    # Dla każdej liczby i od 0 do 8 (łącznie 9 liczb)
    for i in range (9):
        # Dodajemy do listy board liczbę i + 1
        board.append(i + 1)
    
    # Zwracamy listę board jako wynik funkcji
    return board

# Definiujemy funkcję show_board, która przyjmuje listę board jako argument i wyświetla ją w formie planszy do gry w kółko i krzyżyk
def show_board(board):       
    # Wyświetlamy pierwszy wiersz planszy, używając elementów listy board o indeksach 0, 1 i 2
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    # Wyświetlamy linię oddzielającą wiersze
    print("-----------")
    # Wyświetlamy drugi wiersz planszy, używając elementów listy board o indeksach 3, 4 i 5
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    # Wyświetlamy linię oddzielającą wiersze
    print("-----------")
    # Wyświetlamy trzeci wiersz planszy, używając elementów listy board o indeksach 6, 7 i 8
    print(f" {board[6]} | {board[7]} | {board[8]} ")

# Definiujemy funkcję choose_sign, która pozwala graczowi 1 wybrać swój znak ("X" lub "O") i zwraca listę dwóch znaków: pierwszy dla gracza 1, drugi dla gracza 2
def choose_sign():
    # Tworzymy pustą zmienną o nazwie sign
    sign = " "

    # Dopóki zmienna sign nie jest równa "X" lub "O"
    while not (sign == "X" or sign == "O"):
        # Pytamy gracza 1 o jego znak, używając funkcji input i zmieniając wprowadzony znak na wielką literę
        sign = input("\nGraczu 1 Wybierz swój znak (\"X\" lub \"O\"): ").upper()

        # Jeśli zmienna sign nie jest równa "X" lub "O"
        if not (sign == "X" or sign == "O"):
            # Wyświetlamy komunikat o błędnym wyborze
            print("\nZnak nie został wybrany!")

    # Jeśli zmienna sign jest równa "X"
    if sign == "X":
        # Wyświetlamy komunikat o przydzieleniu znaków dla graczy
        print("\nGracz 1 = \"X\"\nGracz 2 = \"O\"")

        # Zwracamy listę ["X", "O"] jako wynik funkcji
        return ["X", "O"]
    # W przeciwnym razie, czyli jeśli zmienna sign jest równa "O"
    else:
        # Wyświetlamy komunikat o przydzieleniu znaków dla graczy
        print("\nGracz 1 = \"O\"\nGracz 2 = \"X\"")

        # Zwracamy listę ["O", "X"] jako wynik funkcji
        return ["O", "X"]
    
# Definiujemy funkcję who_starts, która pozwala wybrać, który gracz ma zacząć pierwszy ruch
def who_starts():
    # Tworzymy pustą zmienną o nazwie choose
    choose = " "

    # Dopóki zmienna choose nie jest równa "1" lub "2"
    while not (choose == "1" or choose == "2"):
        # Pytamy gracza, który ma zacząć pierwszy ruch, używając funkcji input
        choose = input("\nKtóry gracz ma zacząć pierwszy ruch (\"1\" czy \"2\"): ")

        # Jeśli zmienna choose nie jest równa "1" lub "2"
        if not (choose == "1" or choose == "2"):
            # Wyświetlamy komunikat o błędnym wyborze
            print("\nGracz nie został wybrany!")

    # Jeśli zmienna choose jest równa "1"
    if choose == "1":
        # Wyświetlamy komunikat o pierwszym ruchu gracza 1
        print("\nPierwszy ruch wykonuje gracz 1")

        # Zwracamy napis "Gracz 1" jako wynik funkcji
        return "Gracz 1"
    # W przeciwnym razie, czyli jeśli zmienna choose jest równa "2"
    else:
        # Wyświetlamy komunikat o pierwszym ruchu gracza 2
        print("\nPierwszy ruch wykonuje gracz 2")

        # Zwracamy napis "Gracz 2" jako wynik funkcji
        return "Gracz 2"

# Definiujemy funkcję can_place_sign, która przyjmuje listę board i liczbę position jako argumenty i sprawdza, czy można umieścić znak na danej pozycji na planszy
def can_place_sign(board, position):
    # Zwracamy wartość logiczną, czy element listy board o indeksie position jest liczbą z zakresu od 1 do 9
    return board[position] in range (1,10)

# Definiujemy funkcję place_sign, która przyjmuje listę board, napis sign i liczbę position jako argumenty i umieszcza znak na danej pozycji na planszy
def place_sign(board, sign, position):
    # Przypisujemy elementowi listy board o indeksie position wartość napisu sign
    board[position] = sign

# Definiujemy funkcję check_win, która przyjmuje listę board i napis sign jako argumenty i sprawdza, czy gracz o danym znaku wygrał grę
def check_win(board, sign):
    # Zwracamy wartość logiczną, czy spełniony jest któryś z warunków wygranej, czyli czy na planszy jest trzy razy ten sam znak w jednym z wierszy, kolumn lub przekątnych
    return ((board[0] == sign and board[1] == sign and board[2] == sign) or
            (board[3] == sign and board[4] == sign and board[5] == sign) or
            (board[6] == sign and board[7] == sign and board[8] == sign) or
            (board[0] == sign and board[3] == sign and board[6] == sign) or
            (board[1] == sign and board[4] == sign and board[7] == sign) or
            (board[2] == sign and board[5] == sign and board[8] == sign) or
            (board[0] == sign and board[4] == sign and board[8] == sign) or
            (board[2] == sign and board[4] == sign and board[6] == sign))

# Definiujemy funkcję check_draw, która przyjmuje listę board jako argument i sprawdza, czy gra zakończyła się remisem
def check_draw(board):
    # Dla każdej liczby i od 0 do 8 (łącznie 9 liczb)
    for i in range(9):
        # Jeśli można umieścić znak na pozycji i na planszy
        if can_place_sign(board, i):
            # Zwracamy wartość logiczną False, czyli że gra nie jest remisem
            return False
        
    # Jeśli pętla się zakończyła, to znaczy, że nie można umieścić znaku na żadnej pozycji na planszy
    # Zwracamy wartość logiczną True, czyli że gra jest remisem
    return True

# Definiujemy funkcję choose_position, która przyjmuje listę board, napis current_player, napis player1_sign i napis player2_sign jako argumenty i zwraca liczbę oznaczającą pozycję na planszy, na której gracz chce umieścić swój znak
def choose_position(board,current_player,player1_sign,player2_sign):
    # Tworzymy zmienną o nazwie position i przypisujemy jej wartość 0
    position = 0
    
    # Dopóki zmienna position nie jest liczbą z zakresu od 1 do 9 lub nie można umieścić znaku na pozycji position - 1 na planszy
    while position not in range (1,10) or not can_place_sign(board, position - 1):
        # Jeśli zmienna current_player jest równa "Gracz 1"
        if current_player == "Gracz 1":
            # Próbujemy wykonać następujący blok kodu
            try:
                # Pytamy gracza 1 o jego pozycję, używając funkcji input i zmieniając wprowadzony znak na liczbę całkowitą
                position = int(input(f"Graczu 1 ({player1_sign}), Wybierz pozycje (1-9): "))
            # Jeśli wystąpi błąd ValueError, czyli gdy wprowadzony znak nie jest liczbą
            except ValueError:
                # Kontynuujemy pętlę while, ignorując błąd
                continue
        # W przeciwnym razie, czyli jeśli zmienna current_player jest równa "Gracz 2"
        else:
            # Próbujemy wykonać następujący blok kodu
            try:
                # Pytamy gracza 2 o jego pozycję, używając funkcji input i zmieniając wprowadzony znak na liczbę całkowitą
                position = int(input(f"Graczu 2 ({player2_sign}), Wybierz pozycje (1-9): "))
            # Jeśli wystąpi błąd ValueError, czyli gdy wprowadzony znak nie jest liczbą
            except ValueError:
                # Kontynuujemy pętlę while, ignorując błąd
                continue

    # Zwracamy zmienną position pomniejszoną o 1 jako wynik funkcji
    return position - 1


# Wyświetlamy napis "Witaj w grze kółko i krzyżyk!"
print("Witaj w grze kółko i krzyżyk!")
# Tworzymy pętlę nieskończoną, która będzie się powtarzać, dopóki gracz nie zdecyduje się zakończyć gry
while True:
    # Tworzymy listę board, używając funkcji create_board, która tworzy listę 9 liczb od 1 do 9
    board = create_board()
    # Tworzymy dwie zmienne player1_sign i player2_sign, używając funkcji choose_sign, która pozwala graczowi 1 wybrać swój znak ("X" lub "O") i zwraca listę dwóch znaków: pierwszy dla gracza 1, drugi dla gracza 2
    player1_sign, player2_sign = choose_sign()
    # Tworzymy zmienną current_player, używając funkcji who_starts, która pozwala wybrać, który gracz ma zacząć pierwszy ruch i zwraca napis "Gracz 1" lub "Gracz 2"
    current_player = who_starts()
    # Tworzymy zmienną game_on i przypisujemy jej wartość logiczną True, oznaczającą, że gra jest w trakcie
    game_on = True

    # Dopóki zmienna game_on jest równa True
    while game_on:
        # Wyświetlamy pustą linię
        print()
        # Wyświetlamy listę board w formie planszy do gry, używając funkcji show_board, która przyjmuje listę board jako argument i wyświetla ją w formie planszy do gry w kółko i krzyżyk
        show_board(board)
        # Wyświetlamy pustą linię
        print()
        # Tworzymy zmienną current_position i przypisujemy jej wartość zwróconą przez funkcję choose_position, która przyjmuje listę board, napis current_player, napis player1_sign i napis player2_sign jako argumenty i zwraca liczbę oznaczającą pozycję na planszy, na której gracz chce umieścić swój znak
        current_position = choose_position(board,current_player,player1_sign,player2_sign)
        
        # Jeśli zmienna current_player jest równa "Gracz 1"
        if current_player == "Gracz 1":
            # Umieszczamy znak gracza 1 na pozycji current_position na planszy, używając funkcji place_sign, która przyjmuje listę board, napis sign i liczbę position jako argumenty i umieszcza znak na danej pozycji na planszy
            place_sign(board, player1_sign, current_position)
        # W przeciwnym razie, czyli jeśli zmienna current_player jest równa "Gracz 2"
        else:
            # Umieszczamy znak gracza 2 na pozycji current_position na planszy, używając funkcji place_sign, która przyjmuje listę board, napis sign i liczbę position jako argumenty i umieszcza znak na danej pozycji na planszy
            place_sign(board, player2_sign, current_position)

        # Jeśli funkcja check_win, która przyjmuje listę board i napis sign jako argumenty i sprawdza, czy gracz o danym znaku wygrał grę, zwraca wartość logiczną True dla znaku gracza 1
        if check_win(board, player1_sign):
            # Wyświetlamy pustą linię
            print()
            # Wyświetlamy listę board w formie planszy do gry, używając funkcji show_board
            show_board(board)
            # Wyświetlamy napis z gratulacjami dla gracza 1
            print(f"\nGratulacje, Graczu 1 ({player1_sign})! Wygrałeś grę!")
            # Przypisujemy zmiennej game_on wartość logiczną False, oznaczającą, że gra się zakończyła
            game_on = False
        # W przeciwnym razie, jeśli funkcja check_win, która przyjmuje listę board i napis sign jako argumenty i sprawdza, czy gracz o danym znaku wygrał grę, zwraca wartość logiczną True dla znaku gracza 2
        elif check_win(board, player2_sign):
            # Wyświetlamy pustą linię
            print()
            # Wyświetlamy listę board w formie planszy do gry, używając funkcji show_board
            show_board(board)
            # Wyświetlamy napis z gratulacjami dla gracza 2
            print(f"\nGratulacje, Graczu 2 ({player2_sign})! Wygrałeś grę!")
            # Przypisujemy zmiennej game_on wartość logiczną False, oznaczającą, że gra się zakończyła
            game_on = False
        # W przeciwnym razie, jeśli funkcja check_draw, która przyjmuje listę board jako argument i sprawdza, czy gra zakończyła się remisem, zwraca wartość logiczną True
        elif check_draw(board):
            # Wyświetlamy pustą linię
            print()
            # Wyświetlamy listę board w formie planszy do gry, używając funkcji show_board
            show_board(board)
            # Wyświetlamy napis o remisie
            print("\nGra zakończyła się remisem!")
            # Przypisujemy zmiennej game_on wartość logiczną False, oznaczającą, że gra się zakończyła
            game_on = False
        # W przeciwnym razie, czyli jeśli gra jest nadal w trakcie
        else:
            if current_player == "Gracz 1":
                current_player = "Gracz 2" 
            else: 
                current_player = "Gracz 1"

    play_again = input("\nCzy chcesz zagrać ponownie? (Jesli tak Napisz: \"t\" ): ").lower()
    if play_again != 't':
        break