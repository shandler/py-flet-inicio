import flet

from flet import Text, TextField, Row, FilledButton, Banner, Icon, colors, TextButton, icons

def main(page):

    dict_value = {
        "contratante" : '',
        "medida_juricial" : '',
        "outra_parte" : '',
        "prolabore" : '',
        "exito" : '',
        "foro" : '',
        "data" : ''
    }

    def gera_contrato(e):
        dict_value['contratante'] = contratante.value
        dict_value['medida_juricial'] = medida_juricial.value
        dict_value['outra_parte'] = outra_parte.value
        dict_value['prolabore'] = prolabore.value
        dict_value['exito'] = exito.value
        dict_value['foro'] = foro.value
        dict_value['data'] = data.value
        for val in dict_value.values():
            if not val:
                page.banner.open=True
                page.update()
                return

        print("Já é possível gerar o contrato.")
    
    def fecha_banner(e):
        page.banner.open=False
        page.update()

    page.banner = Banner(
        bgcolor=colors.AMBER_100,
        leading=Icon(
            icons.DANGEROUS_SHARP,
            color=colors.RED_400,
            size=40
            ),
        content=Text('Opa! Todos os campos são de preenchimento obrigatório.'),
        actions= [
            TextButton(
                'Entendi',
                on_click=fecha_banner
            )
        ]

    )

    titulo = Text("Gerador de Contrato de Prestação de Serviços Advocatícios", size=30, weight="bold")
    contratante = TextField(label="Nome do Contratante", autofocus=True)
    medida_juricial = TextField(label="Medida Juricial")
    outra_parte = TextField(label="Outra Parte")
    prolabore = TextField(label="Prolabore", prefix_text='RS ')
    exito = TextField(label="Exito", suffix_text=' %')
    foro = TextField(label="Foro")
    data = TextField(label="Data")

    botao_gerar = FilledButton(text='Gerar Contrato', on_click=gera_contrato)

    page.add (
        Row(
            controls = [
                titulo
            ]
        ) ,       
        Row(
            controls = [
                contratante
            ]
        ),        
        Row(
            controls = [
                medida_juricial,
                outra_parte
            ]
        ) ,       
        Row(
            controls = [
                prolabore,
                exito
            ]
        ),
        Row(
            controls = [
                foro,
                data
            ]
        ),
        Row(
            controls = [
                botao_gerar
            ]
        )      
    )
    
flet.app(target=main)