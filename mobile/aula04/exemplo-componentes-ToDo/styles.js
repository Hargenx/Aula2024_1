import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  titulo: {
    fontSize: 20,
    marginBottom: 20,
    marginTop: 20,
  },
  botaoAdicionar: {
    backgroundColor: 'blue',
    padding: 12,
    borderRadius: 5,
    alignItems: 'center',
  },
  textoBotaoAdicionar: {
    color: 'white',
    fontSize: 16,
  },
  containerModal: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  tituloModal: {
    fontSize: 20,
    marginBottom: 20,
  },
  entradaTexto: {
    borderColor: 'gray',
    borderWidth: 1,
    padding: 10,
    width: '80%',
    marginBottom: 10,
  },
  containerBotoes: {
    flexDirection: 'row',
  },
  botao: {
    flex: 1,
  },
  itemTarefa: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  textoTarefa: {
    fontSize: 16,
  },
  containerStatusTarefa: {
    flexDirection: 'row',
    alignItems: 'center',
  },
});

export default styles;
