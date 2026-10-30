# Buggy Script 3: Summarizing Data
# This script produces NA results. Use /explain then fix it.
# Bug: mean() returns NA when there are NA values — need na.rm = TRUE

library(tidyverse)

survey_data <- read_csv("patient_survey_messy.csv")

# Summarize satisfaction by treatment group
# BUG: This will return NA because satisfaction_score has missing values
summary_stats <- survey_data |>
  group_by(treatment_group) |>
  summarize(
    avg_satisfaction = mean(satisfaction_score),
    min_satisfaction = min(satisfaction_score),
    max_satisfaction = max(satisfaction_score),
    n_patients = n()
  )

print(summary_stats)
