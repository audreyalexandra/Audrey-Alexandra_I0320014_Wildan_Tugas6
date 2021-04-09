ulang = 24
for bil in range (10,ulang+1):
    if bil > 1:
        for j in range(2,bil):
            if(bil % j) == 0:
                print(bil,"Bukan Bilangan Prima")
                break
        else:
            print(bil,"Adalah Bilangan Prima")