# Questão 1
q1 <- function(n, m) {
  resultados <- replicate(m, sum(sample(c(0, 1), n, replace = TRUE)))
  hist(resultados, breaks = seq(0, n+1), xlab = "Número de Sucessos", main = "Histograma de Número de Sucessos")
}

# Questão 2a
q2a <- function() {
  media <- 12 * 0.5
  variancia <- 12 * (1/12) * (1/12)
  cat("Média:", media, "\n")
  cat("Variância:", variancia, "\n")
  # Gráfico da distribuição
  curve(dnorm(x, mean = media, sd = sqrt(variancia)), from = 0, to = 12, xlab = "X", ylab = "Densidade", main = "Distribuição de X")
}

# Questão 2b
'''o método Monte Carlo é usado para obter uma aproximação empírica da distribuição da soma de 12 variáveis aleatórias uniformemente distribuídas.'''
q2b <- function(n) {
  x <- matrix(runif(n*12), ncol = 12)
  x_sum <- rowSums(x)
  media <- mean(x_sum)
  variancia <- var(x_sum)
  cat("Média:", media, "\n")
  cat("Variância:", variancia, "\n")
  hist(x_sum, breaks = "FD", xlab = "X", main = "Histograma da Soma de 12 VAs Uniformes")
}

# Questão 3
''' o método Monte Carlo é usado para obter uma aproximação empírica da distribuição da soma de 5, 10 ou 15 distribuições triangulares.'''
q3 <- function(n, m) {
  x <- matrix(runif(n*m, 10, 30), ncol = m)
  x_sum <- rowSums(x)
  media <- mean(x_sum)
  variancia <- var(x_sum)
  cat("Média:", media, "\n")
  cat("Variância:", variancia, "\n")
  hist(x_sum, breaks = "FD", xlab = "X", main = "Histograma da Soma de Distribuições Triangulares")
}

# Questão 4a
'''o método Monte Carlo é usado para obter uma aproximação empírica das funções de probabilidade especificadas para diferentes variáveis aleatórias.'''
q4a <- function(n) {
  x <- rnorm(n)
  y <- rnorm(n)
  z <- x * y
  hist(z, breaks = "FD", xlab = "Z", main = "Histograma do Produto de Duas VAs Normais")
}

# Questão 4b
q4b <- function(n) {
  x <- rnorm(n)
  y <- rnorm(n)
  z <- x / y
  hist(z, breaks = "FD", xlab = "Z", main = "Histograma do Quociente de Duas VAs Normais")
}

# Questão 4c
q4c <- function(n, i) {
  maximos <- apply(matrix(rnorm(n*i), ncol = i), 1, max)
  hist(maximos, breaks = "FD", xlab = "Máximo", main = paste("Histograma do Máximo de", i, "VAs Normais"))
}

# Questão 4d
q4d <- function(n, m) {
  chisquare <- replicate(m, sum(rnorm(n)^2))
  hist(chisquare, breaks = "FD", xlab = "χ^2", main = "Histograma da Distribuição χ^2")
}

# Questão 4e
q4e <- function(n) {
  z <- exp(rnorm(n))
  hist(z, breaks = "FD", xlab = "Z", main = "Histograma da Distribuição Z = e^N(0,1)")
}
