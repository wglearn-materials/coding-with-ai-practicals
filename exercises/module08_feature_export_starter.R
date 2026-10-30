# Module 11 starter: export feature scaffold (historical filename retained)

export_summary <- function(data, out_csv = "summary_export.csv") {
  write.csv(data, out_csv, row.names = FALSE)
  message("Exported summary to ", out_csv)
}

# TODO: create data frame named summary_tbl, then call export_summary(summary_tbl)
