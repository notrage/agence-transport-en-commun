import PySimpleGUI as sg

def Ajouter_un_conducteur(conn):
    """
    Ajouter un conducteur à la DB 

    :param conn: Connexion à la base de données
    """
    layout =   [[sg.Text("Matricule du conducteur"),sg.Input(key='-IMPUT_MAT-')],
                [sg.Text("Nom du conducteur"),sg.Input(key='-IMPUT_NOM-')],
                [sg.Text("Prenom du conducteur"),sg.Input(key='-IMPUT_PRENOM-')],
                [sg.CB('Bus',key="-CK_BUS-"), sg.CB('Tram',key="-CK_TRAM-")],
                [sg.Submit('Valider'), sg.Cancel('Annuler')]]

    # Create the window
    window = sg.Window('ADMIN PANEL', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Annuler': # if user closes window or clicks cancel
            break
        # Vérification de la validité des données
        if event == 'Valider':
            mat,nom,prenom,bus,tram = values['-IMPUT_MAT-'],str(values['-IMPUT_NOM-']),str(values['-IMPUT_PRENOM-']),values['-CK_BUS-'],values['-CK_TRAM-']
            print(values,type(nom),len(nom))
            # Matricule est un entier
            if mat.isdigit():
                # Matricule positif
                if int(mat) > 0:
                    # Nom/prenom non vide
                    if not nom.strip() == '' and not prenom.strip() == '':
                        # Verification que bus et/ou tram est coché
                        if bus or tram:
                            print("Ajout en cours")
                        else:
                            sg.Popup("Erreur : le conducteur doit pouvoir conduire un tram et/ou un bus")
                    else:
                        sg.Popup("Erreur : le nom et le prenom ne peuvent pas être vide")
                else:
                    sg.Popup("Erreur : le matricule doit être un positif")
            else:
                sg.Popup("Erreur : le matricule doit être un nombre entier positif")

    window.close()
