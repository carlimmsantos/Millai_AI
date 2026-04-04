# Importando as classes dos outros arquivos
from .models.meta import MetaAnalyzer
from .models.tiktok import TikTokAnalyzer
from .models.linkedin import LinkedInAnalyzer

class RecommendationEngine:
    def __init__(self):
        # Mapeando qual classe usar para cada plataforma
        self.analyzers = {
            'Meta': MetaAnalyzer(),
            'TikTok': TikTokAnalyzer(),
            'LinkedIn': LinkedInAnalyzer()
        }
        
        # Removemos os fallbacks genéricos. Se o vídeo está bom, devemos assumir isso.

    def gerar_relatorio(self, campaign_data: dict) -> str:
        platform = campaign_data.get('platform')
        campaign_id = campaign_data.get('campaign_id', 'Desconhecida')
        
        # Verifica se a plataforma existe no nosso sistema
        if platform not in self.analyzers:
            return f"Plataforma '{platform}' não suportada pelo motor de recomendações."
            
        # Chama a classe correta e gera a lista bruta de problemas
        analyzer = self.analyzers[platform]
        recomendacoes_brutas = analyzer.analyze(campaign_data)
        
        relatorio = f"=== DIAGNÓSTICO DA CAMPANHA: {campaign_id} ({platform}) ===\n\n"
        
        # Lógica de Feedback: Verifica se a lista de erros está vazia
        if not recomendacoes_brutas:
            relatorio += "Excelente trabalho! O vídeo atende a todas as melhores práticas mapeadas pelos nossos dados para este segmento. Não foram encontrados pontos críticos de melhoria.\n"
        else:
            # Garante que exibiremos no máximo os 3 principais problemas encontrados
            recs_finais = recomendacoes_brutas[:3]
            for i, rec in enumerate(recs_finais, start=1):
                relatorio += f"{i}. {rec}\n"
                
        return relatorio