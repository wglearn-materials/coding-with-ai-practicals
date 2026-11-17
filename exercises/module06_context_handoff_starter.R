# Module 9: optional R handoff scaffold (historical filename retained).
# This prints a list; it does not save SESSION_NOTES.md.
# The claims below are unverified. Check them against your own results and replace them.

create_handoff <- function(completed, next_steps, risks) {
  list(
    completed = completed,
    next_steps = next_steps,
    risks = risks
  )
}

handoff <- create_handoff(
  completed = c("Loaded data", "Cleaned missing values"),
  next_steps = c("Build grouped summary", "Generate plot"),
  risks = c("Missing values in treatment_group")
)

str(handoff)
