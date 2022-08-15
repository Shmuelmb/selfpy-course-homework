def arrow(my_char, max_length):
   em_list = []
   for str_search in my_char:
      yp = range(0,max_length)
      h = max_length - 1
      for range_search in yp:
         if range_search != 0:
            em_list.append(str_search*range_search)
      em_list.append(str_search*max_length)
      
      for range_search_m in yp:
         if h != max_length:
               if h > 0:
                  em_list.append(str_search*h)
                  h -=1

             
   return '\n'.join(em_list)

print(arrow("*",5))
