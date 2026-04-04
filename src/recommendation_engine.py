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
        
    def gerar_relatorio(self, campaign_data: dict) -> str:
        platform = campaign_data.get('platform')
        campaign_id = campaign_data.get('campaign_id', 'Desconhecida')
        
        # Verifica se a plataforma existe no nosso sistema
        if platform not in self.analyzers:
            return f"Plataforma '{platform}' não suportada pelo motor de recomendações."
            
        # Chama a classe e gera a lista bruta de problemas
        analyzer = self.analyzers[platform]
        recomendacoes_brutas = analyzer.analyze(campaign_data)
        
        relatorio = f"=== DIAGNÓSTICO DA CAMPANHA: {campaign_id} ({platform}) ===\n\n"
        
        if not recomendacoes_brutas:
            relatorio += "Excelente trabalho! O vídeo atende a todas as melhores práticas mapeadas pelos nossos dados para este segmento. Não foram encontrados pontos críticos de melhoria.\n"
        else:
            recs_finais = recomendacoes_brutas[:5]
            for i, rec in enumerate(recs_finais, start=1):
                relatorio += f"{i}. {rec}\n"
                
        return relatorio