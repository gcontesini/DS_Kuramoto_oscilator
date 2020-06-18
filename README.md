# Model de Kuramoto

## Modelo Matemático

O oscilador de Kuramoto é um modelo matemático que explica a o fenômeno de sincronização de $N$ oscilador inicialmente dessincronizados. Inicialmente dada oscilador $i=1,2,\dots,N$ possui uma frequência natural de oscilação própria $\omega_i$. Adicionalmente cada oscilador possui um termo de acoplamento $f(\theta_i,\theta_j)$ que depende da fase dos demais osciladores. A evolução dos osciladores é dada pela seguinte equação,

$\frac{d}{dt}\theta_i = \omega_i  +\frac{K}{N}\sum^{N}_{j=1}sin(\theta_j-\theta_i)$  

## Parâmetro de Ordem

Observamos que o plote do parâmetro de ordem em coordenadas polares. Interpretando o parâmetro de ordem como um análogo ao centro de massa do sistema, observamos que o sistema sob estas destas duas condições representa a duas situações no qual o centro de massa do sistema permanece estacionário.

O parâmetro de ordem do sistema é dado pelo Kernel de Dirichlet. Este parâmetro resume a interação entre os osciladores, ou seja, este mede diretamente o grau de sincronização  do sistema. O Kernel de Dirichlet é dado por,

$re^{i\theta}=∑^{N}_{j=0}e^{iθj}$

Se reescrevermos o sistema em termos do parâmetro de ordem,

$\theta_{i} = \omega_{i} + K r sin(\theta-\theta_{j})$,

obtemos que os zeros do kernel de Dirichlet, localizados em $\theta=\theta_{j}$ e $\theta=\frac{2\pi}{N}(j-1)$ contém as soluções estacionárias do sistema. As condições  serão os pontos de estabilidade do sistema para $\theta=\theta_{j}$, obtemos o sistema sincronizados, e para $\theta=\frac{2\pi}{N}(j-1)$ teremos os sistema dessincronizado sem fase.

## Referencial Teórico

Para uma analise, e revisão mais detalhada sobre fenômenos de emergência de sincronicidade em sistemas dinâmicos, consulte os seguintes dois artigos científicos;
-   [Steven H. Strogatz, 2000](http://dx.doi.org/10.1016/S0167-2789(00)00094-4)
-   [APS](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.77.137)

## Apêndice

- Modelo de Kuramoto [Wikipedia](https://en.wikipedia.org/wiki/Kuramoto_model)

- Artigo original [Link](https://link.springer.com/chapter/10.1007/BFb0013365)

- Kuramoto falando sobre o model de Kuramoto [Video 1](https://www.youtube.com/watch?v=lac4TxWyBOg)

- Aula - 2011 Simons Lectures - Steven Strogatz   [Video 1](https://www.youtube.com/watch?v=5zFDMyQ8z8g)

- Metrônomos sincronizando [Video 1](https://www.youtube.com/watch?v=5v5eBf2KwF8)

-   Sincronização de Vagalumes  [Video 1](https://www.youtube.com/watch?v=ZGvtnE1Wy6U) [Video 2](https://www.youtube.com/watch?v=EIgDnJdZm1A)  [Video 3](https://www.youtube.com/watch?v=0BOjTMkyfIA)

-  Material Extra [Steven H. Strogatz, 2000](http://dx.doi.org/10.1016/S0167-2789(00)00094-4)


