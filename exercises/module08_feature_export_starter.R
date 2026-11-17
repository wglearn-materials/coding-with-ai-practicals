# Module 11: optional, incomplete export scaffold (historical filename retained).
# Before calling it, add outputs/ path checks, no-overwrite behavior and HTML export.
# Running this file unchanged defines a function but exports nothing.

export_summary <- function(data, out_csv = "summary_export.csv") {
  write.csv(data, out_csv, row.names = FALSE)
  message("Exported summary to ", out_csv)
}

# TODO: create data frame named summary_tbl, then call export_summary(summary_tbl)
