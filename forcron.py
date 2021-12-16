import configs.db as db
import owm
import plot

a = owm.get_owm()

db.ins(a.temp, a.temp_min, a.temp_max)
plot.get_plot()
