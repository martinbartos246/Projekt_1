zamestnanci ['František', 'Bruno',
    'Anna', 'Jakub',
    'Klára', 'Anežka',
    'Anežka', 'Anežka']
    posledni_index = zamestnanci.index('Anežka', -1)
    print("Na indexu 2 je:", zamestnanci[2])
    print("Na {} indexu je: {}".format(posledni_index, zamestnanci[posledni_index]))
    jména_v_intervalu = ", ".join(zamestnanci[2:5])
print("V intervalu od 2 do 5 je:", jména_v_intervalu)
kazdy_treti = zamestnanci[::3]
print("Každý třetí člen je:", ", ".join(kazdy_treti))