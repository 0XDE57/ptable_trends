from ptable_trends import ptable_plotter

# row [87-118] are highjacked for custom values (so4, ph, conductivity, etc)
#

# file = "AOSTRA_KM9_median.csv"
# file = "BM11_median.csv"
# file = "Crane_Lake_median.csv"
# file = "Dragonfly_median.csv"
# file = "Ft_Mkay_1_median.csv"
# file = "Ft_Mkay_2_median.csv"
# file = "Gateway_median.csv"
# file = "HATS5_median.csv"
# file = "High_Sulfate_median.csv"
# file = "Jenny_median.csv"
# file = "Jetliner_median.csv"
# file = "JP302_median.csv"
# file = "JP311_median.csv"
# file = "Linus_median.csv"
# file = "Maqua_median.csv"
# file = "NE7_median.csv"
# file = "Pat_median.csv"
# file = "Poplar_Marsh_median.csv"
# file = "Ruth_Lake_median.csv"
# file = "La_Saline_median.csv"
# file = "Tower_median.csv"
file = "WF4_median.csv"

ptable_plotter(filename=file, extended=False, cmap="inferno")

