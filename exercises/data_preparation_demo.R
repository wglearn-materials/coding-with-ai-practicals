# Invented-only Module 2 demo: base R, no files/network, no anonymisation claim.
# Run: Rscript data_preparation_demo.R
# All values are constructed here, not sampled/fitted from real records.
invented_rows <- function() {
  data.frame(name = c("Alex Example", "Blair Example", "Casey Example",
                      "Drew Example", "Ellis Example", "Fran Example"),
             age = c(43, 31, 52, 24, 67, 89),
             group = c("A", "A", "A", "B", "B", "C"),
             score = c(2, NA_real_, 6, 10, 14, 100),
             stringsAsFactors = FALSE)
}
minimise <- function(rows) rows[c("group", "score")]
summarise <- function(rows) {
  stopifnot(is.character(rows$group), is.numeric(rows$score))
  result <- list()
  for (group in sort(unique(rows$group))) {
    values <- rows$score[rows$group == group]
    observed <- sum(!is.na(values))
    average <- if (observed == 0) NA_real_ else mean(values, na.rm = TRUE)
    result[[group]] <- c(n = length(values), observed = observed,
                         missing = sum(is.na(values)), mean = average)
  }
  result
}
main <- function() {
  before <- invented_rows()
  after <- minimise(before)
  stopifnot(identical(names(after), c("group", "score")),
            identical(summarise(before), summarise(after)),
            sum(is.na(before$score)) == sum(is.na(after$score)))
  cat("INVENTED ONLY; no privacy certification\n")
  for (label in c("before", "after")) {
    rows <- if (label == "before") before else after
    missing <- sum(is.na(rows$score))
    cat(sprintf("%s: rows=%d missing=%d numeric=%d\n", label, nrow(rows),
                missing, nrow(rows) - missing))
    summary <- summarise(rows)
    for (group in names(summary)) {
      x <- summary[[group]]
      value <- if (is.na(x[["mean"]])) "NA" else sprintf("%g", x[["mean"]])
      cat(sprintf("%s %s: n=%d observed=%d missing=%d mean=%s\n", label, group,
                  as.integer(x[["n"]]), as.integer(x[["observed"]]),
                  as.integer(x[["missing"]]), value))
    }
  }
  cat("checks: columns, types, missingness, question preserved\n")
  cat("release: NOT ASSESSED; C reveals one value\n")
}
main()
