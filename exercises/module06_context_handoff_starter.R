# Module 9 starter: session handoff summary scaffold (historical filename retained)

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
