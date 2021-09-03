from . models import *
from . views import *

def count(request): 
   #user logout      if req.user_is_authenticated
   item_count = 0

   if 'admin' in request.path:
      return{}
   else:
      try:
         ct = cartList.objects.filter(cart_id=crt_id(request))    #here also changed cart_id=crt_id(request)
         ct_items = itemsCart.objects.all().filter(cart=ct[:1])

         for i in ct_items:
            item_count += i.qty
      except cartList.DoesNotExist:
         item_count = 0
      return dict(itc=item_count) 


   #return{} ---> this is for above if condt.