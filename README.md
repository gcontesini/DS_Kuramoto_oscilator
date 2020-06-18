# Model de Kuramoto

## Modelo Matemático

O oscilador de Kuramoto é um modelo matemático que explica a o fenômeno de sincronização de $N$ oscilador inicialmente dessincronizados. Inicialmente dada oscilador $i=1,2,\dots,N$ possui uma frequência natural de oscilação própria $\omega_i$. Adicionalmente cada oscilador possui um termo de acoplamento $f(\theta_i,\theta_j)$ que depende da fase dos demais osciladores. A evolução dos osciladores é dada pela seguinte equação,

$\frac{d}{dt}\theta_i = \omega_i  +\frac{K}{N}\sum^{N}_{j=1}sin(\theta_i-\theta_j)$

## Parâmetro de Ordem

A interação é interpretada como pelo parâmetro de ordem do sistema. Este parâmetro mede diretamente o grau de sincronização  do sistema. O parâmetro de ordem é dado pelo Kernel de 


$re^{i\theta}=∑^{N}_{j=0}e^{iθj}$

Para duas condições $\theta=\theta_{j}$ e $\theta=\frac{2\pi}{N}(j-1)$ obtemos soluções estacionarias distintas.

Dirichlet Kernel

Observamos que o plote do parâmetro de ordem em coordenadas polares. Interpretando o parâmetro de ordem como um análogo ao centro de massa do sistema, observamos que o sistema sob estas destas duas condições representa a duas situações no qual o centro de massa do sistema permanece estacionário.

## Ruido

In order to observe the decay of a perturbation, we allow the creation of a perturbation towards a given angle with a given strength. For this we change the phase angle of every oscillator asθ→θ+Dsin(β−θ)θ→θ+Dsin⁡(β−θ)where  DD  is the perturbation strength and  ββ  is the target angle.

The noise term is only taken into account, when the checkbox is selected and can be scaled such that the standard deviation over a unit time interval is the given value.

By considering  eiθeiθ  we can visualise the evolution on the unit circle which is shown in the simulation along the histogram of the phase angles.


## Distribuição de Frequências

The natural frequencies of each oscillator are drawn at the beginning from the chosen distribution.

The Bi-Cauchy distribution allows the mixture of two Cauchy distributions with the given mean and scale factor  γγ.

In the histogram plot of the natural frequencies the two outermost bins also contain all smaller and larger, respecively, frequencies.

## Resultados Teórico

For a general mathematical perspective, the following two review papers give a good overview:

-   [Steven H. Strogatz, 2000](http://dx.doi.org/10.1016/S0167-2789(00)00094-4)
-   [Arkady Pikovsky and Michael Rosenblum, 2015](http://dx.doi.org/10.1063/1.4922971)

For the Bi-Cauchy distribution, a formal calculation can be done, see the  [paper](http://dx.doi.org/10.1103/PhysRevE.79.026204).

## Landau *Damping*

Even though there is no dissipation term, the incoherent state appears to be stable, if the coupling constant is small enough. This effect was first observed by Landau in 1946 for plasmas and works through phase mixing.

In 1992,  [Steven H. Strogatz, Renato E. Mirollo and Paul C. Matthews](http://dx.doi.org/10.1103/PhysRevLett.68.2730)  noted that the same phenomenon applies in this model.

Understanding Landau damping, is an active area of mathematical research with recent breakthroughs. In  [my first work](http://dx.doi.org/10.1016/j.matpur.2015.11.001), I understood the behaviour around the incoherent state showing Landau damping.

## Referência

- Modelo de Kuramoto [Wikipedia](https://en.wikipedia.org/wiki/Kuramoto_model)

- Artigo original [Link](https://link.springer.com/chapter/10.1007/BFb0013365)

- Kuramoto falando sobre o model de Kuramoto [Video 1](https://www.youtube.com/watch?v=lac4TxWyBOg)

- Aula - 2011 Simons Lectures - Steven Strogatz   [Video 1](https://www.youtube.com/watch?v=5zFDMyQ8z8g)

- Metrônomos sincronizando [Video 1](https://www.youtube.com/watch?v=5v5eBf2KwF8)

-   Sincronização de Vagalumes  [Video 1](https://www.youtube.com/watch?v=ZGvtnE1Wy6U) [Video 2](https://www.youtube.com/watch?v=EIgDnJdZm1A)  [Video 3](https://www.youtube.com/watch?v=0BOjTMkyfIA)

-  Material Extro [Steven H. Strogatz, 2000](http://dx.doi.org/10.1016/S0167-2789(00)00094-4)


