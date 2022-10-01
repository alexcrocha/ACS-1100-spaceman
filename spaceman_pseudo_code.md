# Spaceman Pseudo Code

FUNCTION load_word:
> READ words.txt
>
> GET list of words
>
> INITIALIZE secret_word as random word FROM list of words
>
> RETURNS secret_word
>
ENDFUNCTION

FUNCTION is_word_guessed with PARAMS secret_word, letters_guessed:
> LOOP through all letters IN secret_word
> > IF letter FROM secret_word is NOT IN letters_guessed:
> > > RETURNS False AND ENDFUNCTION
> >
> > ENDIF
>
> ENDLOOP
>
> RETURNS True
>
ENDFUNCTION

FUNCTION get_guessed_word with PARAMS secret_word, letters_guessed:
> INITIALIZE string with empty value
>
> LOOP through all letters in secret_word
> > IF letter is IN letters_guessed:
> > > ADD letter to string
> >
> > ELSE letter is NOT IN letters_guessed:
> > > ADD underscore to string
> >
> > ENDIF
>
> ENDLOOP
>
> RETURNS string
>
ENDFUNCTION

FUNCTION is_guess_in_word with PARAMS guess, secret_word:
> IF guess is IN secret_word:
> > RETURNS True AND ENDFUNCTION
> >
> ELSE guess is NOT IN secret_word:
> > RETURNS False
>
> ENDIF
>
ENDFUNCTION

FUNCTION spaceman with PARAMS secret_word:
> DISPLAY information about the game
>
> INITIALIZE game_over to False
>
> WHILE game_over is False DO:
> > INITIALIZE guess to False
> >
> > WHILE guess is NOT one letter DO:
> > > PROMPT for player to guess one letter
> > >
> > > GET guess
> >
> > ENDLOOP
> >
> > CALL is_guess_in_word with ARGS guess, secret_word
> >
> > GET returned value
> >
> > IF returned value is False:
> > > DISPLAY "You're out of luck..."
> > >
> > ELSE returned value is TRUE:
> > > DISPLAY "You got it!"
> >
> > ENDIF
> >
> > CALL get_guessed_word with ARGS secret_word, letters_guessed
> >
> > GET returned string guessed_word
> >
> > DISPLAY guessed_word
> >
> > CALL is_word_guessed with ARGS secret_word, letters_guessed
> >
> > GET returned value
> >
> > IF returned value is True:
> > > REASSIGN game_over to True
> >
> > ENDIF
>
> ENDLOOP
>
ENDFUNCTION

CALL load_word

GET secret_word

CALL spaceman with ARGS secret_word

DISPLAY "GAME OVER"
