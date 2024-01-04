#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int compute_score(string word);

//Letter points
int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int main(void)
{
    //Player1 word
    string word1 = get_string("Player 1: ");
    //Player2 word
    string word2 = get_string("Player 2: ");

    //Score of words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);


}

int compute_score(string word)
{
    int score = 0;

    for (int i = 0; i < strlen(word); i++)
    {
        if (isupper(word[i]))
        {
            score += points[word[i] - 'A'];
        }
        else if
        {
            
        }
    }
}
