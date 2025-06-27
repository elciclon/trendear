# 📊 Screener Fundamental

Este proyecto es un **screener financiero de código abierto** que permite analizar empresas listadas en cualquier mercado del mundo a partir de sus balances, resultados e indicadores clave de rendimiento (KPIs).  
Está siendo desarrollado como una oportunidad de investigación personal, integrando ciencia de datos, finanzas y desarrollo web.

> 🎓 Estoy documentando el proceso paso a paso en LinkedIn como parte de un ejercicio de *public building* y aprendizaje activo.

---

## 🚀 ¿Qué hace este screener?

✅ Modela empresas, balances y KPIs en una base de datos relacional  
✅ Permite cargar estados financieros trimestrales y anuales  
✅ Calcula automáticamente métricas como P/E, ROE, FCF Yield  
✅ Provee una API para consultar, filtrar y comparar empresas  
✅ Se conecta a una interfaz web para visualizar resultados

---

## 🧱 Arquitectura

- **Backend:** Python 3.12, PostgreSQL 16 + TimescaleDB
- **ETL:** Pandas, SQLAlchemy, (scrapers por fuente)
- **KPIs:** Calculados desde los datos brutos en SQL y Python
- **Front-end:** en desarrollo (Angular o Dash)
- **Visualización:** gráficos y tablas dinámicas
- **Licencia:** MIT

---


└── README.md # Este archivo

