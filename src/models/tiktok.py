class TikTokAnalyzer:
    def analyze(self, data: dict) -> list:
        recs = []
        
        is_genz_segment = data.get('target_audience_age') == '18-24' and data.get('objective') == 'conversions'

        # 1. Regra de Gancho (A regra de ouro do TikTok)
        if not data.get('has_hook'):
            if is_genz_segment:
                recs.append("Alerta de Segmento Gen Z: Para campanhas de conversao com o publico de 18-24 anos, a atencao e altamente volatil. Adicionar um gancho (hook) inicial eleva o klike_score em 7.1 pontos neste segmento.")
            else:
                recs.append("Adicione um gancho (hook) nos primeiros 3 segundos. No TikTok, a falta de um gancho penaliza o video severamente, causando o 'swipe' imediato. Inserir um hook eleva a media geral do score em expressivos 17.3 pontos.")
            
        # 2. Regra de Presenca Humana (O Paradoxo da Gen Z)
        has_face = data.get('has_face')
        if is_genz_segment:
            if has_face:
                recs.append("Alerta de Segmento Gen Z: O uso de rostos humanos ('talking heads') reduz a performance de conversao para 18-24 anos em 3.2 pontos. Para este publico, teste formatos nativos sem rosto (POV, unboxing estetico ou gameplays).")
            else:
                recs.append("Nota de Segmento Gen Z: O criativo nao possui rosto. Excelente escolha! Para o publico de 18-24 anos em campanhas de conversao, videos sem rosto driblam o 'radar de anuncios' e performam 3.2 pontos melhor.")
        else:
            if not has_face:
                recs.append("Inclua rostos humanos no criativo. No cenario geral do TikTok, o formato liderado por criadores gera identificacao imediata e eleva a media do klike_score em 10.7 pontos.")
            
        # 3. Regra de Duracao (A Evolucao do Algoritmo)
        duration = data.get('video_duration_s', 0)
        if duration > 0:
            if is_genz_segment:
                if duration > 30:
                    recs.append("Alerta de Segmento Gen Z: Videos longos (+30s) perdem a atencao deste publico em campanhas de conversao (cai para 53.4 pontos). Reduza para a faixa media (16-30s) para atingir o pico de 63.7 pontos (ganho de 10.3 pontos).")
                elif duration <= 15:
                    recs.append("Nota de Segmento Gen Z: O video e muito curto (ate 15s) e tem performance razoavel (58.8). Porem, o 'sweet spot' para convencao deste publico e a duracao media (16-30s), que eleva o score para 63.7.")
            else:
                if duration <= 15:
                    recs.append("Considere testar videos mais longos. No cenario geral do TikTok atual, videos muito curtos (ate 15s) tem a menor media (60.8). Formatos medios e longos (+30s) performam melhor, chegando a 65.0 pontos.")
            
        # 4. Regra de Formato Nativo
        if data.get('format') != 'vertical':
            recs.append("Mude o formato para 'vertical' (9:16). O TikTok e uma plataforma 100% vertical. Videos quadrados ou horizontais geram bordas pretas e sao fortemente penalizados pelo algoritmo.")
            
        # 5. Regra de Categoria e Som (App Install)
        if data.get('category') == 'App Install' and data.get('music_voice_ratio', 0) < 0.5:
            recs.append("Para App Install no TikTok, aumente a proporcao de musicas/audios virais em relacao a voz. O apelo sonoro e nativo dita grande parte do engajamento nesta plataforma.")

        # 6. Regra de Chamada para Acao (O Direcionamento Gen Z)
        if not data.get('has_cta'):
            if is_genz_segment:
                recs.append("Alerta de Segmento Gen Z: Embora rejeitem formatos muito 'vendedores', o publico de 18-24 anos age por impulso e precisa saber exatamente qual e o proximo passo. Adicionar um Call to Action (CTA) em campanhas de conversao eleva o score em 7.8 pontos.")
            else:
                recs.append("Insira um Call to Action (CTA). No cenario geral do TikTok, direcionar o usuario de forma clara e rapida eleva a media do klike_score em 9.2 pontos.")

        # 7. Regra de Acessibilidade e Retencao (Legendas)
        if not data.get('has_subtitle'):
            if is_genz_segment:
                recs.append("Recomendacao de Segmento Gen Z: O TikTok e uma plataforma 'sound-on', mas as legendas funcionam como uma ancora visual. Para o publico de 18-24 anos em conversao, adicionar legendas eleva o score em 4.2 pontos.")
            else:
                recs.append("Adicione legendas ao video. No cenario geral do TikTok, as legendas ajudam a reter o usuario que le enquanto ouve a mensagem, elevando a media do klike_score em aproximadamente 6.7 pontos.")

        # 8. Regra de Poluicao Visual (Densidade de Texto)
        text_density = data.get('text_density')
        if text_density == 'high':
            if is_genz_segment:
                recs.append("Alerta de Segmento Gen Z: Textoes nao funcionam para este publico. A densidade de texto 'alta' afunda a performance de conversao para 47.0 pontos. Reduza para densidade 'baixa' (foco total no visual) e recupere 17.1 pontos.")
            else:
                recs.append("Reduza a densidade de texto na tela. No TikTok, poluir o video com muito texto ('high') derruba o score. O cenario ideal para a plataforma costuma ser a densidade 'media' (textos curtos e dinamicos).")

        return recs