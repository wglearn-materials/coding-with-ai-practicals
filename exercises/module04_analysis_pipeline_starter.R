# Module 7 starter: implementation pipeline (historical filename retained)

library(dplyr)

survey <- read.csv("patient_survey_messy.csv")

summary_tbl <- survey |>
  group_by(treatment_group) |>
  summarize(
    mean_satisfaction = mean(satisfaction_score, na.rm = TRUE),
    n = n(),
    .groups = "drop"
  )

print(summary_tbl)
