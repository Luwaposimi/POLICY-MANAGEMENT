library(ggplot2)
data <- read.csv("account_details.csv")
ggplot(data, aes(x = name, y = total_payments)) +
    geom_bar(stat = "identity") + # nolint
    labs(title = "Total Payments by Policyholder",
     x = "Policyholder", y = "Total Payments") # nolint