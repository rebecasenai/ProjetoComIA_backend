import os
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from google import genai
from google.genai import types
from dotenv import load_dotenv
from config import REDACAO_SCHEMA, CORRECAO_SCHEMA, SYSTEM_INSTRUCTION

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

app = Flask(__name__)
CORS(app)

def generate_essay(tema):
    """
    Gera uma redação completa baseada no tema fornecido
    """
    # Conteúdo do prompt para o modelo
    conteudo_prompt = f"""
    Tema da redação: {tema}
    
    Por favor, crie uma redação completa seguindo todos os critérios do ENEM.
    A redação deve ser original, única e adequada ao tema proposto.
    """
    
    # Faz a chamada para o modelo pedindo uma resposta estruturada em JSON
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=conteudo_prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            response_mime_type="application/json",
            response_schema=REDACAO_SCHEMA,      
        )
    )
    return response.text


@app.route("/")
def root():
    return jsonify({
        "status": "success",
        "message": "API Gerador de Redações ENEM 1000 funcionando!",
        "version": "2.0",
        "descricao": "Gerador automático de redações nota 1000 para o ENEM"
    }), 200

@app.route("/gerar-redacao", methods=["POST"])
def generate_essay_endpoint():
    """
    Endpoint para gerar uma redação baseada no tema fornecido
    """
    print("=== NOVA REQUISIÇÃO RECEBIDA ===")
    
    data = request.get_json(force=True, silent=True)
    print(f"Dados recebidos no Back-end: {data}")
    
    if not data or "tema" not in data:
        return jsonify({
            "status": "error",
            "message": "Por favor, forneça um tema no formato: {'tema': 'seu tema aqui'}"
        }), 400
        
    tema = data.get("tema", "").strip()
    print(f"Tema extraído: '{tema}' (Tamanho: {len(tema)})")
    
    if not tema:
        return jsonify({
            "status": "error",
            "message": "O tema da redação não pode estar vazio."
        }), 400
    
    if len(tema) < 10:
        return jsonify({
            "status": "error",
            "message": "O tema deve ter pelo menos 10 caracteres."
        }), 400
    
    try:
        print("Chamando a API do Gemini...")
        redacao_json_string = generate_essay(tema)
        redacao_estruturada = json.loads(redacao_json_string)
        print("Redação gerada com sucesso pelo Gemini!")
        
        return jsonify({
            "status": "success",
            "tema_solicitado": tema,
            "redacao": redacao_estruturada
        }), 200
        
    except Exception as e:
        print(f"ERRO CRÍTICO NO BACK-END: {str(e)}")
        return jsonify({
            "status": "error",
            "message": f"Erro interno ao gerar a redação: {str(e)}"
        }), 500


# Certifique-se de ter importado o json no topo do arquivo:
# import json

@app.route("/corrigir-redacao", methods=["POST"])
def corrigir_redacao_endpoint():
    try:
        # 1. Tenta capturar os dados enviados
        data = request.get_json(force=True, silent=True)
        if not data:
            return jsonify({"status": "error", "message": "Nenhum dado JSON foi enviado no Body."}), 400
            
        tema = data.get("tema", "").strip()
        texto = data.get("texto", "").strip()
        
        if not tema or not texto:
            return jsonify({"status": "error", "message": "Faltando os campos 'tema' ou 'texto' no JSON."}), 400

        if len(texto) < 100:
            return jsonify({"status": "error", "message": "Texto muito curto (mínimo 100 caracteres)."}), 400

        # 2. Monta as instruções para a IA
        prompt_corretor = f"Tema: {tema}\nTexto do Aluno:\n{texto}"
        instruction_corretor = "Atue como corretor oficial do ENEM. Forneça notas de 0 a 200 para cada uma das 5 competências baseando-se estritamente nos critérios formais."

        # 3. Faz a chamada para a API do Gemini
        # Nota: Usamos CORRECAO_SCHEMA que definimos anteriormente
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt_corretor,
            config=types.GenerateContentConfig(
                system_instruction=instruction_corretor,
                response_mime_type="application/json",
                response_schema=CORRECAO_SCHEMA,      
            )
        )
        
        # 4. Tenta decodificar a resposta do Gemini
        try:
            correcao_estruturada = json.loads(response.text)
        except Exception as json_err:
            return jsonify({
                "status": "error", 
                "message": "A IA gerou a correção, mas ela veio em um formato inválido.",
                "detalhes": str(json_err),
                "resposta_crua": response.text
            }), 500
        
        return jsonify({
            "status": "success",
            "correcao": correcao_estruturada
        }), 200
        
    except Exception as e:
        # Se qualquer outra coisa falhar (como a API KEY ou o Schema), retorna o erro exato na tela
        return jsonify({
            "status": "error",
            "message": "Erro interno no servidor (Código 500)",
            "causa_exata": str(e)
        }), 500


@app.route("/temas-sugeridos", methods=["GET"])
def get_sugested_themes():
    """
    Retorna uma lista de temas sugeridos para redação
    """
    temas = [
        "Os desafios da saúde pública no Brasil pós-pandemia",
        "A importância da educação ambiental nas escolas brasileiras",
        "Desafios para a valorização do professor na educação básica",
        "O impacto das redes sociais na formação dos jovens",
        "A persistência da desigualdade de gênero no mercado de trabalho",
        "Desafios da mobilidade urbana nas grandes cidades brasileiras",
        "A importância da preservação do patrimônio histórico e cultural",
        "Desafios para o combate à fake news no Brasil",
        "O papel da tecnologia na democratização do acesso à educação",
        "A crise hídrica e a necessidade de conscientização ambiental"
    ]
    
    return jsonify({
        "status": "success",
        "quantidade": len(temas),
        "temas_sugeridos": temas
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
