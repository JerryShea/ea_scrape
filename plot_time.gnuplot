set datafile separator ","
set terminal png size 900,400
set ylabel "kwh"
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%Y-%m-%d %H"
set xtics rotate by 90 offset 0,-7 out nomirror
set bmargin at screen 0.30
set key left top
set grid

filename="store/all.csv"
plot filename using 1:3 title 'power (kwh)' with boxes
set title "Power usage (kwh) by half hour over time"
