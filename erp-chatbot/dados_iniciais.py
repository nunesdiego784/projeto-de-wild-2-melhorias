from validacoes import cabecalho, linha, pausar


def info_horarios():
    cabecalho("Horários de Atendimento")
    print("  Segunda a Sexta: 08h às 18h")
    print("  Sábado:          09h às 13h")
    print("  Domingo:         Fechado")
    pausar()

def info_contato():
    cabecalho("Canais de Contato")
    print("   Telefone : (11) 1234-5678")
    print("   E-mail   : suporte@casadecampocentral011.com")
    pausar()

def info_politicas():
    cabecalho("Políticas e Termos")
    print("  • Prazo de devolução: 7 dias corridos")
    print("  • Garantia padrão   : 12 meses")
    print("  • Privacidade       : www.casadecampocentral011.com/privacidade")
    pausar()

def info_faq():
    cabecalho("Perguntas Frequentes (FAQ)")
    faqs = [
        ("Como rastrear meu pedido?", "Acesse 'Pedidos > Rastrear Pedido' ou use o código no e-mail."),
        ("Posso trocar um produto?",  "Sim, dentro de 7 dias com nota fiscal."),
        ("Aceitam cartão de débito?", "Sim, todas as bandeiras principais."),
    ]
    for i, (p, r) in enumerate(faqs, 1):
        print(f"\n  {i}. {p}")
        print(f"     → {r}")
    pausar()
