# config.py - Configurações para o Gerador de Redações

# ==============================================================================
# SCHEMA DA GERAÇÃO DE REDAÇÃO (Usado na rota /gerar-redacao)
# ==============================================================================
REDACAO_SCHEMA = {
    "type": "object",
    "properties": {
        "titulo": {
            "type": "string",
            "description": "Título criativo e relevante para a redação"
        },
        "introducao": {
            "type": "string", 
            "description": "Parágrafo introdutório com apresentação do tema e tese"
        },
        "desenvolvimento": {
            "type": "object",
            "properties": {
                "paragrafo_1": {
                    "type": "string",
                    "description": "Primeiro parágrafo de desenvolvimento com argumentos e exemplos"
                },
                "paragrafo_2": {
                    "type": "string",
                    "description": "Segundo parágrafo de desenvolvimento com argumentos e exemplos"
                },
                "paragrafo_3": {
                    "type": "string",
                    "description": "Terceiro parágrafo de desenvolvimento (opcional, se necessário)"
                }
            },
            "required": ["paragrafo_1", "paragrafo_2"]
        },
        "conclusao": {
            "type": "string",
            "description": "Parágrafo de conclusão com resumo dos pontos e reafirmação da tese"
        },
        "referencias": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Lista de fontes e referências utilizadas"
        },
        "analise_criterios_enem": {
            "type": "object",
            "properties": {
                "competencia_1": {
                    "type": "string",
                    "description": "Análise da competência 1 (Domínio da escrita formal)"
                },
                "competencia_2": {
                    "type": "string", 
                    "description": "Análise da competência 2 (Compreensão do tema)"
                },
                "competencia_3": {
                    "type": "string",
                    "description": "Análise da competência 3 (Argumentação)"
                },
                "competencia_4": {
                    "type": "string",
                    "description": "Análise da competência 4 (Coesão e coerência)"
                },
                "competencia_5": {
                    "type": "string",
                    "description": "Análise da competência 5 (Proposta de intervenção)"
                }
            }
        }
    },
    "required": ["titulo", "introducao", "desenvolvimento", "conclusao", "referencias", "analise_criterios_enem"]
}

# ==============================================================================
# SCHEMA DA CORREÇÃO DE REDAÇÃO (Usado na rota /corrigir-redacao)
# ==============================================================================
CORRECAO_SCHEMA = {
    "type": "object",
    "properties": {
        "nota_total": {"type": "integer", "description": "Soma das notas das 5 competências (0 a 1000)"},
        "competencia_1": {
            "type": "object",
            "properties": {
                "nota": {"type": "integer", "description": "Nota de 0, 40, 80, 120, 160 ou 200"},
                "justificativa": {"type": "string", "description": "Erros gramaticais encontrados e avaliação da norma culta"}
            },
            "required": ["nota", "justificativa"]
        },
        "competencia_2": {
            "type": "object",
            "properties": {
                "nota": {"type": "integer", "description": "Nota de 0, 40, 80, 120, 160 ou 200"},
                "justificativa": {"type": "string", "description": "Avaliação da compreensão do tema e repertório legítimo e produtivo"}
            },
            "required": ["nota", "justificativa"]
        },
        "competencia_3": {
            "type": "object",
            "properties": {
                "nota": {"type": "integer", "description": "Nota de 0, 40, 80, 120, 160 ou 200"},
                "justificativa": {"type": "string", "description": "Avaliação do projeto de texto, argumentação e seleção de fatos"}
            },
            "required": ["nota", "justificativa"]
        },
        "competencia_4": {
            "type": "object",
            "properties": {
                "nota": {"type": "integer", "description": "Nota de 0, 40, 80, 120, 160 ou 200"},
                "justificativa": {"type": "string", "description": "Avaliação dos conectivos interparágrafos e intraparágrafos e repetições"}
            },
            "required": ["nota", "justificativa"]
        },
        "competencia_5": {
            "type": "object",
            "properties": {
                "nota": {"type": "integer", "description": "Nota de 0, 40, 80, 120, 160 ou 200"},
                "justificativa": {"type": "string", "description": "Avaliação dos 5 elements da proposta: agente, ação, meio/modo, detalhamento e efeito"}
            },
            "required": ["nota", "justificativa"]
        },
        "comentario_geral": {"type": "string", "description": "Análise geral do texto e principais pontos de melhoria"}
    },
    "required": ["nota_total", "competencia_1", "competencia_2", "competencia_3", "competencia_4", "competencia_5", "comentario_geral"]
}

# ==============================================================================
# SYSTEM INSTRUCTION PARA O GERADOR DE REDAÇÕES
# ==============================================================================
SYSTEM_INSTRUCTION = """
Você é um Professor altamente profissional e qualificado, especialista em preparação para o ENEM. 
Você já teve vários alunos que alcançaram nota 1000 na redação e excelente rendimento escolar.

SUA FUNÇÃO:
Criar redações perfeitas com potencial para nota 1000 no ENEM, seguindo rigorosamente os critérios oficiais.

REGRAS IMPORTANTES:
1. Cada redação deve ser ÚNICA e ORIGINAL - nunca repetir estruturas ou argumentos
2. Adaptar o conteúdo especificamente ao tema solicitado pelo aluno
3. Seguir a estrutura padrão ENEM: Título, Introdução, Desenvolvimento (2-3 parágrafos), Conclusão, Referências
4. Incluir obrigatoriamente PROPOSTA DE INTERVENÇÃO detalhada na conclusão (agente, ação, meio, finalidade)
5. Utilizar repertório sociocultural variado (filósofos, sociólogos, dados, obras literárias, filmes)
6. Manter linguagem formal e impessoal, adequada à norma culta
7. Garantir coesão e coerência textual em toda a redação
8. Fornecer análise detalhada das 5 competências do ENEM

ESTRUTURA OBRIGATÓRIA DA REDAÇÃO:

1. TÍTULO: Criativo, impactante e relacionado ao tema (pode ser uma pergunta, declaração ou referência cultural)

2. INTRODUÇÃO:
   - Contextualização do tema (conectando com questões históricas, sociais ou culturais)
   - Apresentação clara da TESE (posicionamento do autor)
   - Mínimo 6 linhas

3. DESENVOLVIMENTO (2 ou 3 parágrafos):
   - Cada parágrafo com um ARGUMENTO central
   - Uso de CONECTORES lógicos (além disso, portanto, contudo, etc.)
   - Exemplificação com dados, fatos ou citações relevantes
   - Cada parágrafo com 8-10 linhas

4. CONCLUSÃO:
   - Síntese dos argumentos apresentados
   - Retomada da tese inicial
   - PROPOSTA DE INTERVENÇÃO completa (5 elementos: agente, ação, modo/meio, efeito, finalidade)
   - Respeito aos direitos humanos

5. REFERÊNCIAS:
   - Listar 3-5 fontes confiáveis que embasaram a argumentação
   - Incluir autores, obras e dados relevantes

A redação deve alcançar NOTA 1000 em todas as competências:
✓ C1: Demonstrar domínio da modalidade escrita formal
✓ C2: Compreender a proposta e aplicar conceitos
✓ C3: Selecionar e organizar argumentos
✓ C4: Demonstrar conhecimento dos mechanisms linguísticos
✓ C5: Elaborar proposta de intervenção detalhada

Lembre-se: Cada redação é uma nova criação! Seja criativo, use repertórios variados e mantenha sempre a excelência acadêmica.
"""