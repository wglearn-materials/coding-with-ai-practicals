# Module 7 starter: implementation pipeline (historical filename retained)

load_invented_survey <- function(path) {
  survey <- read.csv(path, colClasses = "character", na.strings = character(),
                     check.names = FALSE)
  required <- c("treatment_group", "satisfaction_score")
  if (!all(required %in% names(survey))) stop("Missing required survey columns")
  scores <- trimws(survey$satisfaction_score)
  missing <- scores == ""
  numeric_scores <- suppressWarnings(as.numeric(scores))
  invalid <- !missing & (!grepl("^[0-9]+$", scores) | is.na(numeric_scores) |
                         numeric_scores < 1 | numeric_scores > 10)
  if (any(invalid)) stop(paste("Invalid score at CSV row", which(invalid)[1] + 1))
  survey$satisfaction_score <- as.integer(numeric_scores)
  survey$treatment_group <- trimws(survey$treatment_group)
  survey$treatment_group[survey$treatment_group == ""] <- "(missing group)"
  survey
}

survey <- load_invented_survey("patient_survey_messy.csv")
groups <- split(survey$satisfaction_score, survey$treatment_group)
summary_tbl <- do.call(rbind, lapply(names(groups), function(group) {
  scores <- groups[[group]]
  data.frame(treatment_group = group,
             mean_satisfaction = mean(scores, na.rm = TRUE), n = length(scores))
}))

print(summary_tbl)
