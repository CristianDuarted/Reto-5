# Reto 5 — Paquete `Shape` (Programación Orientada a Objetos)

## 1. Descripción del proyecto

Este proyecto retoma el sistema de figuras geométricas del **Reto 4**
(clases `Point`, `Line`, `Shape` y sus figuras derivadas: `Rectangle`,
`Square`, `Triangle`, `Equilateral`, `Isosceles`, `Scalene` y
`TriRectangle`) y lo reorganiza dentro de un **paquete Python**
llamado `Shape`, siguiendo buenas prácticas de modularidad,
empaquetado e importación.

La lógica interna de cada clase (fórmulas de área, perímetro,
validaciones de tipo de triángulo, etc.) **no fue modificada**:
únicamente se reordenó el código en módulos y paquetes, y se
corrigieron las sentencias `import`.

## 2. Objetivo del reto

Aplicar los conceptos de **paquetes y módulos en Python** para:

- Encapsular un conjunto de clases relacionadas por herencia dentro
  de un paquete formal (`Shape`).
- Comparar dos estrategias válidas de organización de código:
  un módulo único vs. módulos independientes por clase.
- Practicar la correcta gestión de importaciones relativas
  (`from .modulo import Clase`) dentro de un paquete.
- Entregar un proyecto con estructura profesional, documentación y
  diagrama UML.

## 3. Estructura del proyecto

```
Reto5-Shape/
├── Shape/
│   ├── __init__.py
│   ├── opcion1_modulo_unico/
│   │   ├── __init__.py
│   │   └── shapes.py
│   └── opcion2_modulos_separados/
│       ├── __init__.py
│       ├── point.py
│       ├── line.py
│       ├── shape.py
│       ├── rectangle.py
│       ├── square.py
│       ├── triangle.py
│       ├── equilateral.py
│       ├── isosceles.py
│       ├── scalene.py
│       └── tri_rectangle.py
├── main.py              # Programa principal (usa Opción 2)
├── main_opcion1.py       # Demo alterna (usa Opción 1)
└── README.md
```

## 4. Opción 1: módulo único (`opcion1_modulo_unico`)

Todas las clases viven dentro de un único archivo: `shapes.py`. El
`__init__.py` del subpaquete reexporta las clases para que puedan
importarse directamente:

```python
from Shape.opcion1_modulo_unico import Rectangle, Triangle
```

**Ventajas:** simplicidad, todo el modelo en un solo lugar.
**Desventajas:** el archivo crece mucho si se agregan más figuras.

## 5. Opción 2: un módulo por clase (`opcion2_modulos_separados`)

Cada clase vive en su propio archivo. Todas heredan de la clase base
`Shape` definida en `shape.py`.

```python
from Shape.opcion2_modulos_separados import Rectangle, Triangle
```

**Ventajas:** alta cohesión, cada módulo tiene una única
responsabilidad; más escalable y mantenible.
**Desventajas:** más archivos que gestionar.

## 6. Diagrama UML

Ver diagrama de herencia en `diagrama_uml.md` (formato Mermaid).

## 7. Conclusiones

- Ambas opciones son funcionalmente equivalentes.
- La Opción 1 es más rápida para proyectos pequeños.
- La Opción 2 favorece el principio de responsabilidad única (SRP)
  y es la práctica recomendada en proyectos reales.
