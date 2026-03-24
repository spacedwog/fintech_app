from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.styles = getSampleStyleSheet()

    def gerar_pdf(self, epic, stories, invest_list, prioridades):
        doc = SimpleDocTemplate(self.filename)
        elementos = []

        # Épico
        elementos.append(Paragraph("ÉPICO", self.styles['Heading1']))
        elementos.append(Paragraph(epic.nome, self.styles['Heading2']))
        elementos.append(Paragraph(epic.justificativa, self.styles['Normal']))
        elementos.append(Spacer(1, 12))

        # User Stories
        elementos.append(Paragraph("USER STORIES", self.styles['Heading1']))
        for s in stories:
            elementos.append(Paragraph(s.descricao, self.styles['Heading3']))
            for c in s.criterios:
                elementos.append(Paragraph(f"- {c}", self.styles['Normal']))
            elementos.append(Spacer(1, 12))

        # INVEST
        elementos.append(Paragraph("VALIDAÇÃO INVEST", self.styles['Heading1']))
        for inv in invest_list:
            elementos.append(Paragraph(inv.historia, self.styles['Heading3']))
            for k, v in inv.validacoes.items():
                elementos.append(Paragraph(f"{k}: {v}", self.styles['Normal']))
            elementos.append(Spacer(1, 12))

        # Prioridades
        elementos.append(Paragraph("PRIORIZAÇÃO", self.styles['Heading1']))
        for p in prioridades:
            elementos.append(Paragraph(p.historia, self.styles['Heading3']))
            elementos.append(Paragraph(p.justificativa, self.styles['Normal']))
            elementos.append(Spacer(1, 12))

        doc.build(elementos)