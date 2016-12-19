data <- read_csv("~/Desktop/word-freq.csv")

# Raw
data %>% 
  group_by(letters, candidate) %>%
  summarize(total = sum(count)) %>%
  ggplot() +
  geom_bar(mapping = aes(x = letters, y = total, fill = candidate), stat = "identity") +
  labs(x = "Letters", y = "Frequency")

# Weighted
data %>% 
  group_by(letters, candidate) %>%
  summarize(total = sum(weighted)) %>%
  ggplot() +
  geom_bar(mapping = aes(x = letters, y = total, fill = candidate), stat = "identity", position = "dodge") +
  labs(x = "Letters", y = "Density")
