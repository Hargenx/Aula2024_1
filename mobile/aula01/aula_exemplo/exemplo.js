// Função simples que exibe uma mensagem no console
function saudacao() {
    console.log("Olá, pessoal!\nOlá, Mamãe e papai!");
}// Chamando a função
saudacao(); // Isso imprimirá "Olá,...!" no console

// Função que soma dois números e retorna o resultado
function somar(a, b) {
    return a + b;
}// Chamando a função e armazenando o resultado em uma variável
var resultado = somar(5, 3);// Exibindo o resultado
console.log("A soma é: " + resultado); // Isso imprimirá "A soma é: 8" no console


const numeros = [1, 2, 3, 4, 5];
const [primeiro, segundo, ...resto] = numeros;
console.log(primeiro); // 1
console.log(segundo); // 2
console.log(resto); // [3, 4, 5]