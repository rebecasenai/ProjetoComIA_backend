# ProjetoComIA_backend

API Flask para geração automática de redações estilo ENEM usando o modelo Gemini da Google.

## Visão Geral

Este projeto fornece um backend em Python que recebe um tema de redação e retorna um texto estruturado em JSON com:
- título
- introdução
- desenvolvimento
- conclusão
- referências
- análise das competências do ENEM

A ideia é criar redações originais e formatadas para simular uma redação pontuada com potencial para nota 1000.

## Tecnologias

- Python 3.x
- Flask
- Flask-CORS
- google-genai
- python-dotenv

## Arquivos principais

- `app.py` - aplicação Flask e endpoints REST
- `config.py` - configuração do schema JSON e instruções de sistema para o modelo
- `requirements.txt` - dependências do projeto
- `vercel.json` - configuração de deploy para Vercel

## Instalação

1. Clone o repositório:

```bash
git clone <seu-repositorio>
cd ProjetoComIA_backend
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto com a variável:

```env
GEMINI_API_KEY=seu_token_gemini_aqui
```

## Uso local

Execute a aplicação:

```bash
python app.py
```

A API ficará disponível em `http://127.0.0.1:5000`.

## Endpoints

### `GET /`

Retorna status da API.

Exemplo de resposta:

```json
{
  "status": "success",
  "message": "API Gerador de Redações ENEM 1000 funcionando!",
  "version": "2.0",
  "descricao": "Gerador automático de redações nota 1000 para o ENEM"
}
```

### `POST /gerar-redacao`

Gera uma redação com base em um tema.

Corpo da requisição:

```json
{
  "tema": "Desafios da inclusão digital no Brasil"
}
```

Exemplo de resposta de sucesso:

```json
{
  "status": "success",
  "tema_solicitado": "Desafios da inclusão digital no Brasil",
  "redacao": { ... },
  "mensagem_extra": "Redação gerada com sucesso! Continue praticando para alcançar a nota 1000! 📝✨"
}
```

### `GET /temas-sugeridos`

Retorna uma lista de temas sugeridos para redação.

Exemplo de resposta:

```json
{
  "status": "success",
  "quantidade": 10,
  "temas_sugeridos": [ ... ]
}
```

## Observações

- Certifique-se de que o `GEMINI_API_KEY` esteja válido.
- O modelo `gemini-2.5-flash` é usado para gerar texto estruturado em JSON.
- Caso o tema não seja fornecido corretamente, a API retorna erro 400.

## Deploy

O projeto está configurado para deploy no Vercel usando `vercel.json`.

## Licença

Projetado para uso educacional e de demonstração.
