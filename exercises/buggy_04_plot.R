# Buggy Script 4: Plotting Data
# This script has a ggplot2 error. Use rubber duck debugging with Copilot.
# Bug: geom_bar with a y aesthetic needs stat = "identity" or use geom_col

library(tidyverse)

survey_data <- read_csv("patient_survey_messy.csv")

# Calculate average satisfaction by treatment group
summary_data <- survey_data |>
  group_by(treatment_group) |>
  summarize(
    avg_satisfaction = mean(satisfaction_score, na.rm = TRUE),
    .groups = "drop"
  )

# Create a bar chart
# BUG: geom_bar() with a y aesthetic needs stat = "identity"
# or you should use geom_col() instead
ggplot(summary_data, aes(x = treatment_group, y = avg_satisfaction)) +
  geom_bar(fill = "#4f46e5") +
  labs(
    title = "Average Satisfaction by Treatment Group",
    x = "Treatment Group",
    y = "Average Satisfaction Score"
  ) +
  theme_minimal()
