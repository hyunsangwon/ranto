library(dplyr)
library(stringr)

print(file.exists("ranto.csv")) 

ranto = read.csv('ranto.csv')

patterns = c("일본", "종합상사", "오사카", "엔화", "춘투")
japan_pattern_regex = paste(patterns, collapse = "|")
patterns = c("미국국채", "장단기", "재무부")
dollor_pattern_regex = paste(patterns, collapse = "|")
patterns = c("금양", "그회사")
the_pattern_regex = paste(patterns, collapse = "|")
patterns = c("시진핑", "중국", "태무")
china_pattern_regex = paste(patterns, collapse = "|")
patterns = c("트럼프", "바이든", "미중" , "관세")
usa_pattern_regex = paste(patterns, collapse = "|")

ranto = ranto %>%
  mutate(category = ifelse(str_detect(title, '포트폴리오'), '포트폴리오'
                           ,ifelse(str_detect(title, japan_pattern_regex), '일본'
                                   ,ifelse(str_detect(title, dollor_pattern_regex), '국채'
                                           ,ifelse(str_detect(title, '조선업'), '조선'
                                                   ,ifelse(str_detect(title, 'VIX'), 'VIX'
                                                           ,ifelse(str_detect(title, '브라질'), '브라질'
                                                                   ,ifelse(str_detect(title, '희토류'), '희토류',
                                                                           ifelse(str_detect(title, the_pattern_regex), '그회사'
                                                                                  ,ifelse(str_detect(title, 'ETF'), 'ETF'
                                                                                          ,ifelse(str_detect(title, china_pattern_regex), '중국'
                                                                                                  ,ifelse(str_detect(title, usa_pattern_regex), '미국','')))
                                                                                  )
                                                                           )
                                                           )
                                                   )
                                           )
                                   ) 
                           )
         ))
  

write.csv(ranto, file = "ranto.csv", row.names = FALSE, fileEncoding = "cp949")

