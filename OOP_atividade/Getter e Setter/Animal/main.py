from animal import Animal

animal = Animal(input("Digite a espécie do Animal:> "), 
(input("Digite a raça do animal:> ")),
(input("Digite o porte do animal:> ")),
(input("Digite a cor do animal:> ")))

print ('Animal da especie {}, raça {} de porte {} de cor {}'.format(animal.especie,animal.raca, animal.porte, animal.cor))


animal2 = Animal(input("Digite a espécie do segundo animal:> "),
(input("Digite a raça do animal:> ")),
(input("Digite o porte do animal:> ")),
(input("Digite a cor do animal:> ")))

print ('Segundo animal da especie{}, raça{} de porte {} de cor{}'.format(animal.especie,animal.raca, animal.porte, animal.cor))