import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from typing import List


def load_data():
    filepath = "dane.txt"
    f = open(filepath, "r", encoding="utf-8")
    lst = f.read()
    lst = lst.splitlines(keepends=False)
    data_base = []
    for line in lst:
        if line != '':
            data_base.append(line.split())
            f.close()
        else:
            f.close()
    return data_base


def data_unpack():
    data_base = load_data()
    daty = []
    value = []
    for line in data_base:
        for i in line:
            daty.append(i.split(",", 1)[0])
            wart = i.split(",", 1)[1]
            lst_temp = []
            for temp in wart.split(","):
                lst_temp.append(float(temp))
            value.append(lst_temp)
    return daty, value


def min_max_value():
    min_val = []
    max_val = []
    rok, wartosci = data_unpack()
    maxval = max([max([i for i in z]) for z in wartosci])
    minval = min([min([i for i in z]) for z in wartosci])

    for year, temp in enumerate(wartosci, start=1951):
        for counter, value in enumerate(temp, start=1):
            if value == minval:
                temp = f'{year}, {counter}, {value}'
                min_val.append(temp)
            if value == maxval:
                temp = f'{year}, {counter}, {value}'
                max_val.append(temp)
    return min_val, max_val


def average_temp_in_year():
    rok, wart = data_unpack()
    dct = {}
    for year, temp in enumerate(wart, start=1951):
        suma = 0
        for i in temp:
            suma += i
        srednia = suma / len(temp)
        dct[year] = round(srednia, 2)
    return dct


def plot_average_temp():
    dct = average_temp_in_year()
    years = []
    temp = []
    for year, aver_temp in dct.items():
        years.append(year)
        temp.append(aver_temp)

    x = np.arange(len(years))
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)

    ax.set_ylabel('Temperatura ($^\circ$C)')
    ax.set_title("Średnia temperatura w danym roku")
    ax.set_xticks(x)
    ax.set_xticklabels(years)

    plt.xticks(
        rotation=90,
        horizontalalignment='right',
        fontsize=9
    )
    plt.yticks(np.arange(0, 13, 0.25))

    ax.bar(x, temp)
    fig.tight_layout()
    plt.show()


def odch_standard(miesiac) -> float:
    srednia = sum(miesiac) / len(miesiac)
    x = 0
    for i in miesiac:
        x += i ** 2
    A_prim = x / len(miesiac)
    odchylenie = np.sqrt(A_prim - srednia ** 2)
    return round(odchylenie, 2)


def average_temp_through_years():
    years, values = data_unpack()
    styczen = []
    luty = []
    marzec = []
    kwiecien = []
    maj = []
    czerwiec = []
    lipiec = []
    sierpien = []
    wrzesien = []
    pazdziernik = []
    listopad = []
    grudzien = []
    miesiace = [styczen, luty, marzec, kwiecien, maj, czerwiec, lipiec, sierpien, wrzesien, pazdziernik, listopad,
                grudzien]
    for year, temp in enumerate(values, start=1951):
        for month, value in enumerate(temp, start=1):
            for i in range(len(miesiace)):
                if month == i + 1:
                    miesiace[i].append(value)
    srednia = []  # Średnia temperatura dla poszczególnych miesięcy
    stds = []  # Odchylenie standardowe temperatury dla poszczególnych miesięcy
    for i in range(12):
        sr = sum(miesiace[i]) / len(miesiace[i])
        odch = odch_standard(miesiace[i])
        stds.append(odch)
        srednia.append(round(sr, 3))

    return srednia, stds


def plot_average_temp_through_years():
    sr, odch = average_temp_through_years()
    miechy = ["sty", "lut", "mar", "kwi", "maj", "cze", "lip", "sie", "wrz",
              "paz", "lis", "gru"]

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.set_xlabel("Miesiąc", fontsize=18)
    ax.set_ylabel('Temperatura ($^\circ$C)', fontsize=18)
    xaxis = [i + 1 for i in range(0, 12)]

    color_temperature = "red"
    lineStyle = {"linestyle": "--", "linewidth": 2, "markeredgewidth": 2, "elinewidth": 2, "capsize": 3}

    # create an error bar for each dataset
    line_Temperature = ax.errorbar(xaxis, sr, yerr=odch, **lineStyle, color=color_temperature,
                                   label='Month_Temperature')

    for i, txt in enumerate(sr):
        ax.annotate(txt, xy=(xaxis[i], sr[i]), xytext=(xaxis[i] + 0.03, sr[i] + 0.3), color=color_temperature)

    plt.xticks(xaxis, miechy)
    plt.yticks(np.arange(-10, 25, 2))

    params = {'legend.fontsize': 13,
              'legend.handlelength': 2}
    plt.rcParams.update(params)

    # Customize the font
    font = {'family': 'Arial',
            'weight': 'bold',
            'size': 12}
    matplotlib.rc('font', **font)

    ax.grid(color='lightgrey', linestyle='-')
    ax.set_facecolor('w')

    plt.title("Sr. temp. z poszczegolnych miesięcy na przestrzenie lat z odchyleniem standardowym")

    plt.show()

