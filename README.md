# HealthIA 🏥🤖

Sistema de diagnóstico médico baseado em Machine Learning que utiliza XGBoost e processamento de linguagem natural para prever possíveis diagnósticos a partir de sintomas descritos.

## 📋 Descrição

O HealthIA é uma API REST que recebe sintomas como entrada e retorna um diagnóstico previsto baseado em um modelo de Machine Learning treinado. O sistema é capaz de identificar 20 doenças diferentes através da análise de sintomas textuais.

### Doenças Identificadas

- Anemia Falciforme
- Artrite Reumatoide
- Diabetes Tipo 1
- Doença de Alzheimer
- Doença de Crohn
- Doença de Lyme
- Doença de Parkinson
- Doença de Wilson
- Esclerose Lateral
- Esclerose Múltipla
- Febre Maculosa
- Fibromialgia
- Hipertireoidismo
- Hipotireoidismo
- Lúpus
- Miastenia Gravis
- Porfiria
- Sarcoidose
- Síndrome da Fadiga Crônica
- Síndrome de Sjögren

## 🚀 Tecnologias

- **Python 3.x**
- **FastAPI** - Framework web para criação da API
- **XGBoost** - Algoritmo de Machine Learning
- **scikit-learn** - Vetorização TF-IDF e métricas
- **pandas** - Manipulação de dados
- **joblib** - Serialização de modelos
- **uvicorn** - Servidor ASGI

## 📁 Estrutura do Projeto

```
.
├── api/
│   ├── sintomasAPI.py        # Endpoints da API
│   └── testAPI.py            # Testes da API
├── services/
│   ├── datasetService.py     # Dataset de sintomas e diagnósticos
│   ├── vetorizacaoService.py # Vetorização TF-IDF dos textos
│   ├── treinamentoService.py # Treinamento do modelo
│   ├── treinamentoMsgService.py # Treinamento com logs
│   ├── salvarModeloService.py   # Salvamento dos artefatos
│   └── executarService.py    # Classe para predição
├── model/
│   ├── modelo_HealthIA.json  # Modelo XGBoost treinado
│   ├── vetorizador_HealthIA.pkl # Vetorizador TF-IDF
│   └── encoder_HealthIA.pkl  # Encoder de labels
├── main.py                   # Aplicação principal FastAPI
└── leitura.py               # Scripts auxiliares
```

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd healthia
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install fastapi uvicorn xgboost scikit-learn pandas joblib
```

## 🎓 Treinamento do Modelo

Antes de usar a API, é necessário treinar e salvar o modelo:

```python
python leitura.py
```

Isso irá:
1. Vetorizar os dados usando TF-IDF
2. Treinar o modelo XGBoost
3. Salvar o modelo, vetorizador e encoder na pasta `model/`

### Verificar Acurácia

Para treinar e visualizar a acurácia com mensagens detalhadas:

```python
from services.treinamentoMsgService import acuracia_modelo_with_msg

acuracia = acuracia_modelo_with_msg()
```

## 🌐 Uso da API

### Iniciar o servidor

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`

### Documentação Interativa

Acesse `http://localhost:8000/docs` para ver a documentação Swagger gerada automaticamente.

### Endpoints

#### GET /
Rota raiz de boas-vindas.

**Resposta:**
```json
{
  "mensagem": "Bem vindo à API HealthIA"
}
```

#### GET /predict
Realiza predição de diagnóstico baseado em sintomas.

**Parâmetros:**
- `sintomas` (query string): Sintomas separados por vírgulas

**Exemplo de requisição:**
```bash
curl "http://localhost:8000/predict?sintomas=cansaço extremo,dor articular severa,crises dolorosas"
```

**Resposta:**
```json
{
  "sintomas": [
    "cansaço extremo",
    "dor articular severa",
    "crises dolorosas"
  ],
  "diagnostico_previsto": ["anemia_falciforme"]
}
```

## 🧪 Exemplo de Uso

```python
from services.executarService import DiagnosticoIA

# Carregar o modelo
diagnostico = DiagnosticoIA(caminhoModelo='model')

# Fazer predição
sintomas = "cansaço extremo dor articular severa crises dolorosas"
resultado = diagnostico.predict_simples(sintomas)

print(f"Diagnóstico previsto: {resultado}")
```

## 📊 Características do Modelo

- **Algoritmo**: XGBoost Classifier
- **Vetorização**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Hiperparâmetros**:
  - n_estimators: 150
  - learning_rate: 0.03
  - max_depth: 3
  - min_child_weight: 1
- **Divisão dos dados**: 70% treino / 30% teste
- **Acurácia esperada**: Tipicamente acima de 85%

## ⚠️ Avisos Importantes

1. **Uso Educacional**: Este sistema é apenas para fins educacionais e demonstrativos.
2. **Não substitui profissionais**: Nunca use este sistema como substituto para diagnóstico médico profissional.
3. **Consulte um médico**: Sempre consulte um profissional de saúde qualificado para diagnósticos reais.
4. **Dataset limitado**: O modelo foi treinado com um dataset limitado e pode não cobrir todas as variações de sintomas.

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👥 Autores

Desenvolvido como projeto educacional de Machine Learning aplicado à saúde.

## 📧 Contato

Para dúvidas ou sugestões, abra uma issue no repositório.

---

**Disclaimer**: Este software não deve ser usado para diagnósticos médicos reais. Sempre consulte um profissional de saúde qualificado.
