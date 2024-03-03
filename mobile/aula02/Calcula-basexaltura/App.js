/* importando os componentes e ganchos necessários do React, 
do Expo e do React Native para construir nosso aplicativo*/
import React, { useState, useRef } from 'react';
import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Text, TextInput, View } from 'react-native';
export default function App() { //componente funcional
  /** usando o useState para criar estados para as variáveis base, 
   * altura e area, que serão usadas para armazenar os valores dos campos de entrada 
   * e o resultado do cálculo da área. Usamos useRef para criar a referência baseInputRef, 
   * que será usada para manipular o campo de entrada "Base".*/
  const [base, setBase] = useState('');
  const [altura, setAltura] = useState('');
  const [area, setArea] = useState('');
  const [menssagemErro, setMenssagemErro] = useState('');

  const baseInputRef = useRef(); // Referência para o TextInput da base

   /**A função CalcularArea é responsável por calcular a área do triângulo 
   * e manipular os estados das variáveis. Se os valores de base e altura 
   * forem maiores que zero, calculamos a área, atualizamos o estado de area, 
   * e então limpamos e focamos o campo de entrada "Base". Caso contrário, 
   * apenas limpamos o estado de area. E verificamos se ambos os campos estão
   * preenchidos e enviamos um alerta caso não.*/
  function CalcularArea() {
    if (base > 0 && altura > 0) {
      const areaCalculada = (parseFloat(base) * parseFloat(altura)) / 2;
      setArea(areaCalculada.toFixed(2).toString());
      setAltura('');
      setBase('');
      baseInputRef.current.clear();
      baseInputRef.current.focus();
      setMenssagemErro('')
    } else {
      setMenssagemErro('🤢Insira todos os dados!🤮');
      setArea('');
      }
    }
       /**Usamos componentes Text para exibir mensagens, 
      * TextInput para entrada de dados, e um botão para calcular a área. 
      * A referência baseInputRef é atribuída ao campo de entrada "Base". 
      * Também exibimos o resultado da área calculada ou uma string vazia, 
      * dependendo do estado de area. */
    return (
      <View style={styles.container}>
        {/*<Text>Olá Mamãe! </Text>*/}
        <Text>Insira os dados abaixo para o cálculo da área do triângulo.❤️</Text>
        <TextInput
          placeholder="Base"
          style={styles.input}
          keyboardType={'numeric'}
          value={base}
          onChangeText={(base) => setBase(base)}
          ref={baseInputRef} // Atribui a referência aqui
        />
        <TextInput
          placeholder="Altura"
          style={styles.input}
          keyboardType={'numeric'}
          value={altura}
          onChangeText={(altura) => setAltura(altura)}
        />
        {menssagemErro ? <Text style={styles.TextoErro}>{menssagemErro}</Text> : null}
        <Button title="👾Calcular🤓" onPress={CalcularArea} />
        <Text>{area ? `Resultado: ${area}` : ''}</Text>
        <StatusBar style="auto" />
      </View>
    );
  }

  //definindo o estilo do contêiner principal usando StyleSheet.create.
const styles = StyleSheet.create({
      container: {
      flex: 1,
      backgroundColor: '#fff',
      alignItems: 'center',
      justifyContent: 'center',
    },
    input: { 
      height: 40, 
      textAlign: 'center', 
    },
    TextoErro: {
      color: 'red',
      marginTop: 10,
    },
  });
