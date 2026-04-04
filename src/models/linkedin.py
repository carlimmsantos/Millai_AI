class LinkedInAnalyzer:
    def analyze(self, data: dict) -> list:
        recs = []
        
        is_gold_segment = data.get('target_audience_age') == '35-44' and data.get('objective') == 'conversions'

        # 1. Regra de Gancho (Baseada nos dados de Klike Score)
        if not data.get('has_hook'):
            if is_gold_segment:
                recs.append("Alerta de Segmento B2B: Em campanhas de conversao no LinkedIn para o publico de 35-44 anos, adicionar um gancho (hook) inicial eleva o klike_score em 9.6 pontos.")
            else:
                recs.append("Adicione um gancho (hook) inicial. No cenario geral do LinkedIn, a presenca de um gancho no inicio do video eleva a media do klike_score em aproximadamente 15.9 pontos.")

        # 2. Regra de Presenca Humana (Humanizacao B2B)
        if not data.get('has_face'):
            if is_gold_segment:
                recs.append("Alerta de Segmento B2B: Para o publico de 35-44 anos focado em conversao, a presenca de um rosto humano e vital para gerar confianca corporativa. Incluir pessoas eleva o score em 17.3 pontos neste segmento.")
            else:
                recs.append("Inclua rostos humanos no criativo. No LinkedIn, humanizar a comunicacao quebra o padrao excessivamente corporativo e eleva a media do klike_score em aproximadamente 13.1 pontos gerais.")

        # 3. Regra do Audio Mutado (Crucial no LinkedIn)
        if not data.get('has_subtitle'):
            if is_gold_segment:
                recs.append("Recomendacao de Segmento B2B: Adicione legendas urgentes. Para o publico de 35-44 anos focado em conversao, ler o conteudo no mudo e o padrao no ambiente de trabalho. Legendas elevam o klike_score em 8.7 pontos neste segmento.")
            else:
                recs.append("Adicione legendas ao video. No LinkedIn, o consumo silencioso de conteudo e altissimo. Garantir que sua mensagem seja lida sem audio eleva a media do klike_score em aproximadamente 5.5 pontos gerais.")
            
        # 4. Regra de Formato Desktop
        if data.get('format') == 'vertical':
            recs.append("Troque para formato 'horizontal' ou 'quadrado'. O feed do LinkedIn no desktop corta videos verticais, prejudicando a visualizacao da mensagem.")
            
        # 5. Regra de Custo / Retargeting
        category = data.get('category')
        if category in ['SaaS', 'Lead Gen'] and not data.get('is_retargeting'):
            recs.append("O CPC no LinkedIn para SaaS/Lead Gen e altissimo em publico frio. Transforme essa campanha em Retargeting para focar em leads mais quentes e baratear a aquisicao.")
            
        # 6. Regra de Chamada para Acao (Direcionamento B2B)
        if not data.get('has_cta'):
            if is_gold_segment:
                recs.append("Alerta de Segmento B2B: Diferente de outras redes, tomadores de decisao (35-44 anos) no LinkedIn esperam direcionamento claro. Adicionar um Call to Action (CTA) em campanhas de conversao eleva o score em 8.7 pontos.")
            else:
                recs.append("Profissionais precisam de clareza sobre o proximo passo. No cenario geral do LinkedIn, a presenca de um CTA eleva a media do klike_score em 8.7 pontos.")

        # 7. Regra de Poluicao Visual (O Paradoxo do B2B)
        text_density = data.get('text_density')
        if is_gold_segment and text_density == 'medium':
            recs.append("Alerta de Segmento B2B: A densidade de texto 'media' e a pior escolha para este publico (cai para 44.6 pontos). Va para os extremos: use 'low' para videos focados no porta-voz, ou 'high' se for um material rico/tecnico (infograficos e slides).")
        elif not is_gold_segment and text_density == 'high':
            recs.append("Reduza a densidade de texto na tela. No cenario geral do LinkedIn, excesso de texto ('high') derruba o score para 47.4. O ponto ideal costuma ser a densidade 'media'.")

        # 8. Regra de Duracao de Video (O Elevator Pitch B2B)
        duration = data.get('video_duration_s', 0)
        if duration > 0:
            if is_gold_segment:
                if duration <= 15:
                    recs.append("Alerta de Segmento B2B: Videos muito curtos (ate 15s) performam mal para tomadores de decisao (47.0 pontos). O publico de 35-44 anos precisa de um 'Elevator Pitch'. Aumente para 16-30s e ganhe ate 13.4 pontos.")
                elif duration > 30:
                    recs.append("Alerta de Segmento B2B: Videos longos (+30s) perdem a atencao do publico de 35-44 anos (48.9 pontos). Reduza para a faixa media (16-30s) para atingir o pico de performance de 60.4 pontos.")
            else:
                if duration <= 15 or duration > 30:
                    recs.append("Otimize a duracao do video. No LinkedIn, o ponto ideal de retencao e klike_score geral fica na faixa media de 16 a 30 segundos.")

        return recs