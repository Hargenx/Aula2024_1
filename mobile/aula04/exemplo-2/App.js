import React, { useState } from 'react';
import { View, Button } from 'react-native';
import FlatListExemplo from './exemplos/FlatListExemplo';
import SectionListExemplo from './exemplos/SectionListExemplo';
import ScrollViewExemplo from './exemplos/ScrollViewExemplo';
import CarouselExemplo from './exemplos/CarouselExemplo'; 
import styles from './style/style';


export default function App() {
  const [currentScreen, setCurrentScreen] = useState(null);
  const navigateToScreen = (screenName) => {
    setCurrentScreen(screenName);
  };
  const renderScreen = () => {
    switch (currentScreen) {
      case 'FlatList':
        return <FlatListExemplo goBack={() => setCurrentScreen(null)} />;
      case 'SectionList':
        return <SectionListExemplo goBack={() => setCurrentScreen(null)} />;
      case 'ScrollView':
        return <ScrollViewExemplo goBack={() => setCurrentScreen(null)} />;
      case 'Carousel':
        return <CarouselExemplo goBack={() => setCurrentScreen(null)} />;
      default:
        return (
          <View style={styles.container}>
            <Button title="FlatList Exemplo" onPress={() => navigateToScreen('FlatList')} />
            <View style={styles.buttonSpacing} />
            <Button title="SectionList Exemplo" onPress={() => navigateToScreen('SectionList')} />
            <View style={styles.buttonSpacing} />
            <Button title="ScrollView Exemplo" onPress={() => navigateToScreen('ScrollView')} />
            <View style={styles.buttonSpacing} />
            <Button title="Carousel Exemplo" onPress={() => navigateToScreen('Carousel')} />
          </View>
        );
    }
  };
  return (
    <View style={styles.container}>
      {renderScreen()}
    </View>
  );
}
