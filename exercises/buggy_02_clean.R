# Buggy Script 2: Cleaning Data
# This script has TWO bugs. Use Copilot (Inline Chat) to find and fix them.
# Bug 1: Logic error in filter (should keep ages > 18, not < 18)
# Bug 2: Missing pipe between filter and mutate

library(tidyverse)

survey_data <- read_csv("patient_survey_messy.csv")

# Clean the data: keep adults and create age groups
# BUG 1: This keeps only people UNDER 18 — should be > 18
# BUG 2: Missing |> between filter() and mutate()
cleaned_data <- survey_data |>
  filter(age < 18)
  mutate(
    age_group = case_when(
      age < 30 ~ "Young",
      age < 50 ~ "Middle",
      TRUE ~ "Senior"
    )
  )

glimpse(cleaned_data)
