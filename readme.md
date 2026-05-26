# ProjetoComIA_backend 📝

API Flask para geração e correção automática de redações estilo ENEM usando o modelo Gemini 3.5 Flash da Google.

## 📋 Visão Geral

Este projeto fornece um backend em Python com endpoints REST que:
- **Gera** redações originais estruturadas com base em um tema
- **Corrige** redações com análise detalhada das 5 competências do ENEM
- **Sugere** temas para prática

Cada redação gerada contém:
- Título
- Introdução
- Desenvolvimento
- Conclusão
- Referências
- Análise das competências ENEM

## 🛠️ Tecnologias

- Python 3.x
- Flask
- Flask-CORS
- google-genai (Gemini 3.5 Flash)
- python-dotenv
- JSON Schema para validação de respostas

## 📁 Arquivos principais

- `app.py` - Aplicação Flask com endpoints REST
- `config.py` - Schemas JSON e instruções de sistema para o modelo
- `requirements.txt` - Dependências do projeto
- `vercel.json` - Configuração de deploy para Vercel
- `.env` - Variáveis de ambiente (não incluir no Git)

## 🚀 Instalação

1. **Clone o repositório:**

```bash
git clone <seu-repositorio>
cd ProjetoComIA_backend
```

2. **Crie e ative um ambiente virtual:**

```bash
python -m venv venv
```

No Windows:
```bash
venv\Scripts\activate
```

No macOS/Linux:
```bash
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Configure a variável de ambiente:**

Crie um arquivo `.env` na raiz do projeto:

```env
GEMINI_API_KEY=sua_chave_api_gemini_aqui
```

> 💡 Obtenha sua chave em: https://aistudio.google.com/app/apikeys

## ▶️ Executando localmente

```bash
python app.py
```

A API estará disponível em `http://127.0.0.1:5000`

## 🔌 Endpoints

### `GET /`

Verifica o status da API.

**Resposta:**

```json
{
  "status": "success",
  "message": "API Gerador de Redações ENEM 1000 funcionando!",
  "version": "2.0",
  "descricao": "Gerador automático de redações nota 1000 para o ENEM"
}
```

### `POST /gerar-redacao`

Gera uma redação completa com base em um tema fornecido.

**Requisição:**

```json
{
  "tema": "Desafios da inclusão digital no Brasil"
}
```

**Validação:**
- O tema deve ter no mínimo 10 caracteres
- Campo obrigatório

**Resposta de sucesso (200):**

```json
{
  "status": "success",
  "tema_solicitado": "Desafios da inclusão digital no Brasil",
  "redacao": {
    "titulo": "...",
    "introducao": "...",
    "desenvolvimento": "...",
    "conclusao": "...",
    "referencias": ["...", "..."]
  }
}
```

**Erros possíveis:**
- `400` - Tema não fornecido ou muito curto
- `500` - Erro ao chamar a API do Gemini

### `POST /corrigir-redacao`

Corrige uma redação existente com análise detalhada das 5 competências ENEM.

**Requisição:**

```json
{
  "tema": "Desafios da inclusão digital no Brasil",
  "texto": "Aqui vai o texto completo da redação do aluno com no mínimo 100 caracteres..."
}
```

**Validação:**
- Tema obrigatório
- Texto deve ter no mínimo 100 caracteres
- Ambos os campos são obrigatórios

**Resposta de sucesso (200):**

```json
{
  "status": "success",
  "correcao": {
    "competencia_1": { "nota": 200, "analise": "..." },
    "competencia_2": { "nota": 160, "analise": "..." },
    "competencia_3": { "nota": 200, "analise": "..." },
    "competencia_4": { "nota": 180, "analise": "..." },
    "competencia_5": { "nota": 200, "analise": "..." },
    "nota_total": 940,
    "feedback_geral": "..."
  }
}
```

**Notas por competência (valores oficiais ENEM):** 0, 40, 80, 120, 160, 200

**Erros possíveis:**
- `400` - Campos obrigatórios faltando ou texto muito curto
- `500` - Erro ao chamar a API do Gemini

### `GET /temas-sugeridos`

Retorna uma lista com 10 temas sugeridos para prática.

**Resposta:**

```json
{
  "status": "success",
  "quantidade": 10,
  "temas_sugeridos": [
    "Os desafios da saúde pública no Brasil pós-pandemia",
    "A importância da educação ambiental nas escolas brasileiras",
    "..."
  ]
}
```

## ⚙️ Notas importantes

- Certifique-se de que o `GEMINI_API_KEY` está válido e ativo
- O modelo utilizado é **Gemini 3.5 Flash** (otimizado para velocidade e custo)
- As respostas são estruturadas em JSON usando schemas predefinidos
- Erros na API retornam com mensagens descritivas
- Limite mínimo de caracteres para temas: 10 caracteres
- Limite mínimo de caracteres para textos a corrigir: 100 caracteres

## 🧪 Testando a API

### Usando cURL

```bash
# Gerar redação
curl -X POST http://127.0.0.1:5000/gerar-redacao \
  -H "Content-Type: application/json" \
  -d '{"tema": "A importância da educação no desenvolvimento do país"}'

# Corrigir redação
curl -X POST http://127.0.0.1:5000/corrigir-redacao \
  -H "Content-Type: application/json" \
  -d '{"tema": "Um tema", "texto": "Um texto de redação com pelo menos 100 caracteres para ser corrigido pela API..."}'

# Obter temas sugeridos
curl http://127.0.0.1:5000/temas-sugeridos
```

### Usando Postman

1. Crie uma requisição POST para `http://127.0.0.1:5000/gerar-redacao`
2. Na aba "Body", selecione "raw" e "JSON"
3. Passe: `{"tema": "seu tema aqui"}`
4. Clique em Send

## 📦 Variáveis de ambiente

| Variável | Descrição | Obrigatório |
|----------|-----------|------------|
| `GEMINI_API_KEY` | Chave da API Gemini | ✅ Sim |

## 🚀 Deploy

### Vercel

Este projeto está pronto para deploy no Vercel:

```bash
vercel deploy
```

A configuração está em `vercel.json`

### Outras plataformas

- **Heroku**: Use `Procfile` (não incluído)
- **Railway**: Compatível com Python/Flask
- **Replit**: Execute diretamente

## 📚 Estrutura do projeto

```
ProjetoComIA_backend/
├── app.py              # Aplicação principal com endpoints
├── config.py           # Schemas JSON e instruções do sistema
├── requirements.txt    # Dependências Python
├── vercel.json         # Configuração de deploy
├── .env               # Variáveis de ambiente (não versionar)
└── readme.md          # Este arquivo
```

## 📝 Licença

Projetado para uso educacional e de demonstração.

## 👨‍💻 Autor

Desenvolvido como projeto de Programação Back-end com IA.
