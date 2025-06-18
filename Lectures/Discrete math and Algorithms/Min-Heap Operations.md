
## Udfør først **HEAP-EXTRACT-MIN**(B) og dernæst **MIN-HEAP-INSERT**(B,2) på nedenstående min-heap **B** (dvs. fjern først den mindste værdi, og indsæt dernæst værdien 2)

$$B:\quad\begin{array}{ccccccccc}
\boxed{3} & \boxed{5} & \boxed{4} & \boxed{8} & \boxed{7} & \boxed{6} & \boxed{9} & \boxed{10} & \boxed{11}
\end{array}$$




```tikz
\usepackage{tikz}
\usetikzlibrary{trees}

\begin{document}

\begin{tikzpicture}[
  level 1/.style={sibling distance=40mm},
  level 2/.style={sibling distance=20mm},
  level 3/.style={sibling distance=10mm},
  every node/.style={circle,draw}
  ]

\node {3}
  child {node {5}
    child {node {8}
      child {node {10}}
      child {node {11}}
    }
    child {node {7}}
  }
  child {node {4}
    child {node {6}}
    child {node {9}}
  };

\end{tikzpicture}

\end{document}
```



## Heap Extract-min

min value is removed from the root node and the last value in the array/binary tree becomes the new root node.


### Heapify Down to restore min-heap

```tikz
\usepackage{tikz}
\usetikzlibrary{trees}

\begin{document}

\begin{tikzpicture}[
  level 1/.style={sibling distance=40mm},
  level 2/.style={sibling distance=20mm},
  level 3/.style={sibling distance=10mm},
  every node/.style={circle,draw}
  ]

\node {11}
  child {node {5}
    child {node {8}
      child {node {10}}
    }
    child {node {7}}
  }
  child {node {4}
    child {node {6}}
    child {node {9}}
  };

\end{tikzpicture}

\end{document}
```


Compare root node with it's  children and swap with the lowest  value, until the  root node is smaller than it's children or until it doesn't have any children (leaf node)


```tikz
\usepackage{tikz}
\usetikzlibrary{trees}

\begin{document}

\begin{tikzpicture}[
  level 1/.style={sibling distance=40mm},
  level 2/.style={sibling distance=20mm},
  level 3/.style={sibling distance=10mm},
  every node/.style={circle,draw}
  ]

\node {4}
  child {node {5}
    child {node {8}
      child {node {10}}
    }
    child {node {7}}
  }
  child {node {11}
    child {node {6}}
    child {node {9}}
  };

\end{tikzpicture}

\end{document}
```



```tikz
\usepackage{tikz}
\usetikzlibrary{trees}

\begin{document}

\begin{tikzpicture}[
  level 1/.style={sibling distance=40mm},
  level 2/.style={sibling distance=20mm},
  level 3/.style={sibling distance=10mm},
  every node/.style={circle,draw}
  ]

\node {4}
  child {node {5}
    child {node {8}
      child {node {10}}
    }
    child {node {7}}
  }
  child {node {6}
    child {node {11}}
    child {node {9}}
  };

\end{tikzpicture}

\end{document}
```


Since the old root node (11) is  a lead node, we stop and continue with the next step


## min-heap-insert(B,2)

```tikz
\usepackage{tikz}
\usetikzlibrary{trees}

\begin{document}

\begin{tikzpicture}[
  level 1/.style={sibling distance=40mm},
  level 2/.style={sibling distance=20mm},
  level 3/.style={sibling distance=10mm},
  every node/.style={circle,draw}
  ]

\node {4}
  child {node {5}
    child {node {8}
      child {node {10}}
      child {node {2}}
    }
    child {node {7}}
  }
  child {node {6}
    child {node {11}}
    child {node {9}}
  };

\end{tikzpicture}

\end{document}
```

We add 2 to the end of the heap and perform heapify up. We keep swapping until the insert value becomes the new root node...


```tikz
\usepackage{tikz}
\usetikzlibrary{trees}

\begin{document}

\begin{tikzpicture}[
  level 1/.style={sibling distance=40mm},
  level 2/.style={sibling distance=20mm},
  level 3/.style={sibling distance=10mm},
  every node/.style={circle,draw}
  ]

\node {4}
  child {node {5}
    child {node {2}
      child {node {10}}
      child {node {8}}
    }
    child {node {7}}
  }
  child {node {6}
    child {node {11}}
    child {node {9}}
  };

\end{tikzpicture}

\end{document}
```



```tikz
\usepackage{tikz}
\usetikzlibrary{trees}

\begin{document}

\begin{tikzpicture}[
  level 1/.style={sibling distance=40mm},
  level 2/.style={sibling distance=20mm},
  level 3/.style={sibling distance=10mm},
  every node/.style={circle,draw}
  ]

\node {4}
  child {node {2}
    child {node {5}
      child {node {10}}
      child {node {8}}
    }
    child {node {7}}
  }
  child {node {6}
    child {node {11}}
    child {node {9}}
  };

\end{tikzpicture}

\end{document}
```



## Udfør først **HEAP-EXTRACT-MIN**(B) og dernæst **MIN-HEAP-INSERT**(B,2) på nedenstående min-heap **B** (dvs. fjern først den mindste værdi, og indsæt dernæst værdien 2)

$$B:\quad\begin{array}{ccccccccc}
\boxed{3} & \boxed{5} & \boxed{4} & \boxed{8} & \boxed{7} & \boxed{6} & \boxed{9} & \boxed{10} & \boxed{11}
\end{array}$$




```tikz
\usepackage{tikz}
\usetikzlibrary{trees}

\begin{document}

\begin{tikzpicture}[
  level 1/.style={sibling distance=40mm},
  level 2/.style={sibling distance=20mm},
  level 3/.style={sibling distance=10mm},
  every node/.style={circle,draw}
  ]

\node {3}
  child {node {5}
    child {node {8}
      child {node {10}}
      child {node {11}}
    }
    child {node {7}}
  }
  child {node {4}
    child {node {6}}
    child {node {9}}
  };

\end{tikzpicture}

\end{document}
```



## Heap Extract-min

min value is removed from the root node and the last value in the array/binary tree becomes the new root node.


### Heapify Down to restore min-heap

```tikz
\usepackage{tikz}
\usetikzlibrary{trees}

\begin{document}

\begin{tikzpicture}[
  level 1/.style={sibling distance=40mm},
  level 2/.style={sibling distance=20mm},
  level 3/.style={sibling distance=10mm},
  every node/.style={circle,draw}
  ]

\node {11}
  child {node {5}
    child {node {8}
      child {node {10}}
    }
    child {node {7}}
  }
  child {node {4}
    child {node {6}}
    child {node {9}}
  };

\end{tikzpicture}

\end{document}
```


Compare root node with it's  children and swap with the lowest  value, until the  root node is smaller than it's children or until it doesn't have any children (leaf node)


```tikz
\usepackage{tikz}
\usetikzlibrary{trees}

\begin{document}

\begin{tikzpicture}[
  level 1/.style={sibling distance=40mm},
  level 2/.style={sibling distance=20mm},
  level 3/.style={sibling distance=10mm},
  every node/.style={circle,draw}
  ]

\node {4}
  child {node {5}
    child {node {8}
      child {node {10}}
    }
    child {node {7}}
  }
  child {node {11}
    child {node {6}}
    child {node {9}}
  };

\end{tikzpicture}

\end{document}
```



```tikz
\usepackage{tikz}
\usetikzlibrary{trees}

\begin{document}

\begin{tikzpicture}[
  level 1/.style={sibling distance=40mm},
  level 2/.style={sibling distance=20mm},
  level 3/.style={sibling distance=10mm},
  every node/.style={circle,draw}
  ]

\node {4}
  child {node {5}
    child {node {8}
      child {node {10}}
    }
    child {node {7}}
  }
  child {node {6}
    child {node {11}}
    child {node {9}}
  };

\end{tikzpicture}

\end{document}
```


Since the old root node (11) is  a lead node, we stop and continue with the next step


## min-heap-insert(B,2)

```tikz
\usepackage{tikz}
\usetikzlibrary{trees}

\begin{document}

\begin{tikzpicture}[
  level 1/.style={sibling distance=40mm},
  level 2/.style={sibling distance=20mm},
  level 3/.style={sibling distance=10mm},
  every node/.style={circle,draw}
  ]

\node {4}
  child {node {5}
    child {node {8}
      child {node {10}}
      child {node {2}}
    }
    child {node {7}}
  }
  child {node {6}
    child {node {11}}
    child {node {9}}
  };

\end{tikzpicture}

\end{document}
```

We add 2 to the end of the heap and perform heapify up. We keep swapping until the insert value becomes the new root node...


```tikz
\usepackage{tikz}
\usetikzlibrary{trees}

\begin{document}

\begin{tikzpicture}[
  level 1/.style={sibling distance=40mm},
  level 2/.style={sibling distance=20mm},
  level 3/.style={sibling distance=10mm},
  every node/.style={circle,draw}
  ]

\node {4}
  child {node {5}
    child {node {2}
      child {node {10}}
      child {node {8}}
    }
    child {node {7}}
  }
  child {node {6}
    child {node {11}}
    child {node {9}}
  };

\end{tikzpicture}

\end{document}
```



```tikz
\usepackage{tikz}
\usetikzlibrary{trees}

\begin{document}

\begin{tikzpicture}[
  level 1/.style={sibling distance=40mm},
  level 2/.style={sibling distance=20mm},
  level 3/.style={sibling distance=10mm},
  every node/.style={circle,draw}
  ]

\node {2}
  child {node {4}
    child {node {5}
      child {node {10}}
      child {node {8}}
    }
    child {node {7}}
  }
  child {node {6}
    child {node {11}}
    child {node {9}}
  };

\end{tikzpicture}

\end{document}
```



```tikz
\usepackage{tikz}
\usetikzlibrary{trees}

\begin{document}

\begin{tikzpicture}[
  level distance=1.2cm,
  level 1/.style={sibling distance=40mm},
  level 2/.style={sibling distance=20mm},
  level 3/.style={sibling distance=10mm},
  every node/.style={circle,draw,minimum size=7mm,inner sep=1pt},
  edge from parent/.style={draw,thick}
  ]

% Tree
\node (root) {2}
  child {node {4}
    child {node {5}
      child {node {10}}
      child {node {8}}
    }
    child {node {7}}
  }
  child {node {6}
    child {node {11}}
    child {node {9}}
  };

% Level labels
\node[draw=none,rectangle,anchor=east] at (-3.5,0)     {Level 0:};
\node[draw=none,rectangle,anchor=east] at (-3.5,-1.2)  {Level 1:};
\node[draw=none,rectangle,anchor=east] at (-3.5,-2.4)  {Level 2:};
\node[draw=none,rectangle,anchor=east] at (-3.5,-3.6)  {Level 3:};

\end{tikzpicture}

\end{document}
```


$$B:\quad\begin{array}{ccccccccc}
\boxed{2} & \boxed{4} & \boxed{6} & \boxed{5} & \boxed{7} & \boxed{11} & \boxed{9} & \boxed{10} & \boxed{8}
\end{array}$$



