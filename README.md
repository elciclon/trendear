# 📊 Screener Fundamental

Este proyecto es un **screener financiero de código abierto** que permite analizar empresas listadas en cualquier mercado del mundo a partir de sus balances, resultados e indicadores clave de rendimiento (KPIs).  
Está siendo desarrollado como una oportunidad de investigación personal, integrando ciencia de datos, finanzas y desarrollo web.

> 🎓 Estoy documentando el proceso paso a paso en LinkedIn como parte de un ejercicio de _public building_ y aprendizaje activo.

---

## 🚀 ¿Qué hace este screener?

✅ Modela empresas, balances y KPIs en una base de datos relacional  
✅ Permite cargar estados financieros trimestrales y anuales  
✅ Calcula automáticamente métricas como P/E, ROE, FCF Yield  
✅ Provee una API para consultar, filtrar y comparar empresas  
✅ Se conecta a una interfaz web para visualizar resultados

---

## 🧱 Arquitectura

-   **Backend:** Python 3.11, PostgreSQL 16 + TimescaleDB
-   **ETL:** Pandas, SQLAlchemy, (scrapers por fuente)
-   **KPIs:** Calculados desde los datos brutos en SQL y Python
-   **Front-end:** en desarrollo (Angular o Dash)
-   **Visualización:** gráficos y tablas dinámicas
-   **Licencia:** MIT

---

# 📊 Financial Screener for Global Equities

A modular, data-driven platform to collect, store, analyze and visualize key financial metrics for publicly traded companies worldwide.  
Designed as both a professional-grade tool and a didactic project in the context of a Data Science degree.

---

## 🚀 Project Goals

-   🏗 Build a backend to ingest and normalize data from quarterly and annual financial reports (balance sheet, income, cash flow)
-   🌍 Cover global assets (U.S. equities, CEDEARs, Merval, etc.)
-   🧮 Implement customizable financial KPIs per asset type
-   📊 Enable interactive exploration via a clean, web-based UI
-   🧠 Use this project as a learning tool and for public building on LinkedIn

## 🧱 Architecture

-   **Backend:** Python 3.12, PostgreSQL 16 + TimescaleDB
-   **ETL:** Pandas, SQLAlchemy, (custom scrapers per data source)
-   **KPIs:** Calculated from raw financial data using SQL and Python
-   **Front-end:** In development (Angular or Dash)
-   **Visualization:** Interactive charts and dynamic tables
-   **License:** MIT
