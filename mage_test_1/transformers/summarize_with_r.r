pacman::p_load(dplyr)

transform <- function(df_1, ...) {
    # Specify your transformation logic here
    # Return value: transformed dataframe.
    df_1 %>%
        group_by(Pclass) %>%
        summarize(n = n(),
                  n_survived = sum(Survived)) %>%
        mutate(perc_survived = n_survived / n)
}
