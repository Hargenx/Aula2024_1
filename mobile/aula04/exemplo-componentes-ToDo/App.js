import React, { useState } from 'react';
import { View, Text, FlatList, TouchableOpacity, Modal, TextInput, Button as Botao, Switch } from 'react-native';
import estilos from './styles'; // Importe os estilos

const App = () => {
  const [tarefas, setTarefas] = useState([
    { id: '1', texto: 'Estudar JSX', completada: false },
    { id: '2', texto: 'Estudar React', completada: true },
    { id: '3', texto: 'Terminar projeto', completada: false },
  ]);

  const [modalVisivel, setModalVisivel] = useState(false);
  const [novoTextoTarefa, setNovoTextoTarefa] = useState('');

  const alternarStatusTarefa = (idTarefa) => {
    setTarefas((tarefasAnteriores) =>
      tarefasAnteriores.map((tarefa) =>
        tarefa.id === idTarefa ? { ...tarefa, completada: !tarefa.completada } : tarefa
      )
    );
  };

  const adicionarNovaTarefa = () => {
    if (novoTextoTarefa.trim() !== '') {
      setTarefas((tarefasAnteriores) => [
        ...tarefasAnteriores,
        { id: (tarefasAnteriores.length + 1).toString(), texto: novoTextoTarefa, completada: false },
      ]);
    }
    setModalVisivel(false);
    setNovoTextoTarefa('');
  };

  return (
    <View style={estilos.container}>
      <Text style={estilos.titulo}>Lista de Tarefas</Text>
      <FlatList
        data={tarefas}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={estilos.itemTarefa}>
            <Text style={estilos.textoTarefa}>{item.texto}</Text>
            <View style={estilos.containerStatusTarefa}>
              <Switch
                value={item.completada}
                onValueChange={() => alternarStatusTarefa(item.id)}
              />
              <Text style={{ color: item.completada ? 'green' : 'red' }}>
                {item.completada ? 'Concluída' : 'Pendente'}
              </Text>
            </View>
          </View>
        )}
      />

      <TouchableOpacity onPress={() => setModalVisivel(true)} style={estilos.botaoAdicionar}>
        <Text style={estilos.textoBotaoAdicionar}>Adicionar Tarefa</Text>
      </TouchableOpacity>

      <Modal visible={modalVisivel} animationType="slide">
        <View style={estilos.containerModal}>
          <Text style={estilos.tituloModal}>Nova Tarefa</Text>
          <TextInput
            placeholder="Digite a nova tarefa"
            style={estilos.entradaTexto}
            onChangeText={(texto) => setNovoTextoTarefa(texto)}
            value={novoTextoTarefa}
          />
          <View style={estilos.containerBotoes}>
            <Botao title="Adicionar" onPress={adicionarNovaTarefa} color="blue" style={estilos.botao} />
            <Botao title="Cancelar" onPress={() => setModalVisivel(false)} color="orange" style={estilos.botao} />
          </View>
        </View>
      </Modal>
    </View>
  );
};

export default App;
