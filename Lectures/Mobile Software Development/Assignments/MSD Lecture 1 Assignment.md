---
creation date: 2025-09-06 15:53
modification date: Saturday 6th September 2025 15:53:47
tags:
  - Assignments
year: 2025
semester: 5
links: "[[MSD Lecture 1]]"
---

---
# [[MSD Lecture 1 Assignment]]


## Exercise: Creating a new component
- Use the application you just created
- Create a new component
- Create a file with a name such as: MyComponent.tsx o js
- Make sure it has View and Text component with text like: “Hello World!”
- Import it into App.tsx, to show the component
- Also, create another Text component  and pass a Prop with some new text. 



```tsx
//Component Hello world
import { View, Text } from 'react-native'
export function HelloWorldComponent() {
	return (
		<View>
			<Text>Hello world!<Text/>
		<View/>	 
	)
}
```


```tsx
//Hello world component with props

interface helloworldProp {
	message: string
}

export function HelloWorldComponentProps(props: helloworldProp) {
	return (
		<View>
			<Text>{props.message}<Text/>
		<View/>	 
	)
}
```


```tsx
//App.tsx

import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { HelloWorldComponent } from './HelloWorldComponent';
import { HelloWorldComponentProps } from './HelloWorldComponentProps';

export default function App() {
  return (
    <View style={styles.container}>
      <HelloWorldComponent />
      <HelloWorldComponentProps message="Hello, World from Props!" />
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
});

```