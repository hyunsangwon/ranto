library(dplyr)
library(stringr)

# 예시 데이터
df <- tibble(
  name = c("KODEX ETF", "TIGER Index", "삼성전자", "ARIRANG Fund", "현대차")
)

# 여러 패턴 중 하나라도 포함된 행 필터링
patterns <- c("ETF", "Index")
pattern_regex <- paste(patterns, collapse = "|")

df = df %>%
  filter(str_detect(name, pattern_regex))

View(df)