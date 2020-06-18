reset

input_data="kuramoto_oscilator.dat"

set terminal gif animate delay 3
set output 'kuramoto_oscilator.gif'   
set polar
set grid
set angles radi
set size 1,1; set origin 0,0
set xrange[-1.51:1.51]
set yrange[-1.51:1.51]

do for[i=1:10*100]{
  plot input_data index i ls 7 lw 1.5 notitle
}

reset

input_data="order_parameter.dat"

set terminal png
set yrange[-1:1]
set grid

plot input_data u 1:2 ls 1 lw 1.0 title "Real part"  
replot input_data u 1:3 ls 2 title "Imaginary part"
replot input_data u 1:(sqrt($2*$2+$3*$3)) ls 7 title "Mod r" 

set output "order_parameter.png"
replot

reset