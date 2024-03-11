import React from 'react';
import { View, Text, StyleSheet, Image } from 'react-native';
const App = () => {
  return (
    <View style={styles.container}>
      <Image
        source={require('./assets/img/fun.png')}
        style={styles.logo}
      />
      <Text style={styles.header}>Minha APP</Text>
      <View style={styles.nav}>
        <Text style={styles.navLink} onPress={() => console.log('Início clicado')}>
          Início
        </Text>
        <Text style={styles.navLink} onPress={() => console.log('Sobre clicado')}>
          Sobre
        </Text>
        <Text style={styles.navLink} onPress={() => console.log('Contato clicado')}>
          Contato
        </Text>
      </View>
      <View style={styles.section} id="inicio">
        <Text style={styles.sectionHeader}>Seção de Início</Text>
        <Text>Conteúdo da seção de Início.</Text>
        <Text>{'\n'}{'\n'}{'\n'}{'\n'}{'\n'}</Text>
      </View>
      <View style={styles.section} id="sobre">
        <Text style={styles.sectionHeader}>Seção Sobre</Text>
        <Text>Conteúdo da seção Sobre.</Text>
        <Text>{'\n'}{'\n'}{'\n'}{'\n'}{'\n'}</Text>
      </View>
      <View style={styles.section} id="contato">
        <Text style={styles.sectionHeader}>Seção de Contato</Text>
        <Text>Conteúdo da seção de Contato.</Text>
        <Text>{'\n'}{'\n'}{'\n'}{'\n'}{'\n'}</Text>
      </View>
    </View>
  );
};
const styles = StyleSheet.create({
  container: {
    padding: 20,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 20,
  },
  logo: {
    width: 40,
    height: 40,
    marginRight: 10,
  },
  headerText: {
    fontSize: 24,
  },
  nav: {
    flexDirection: 'row',
    justifyContent: 'center',
    marginBottom: 20,
  },
  navLink: {
    marginHorizontal: 10,
    color: 'blue',
  },
  section: {
    marginBottom: 30,
  },
  sectionHeader: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 10,
  },
});
export default App;
