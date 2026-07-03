def is_valid(s: str) -> bool:
  str_list = list(s)
  if len(str_list) % 2 != 0:
    return False
  return str_list.count("(")==str_list.count(")") 
  
print(is_valid("((()))"))