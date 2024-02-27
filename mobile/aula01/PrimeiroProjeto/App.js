import React, { useState, useRef } from 'react';
import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Text, TextInput, View } from 'react-native';

export default function App() {
  const [base, setBase] = useState('');
  const [altura, setAltura] = useState('');
  const [area, setArea] = useState('');
  const baseInputRef = useRef();
  
  function CalcularArea() {
    if (base > 0 && altura > 0) {
      const areaCalculada = (parseFloat(base) * parseFloat(altura)) / 2;
      setArea(areaCalculada.toString());
      setAltura('');
      setBase('');
      baseInputRef.current.clear();
      baseInputRef.current.focus();
    } else {
      setArea('');
    }
  }
  return (
    <View style={styles.container}>
      <Text>Olá Mamãe! ❤️</Text>
      <Text>Insira os dados abaixo para o cálculo da área do triângulo.</Text>
      <TextInput
        placeholder="Base"
        style={{ height: 40, textAlign: 'center' }}
        keyboardType={'numeric'}
        value={base}
        onChangeText={(base) => setBase(base)}
        ref={baseInputRef} // Atribui a referência aqui
      />

      <TextInput
        placeholder="Altura"
        style={{ height: 40, textAlign: 'center' }}
        keyboardType={'numeric'}
        value={altura}
        onChangeText={(altura) => setAltura(altura)}
      />
      <Button title="👾Calcular🤓" onPress={CalcularArea} />
      <Text>{area ? `Resultado: ${area}` : ''}</Text>
      <StatusBar style="auto" />
    </View>
  );
}
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

});




