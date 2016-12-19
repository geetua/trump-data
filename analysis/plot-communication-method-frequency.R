library("tidyverse")
library("lubridate")

# Prepare: ./analysis/csv-communication-method-frequency.py data/2016_donald-trump/ > /tmp/trump.csv
#data <- read_csv("/tmp/trump.csv")
data <- read_csv("/tmp/clinton.csv")

data %>% 
  filter(date >= ymd("2015-01-01")) %>%
  mutate(week = round_date(date, unit = "week"), month = round_date(date, unit = "month")) %>% 
  group_by(month, method) %>%
  count() %>%
  ggplot() +
  geom_bar(mapping = aes(x = month, y = n, fill = method), stat = "identity") +
  labs(x = "Month", y = "Frequency") +
  xlim(ymd("2015-01-01"), ymd("2017-01-01")) +
  geom_vline(xintercept = as.numeric(ymd("2016-11-08")), linetype=2) +
  annotate("text", x = ymd("2016-11-08"), y = -1, label = "Election") +
  geom_vline(xintercept = as.numeric(ymd("2016-07-21")), linetype=2) +
  #annotate("text", x = ymd("2016-07-21"), y = -1, label = "Nomination")
  annotate("text", x = ymd("2016-07-26"), y = -1, label = "Nomination")
