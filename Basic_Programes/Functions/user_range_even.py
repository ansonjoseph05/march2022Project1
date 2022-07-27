def even_range(initial,final):
    while final>=initial:
        if final%2==0:
            print(final)
        final-=1
initial=int(input("Enter initial value : "))
final=int(input("Enter final value : "))
even_range(initial,final)
