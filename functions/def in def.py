
def x_dec(func):
   def func_dec_intrare():
       print("Buna ziua!")
       func()
       print("La revedere!")
   return func_dec_intrare
@x_dec
def intrebare():
   print("Salut!")
intrebare()