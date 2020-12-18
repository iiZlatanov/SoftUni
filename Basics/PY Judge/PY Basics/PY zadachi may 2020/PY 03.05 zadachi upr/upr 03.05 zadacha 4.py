#212 / 20 / 2  izhod 5.3
broi_stranici = int(input())
stranici_koito_moje_da_prochete_za_chas = int(input())
broi_na_dnite_nujni_da_se_prochete_knigata = int(input())
#Да се отпечата на конзолата броят часове, които Жоро трябва да отделя за четене всеки ден.
jore_jore = broi_stranici / stranici_koito_moje_da_prochete_za_chas
jore = jore_jore / broi_na_dnite_nujni_da_se_prochete_knigata
print(jore)