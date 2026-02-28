def extract_feature(text: str) -> dict:
  text_split = text.lower().split()
  word_count = len(text_split)
  char_count = len(text)
  contains_free = 0
  contains_win = 0
  contains_click = 0
  contains_offer = 0
  uppercase_ratio = 0
  
  contains_free = 1 if "free" in text_split else 0
  contains_win = 1 if "win" in text_split else 0
  contains_click = 1 if "click" in text_split else 0
  contains_offer = 1 if "offer" in text_split else 0
  
  for i in text:
    if i.isupper() is True:
      uppercase_ratio += 1
  
  # print(word_count, 
  #       char_count, 
  #       contains_free, 
  #       contains_win, 
  #       contains_click, 
  #       contains_offer, 
  #       uppercase_ratio
  #       )
  return {
    "Word count": word_count,
    "Char count": char_count,
    "Contains free": contains_free,
    "Contains win": contains_win,
    "Contains click": contains_click,
    "Contains offer": contains_offer,
    "Uppercase ratio": round(uppercase_ratio / char_count, 2)
    }
  
