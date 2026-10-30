# Buggy Script 1: Loading Data
# This script has TWO bugs. Use Copilot to find and fix them.
# Bug 1: Wrong file path
# Bug 2: Wrong function name

library(tidyverse)

# Load the patient survey data
# BUG 1: The file is called "patient_survey_messy.csv", not "patient_survey.csv"
survey_data <- read_csv("data/patient_survey.csv")

# Display the first few rows
# BUG 2: The function is head(), not header()
header(survey_data)

# Check the structure
glimpse(survey_data)
