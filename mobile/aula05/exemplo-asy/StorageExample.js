import React, { useState, useEffect } from 'react';
import { View, TextInput, Button, Text } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';

const StorageExample = () => {
  const [name, setName] = useState('');
  const [storedName, setStoredName] = useState('');

  useEffect(() => {
    // Quando o componente monta, tentamos obter o nome armazenado
    retrieveData();
  }, []);

  const storeData = async (value) => {
    try {
      await AsyncStorage.setItem('@stored_name', value);
      setStoredName(value);
    } catch (error) {
      console.error('Erro ao armazenar o nome:', error);
    }
  };

  const retrieveData = async () => {
    try {
      const value = await AsyncStorage.getItem('@stored_name');
      if (value !== null) {
        setStoredName(value);
      }
    } catch (error) {
      console.error('Erro ao recuperar o nome:', error);
    }
  };

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <TextInput
        style={{ height: 40, borderColor: 'gray', borderWidth: 1, marginBottom: 20, padding: 10 }}
        placeholder="Digite seu nome"
        onChangeText={(text) => setName(text)}
        value={name}
      />
      <Button
        title="Salvar Nome"
        onPress={() => {
          storeData(name);
          setName('');
        }}
      />
      {storedName ? <Text style={{ marginTop: 20 }}>Seu nome salvo é: {storedName}</Text> : null}
    </View>
  );
};

export default StorageExample;
