#1-Simule um jogo de cara ou coroa. Verifique a frequencia do número de caras com: 10, 100 e 1000 lançamentos.
ex1 = function () {
	for(N in c(10,100,1000))
	print(sum(sample(0:1,N,replace=T)))
}


#2- Seja X uma VA que representa a soma de 12 VAs uniformes (0,1):
#2a- Usando o TCL, obtenha uma aproximação analítica para a X, e calcule a média, a variância e esboce um gráfico dessa distribuição.
ex2a <- function() {
  media <- 12 * (1^2/2 - 0^2/2)
  var <- function(x) x^3/3-x^2/2+x/4   ## integral de (x-1/2)2 * 1 dx para ser aplicada entre 0 e 1
  variancia <- 12 * (var(1) - var(0))
  print(c(media,variancia))  
}


#2b-idem ao 2a usando MC.
ex2b = function(){
  m <- matrix(runif(12000), ncol = 12)
  c <- apply(m, 1, sum)
  print(c(mean(c),var(c)))
  hist(c)
}
  

#3- Usando MC, obtenha uma aproximação empírica para a VA que representa a soma de 10 distribuições triangulares Xi distribuidas com parâmetros (mini = i; maxi = 20 + i; mprovi = 10 + i). Calcule a média, a variância e plote um gráfico de sua função de probabilidade.
ex3 = function(){
  library (triangle)
  media <- c()
  variancia <- c()
  for(n in 1:1000){
    u <- 0
    for(i in 1:10){
      u <- rtriangle(1000,i,20+i,10+1) + u
    }
    media <- c(media,mean(u))
    variancia <- c(variancia,var(u))
  }
  mean(media)
  mean(variancia)
  hist(u)
}

#4- Usando simulação:
#4a- obtenha uma aproximação empírica para a função de probabilidade do produto de duas VAs Z = X ∗ Y; X; Y ∼ N(0; 1).
ex4a = function(n){
  z <- rnorm(n,0,1) * rnorm(n,0,1)
  hist(z)
}

#4b- idem para o quociente Z = X=Y .
ex4b = function(n){
  z <- rnorm(n,0,1) / rnorm(n,0,1)
  hist(z)  
}

#5-Obtenha um aproximação empírica para a função de probabilidade Máximo(Xi)(i = 2; 5; 10) que representa a função de probabilidade do máximo dentre i VAs cada uma delas seguindo uma Normal(0; 1).
ex5 = function(){
  len = 3000
  tam <- c(2,5,10)
  
  for(t in 1:3 ){
    conjunto <- c()
    for(l in 1:len){
      x1 <- -Inf
      for(t2 in 1:tam[t] )  x1 <- max(x1,rnorm(1,0,1))
      conjunto <- c(conjunto,x1)
    }
    hist(conjunto)
  }
}

#6-Obtenha uma aproximação empírica para a função χ2(n) = Pn 1 Xi2 onde Xi ∼ Normal(0; 1).

ex6 = function(){
  aprox <- function(n){
    z <- n *rnorm(1000,0,1) ^2
    hist(z)
  }
  for(h in 1:4)
    aprox(h)
}

#7-Obtenha uma aproximaçãao empirica para a função de probabilidade Z = eN(0;1)
ex7 = function(){
  z <- exp(rnorm(1000,0,1))
  hist(z)
}
