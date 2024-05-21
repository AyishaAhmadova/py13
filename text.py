def sirala_ve_yerleri_tap(xallar):
    
    xallar_ve_indeksler = [(xallar[i], i) for i in range(len(xallar))]
    
  
    xallar_ve_indeksler.sort(reverse=True, key=lambda x: x[0])
    
    yerlər = [0] * len(xallar)
    for sira, (_, indeks) in enumerate(xallar_ve_indeksler):
        yerlər[indeks] = f"{sira + 1}-ci"
    
    return yerlər


xallar = [5, 3, 4, 2, 1]
yerlər = sirala_ve_yerleri_tap(xallar)
print(yerlər)