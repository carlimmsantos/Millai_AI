class MetaAnalyzer:
    def analyze(self, data: dict) -> list:
        recs = []
        duration = data.get('video_duration_s', 0)
        age = data.get('target_audience_age')
        objective = data.get('objective')

        # 1. Regra de Gancho (Maior preditor de sucesso)
        if not data.get('has_hook'):
            if age == '35-44' and objective == 'conversions':
                recs.append("Alerta Critico: Para campanhas de conversao focadas no publico de 35-44 anos, a ausencia de um gancho (hook) penaliza severamente o anuncio. Adicionar um hook pode elevar o score em 19.8 pontos neste segmento.")
            else:
                recs.append("Adicionar um gancho (hook) nos primeiros 3 segundos do video poderia elevar a media do klike_score em aproximadamente 18 pontos, com base na analise historica de retencao.")
            
        # 2. Regra de Presenca Humana (Forte impacto positivo)
        if not data.get('has_face'):
            if age == '35-44' and objective == 'conversions':
                recs.append("Alerta de Segmento: Para campanhas de conversao focadas no publico de 35-44 anos, a presenca de um rosto humano e fundamental para gerar confianca. Incluir pessoas no criativo pode elevar o klike_score em 16.4 pontos neste segmento.")
            else:
                recs.append("Inclua rostos humanos no criativo. Historicamente, a presenca de pessoas gera identificacao imediata e pode elevar a media do klike_score em aproximadamente 13 pontos gerais.")
            
        # 3. Regra de Chamada para Acao (Direcionamento)
        if not data.get('has_cta'):
            if age == '35-44' and objective == 'conversions':
                recs.append("Nota de Segmento: O criativo nao possui CTA. Excelente escolha! Para o publico de 35-44 anos em campanhas de conversao, os dados mostram que abordagens sutis funcionam melhor e a ausencia de um CTA explicito ajuda a manter o klike_score estavel.")
            else:
                recs.append("Insira um Call to Action (CTA) claro. No cenario geral, criativos com um direcionamento explicito elevam a media do klike_score em aproximadamente 7.6 pontos.")
            
        # 4. Regra de Acessibilidade e Retencao (Legendas)
        if not data.get('has_subtitle'):
            if age == '35-44' and objective == 'conversions':
                recs.append("Recomendacao de Segmento: Adicione legendas ao video. Para campanhas de conversao com o publico de 35-44 anos, as legendas facilitam o consumo do conteudo e elevam o klike_score em 5.5 pontos.")
            else:
                recs.append("Adicione legendas ao video. No cenario geral, as legendas garantem a retencao de usuarios que navegam com o som mutado e elevam a media do klike_score em aproximadamente 7.4 pontos.")

        # 5. Regra de Poluicao Visual (Impacto negativo)
        if data.get('text_density') == 'high':
            if age == '35-44' and objective == 'conversions':
                recs.append("Alerta Critico: A densidade de texto 'alta' derruba a performance neste segmento. Reduzir para 'baixa' recupera 16.7 pontos, mas o ideal absoluto e usar a densidade 'media', que eleva o score para o pico de 72.5 pontos.")
            else:
                recs.append("Reduza a densidade de texto na tela para 'medium' (ideal) ou 'low'. Excesso de texto sobreposto prejudica a visualizacao e penaliza o klike_score em mais de 18 pontos em relacao a densidade media.")

        # 6. Regras de Estrategia e Segmentacao
        category = data.get('category')
        if category == 'E-commerce' and not data.get('is_retargeting'):
            recs.append("Para a categoria E-commerce, campanhas para publico frio tem menor eficiencia. Considere focar em Retargeting.")

        # 7. Regra de Dinamica de Publico e Duracao
        if age == '35-44' and objective == 'conversions':
            if duration > 30:
                recs.append("Alerta Critico: Para campanhas de conversao (35-44 anos), videos longos (+30s) penalizam severamente a performance. Reduza para a faixa media (16 a 30 segundos) para obter um ganho expressivo de 17.1 pontos.")
            elif duration <= 15 and duration > 0:
                recs.append("Otimizacao de Segmento: O video e curto (ate 15s) e possui uma boa performance. No entanto, para o publico de 35-44 anos, videos de duracao media (16 a 30s) sao o cenario ideal e podem elevar o score em mais 7.5 pontos.")
        elif age == '18-24' and duration > 30:
            recs.append("O publico de 18-24 anos apresenta menor tempo de atencao. Reduza a duracao do video para menos de 30 segundos.")

        return recs